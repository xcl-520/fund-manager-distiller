"""配置管理"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from pathlib import Path
import yaml
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


@dataclass
class AIConfig:
    """AI 提取配置"""
    enabled: bool = False
    provider: str = "openai"  # openai / claude / gemini
    model: str = "gpt-4-turbo"
    api_key: Optional[str] = None
    temperature: float = 0.3
    max_tokens: int = 2000

    def __post_init__(self):
        # 从环境变量读取 API Key
        if not self.api_key:
            env_key = f"{self.provider.upper()}_API_KEY"
            self.api_key = os.getenv(env_key)


@dataclass
class CrawlerConfig:
    """爬虫配置"""
    timeout: int = 30
    retry_times: int = 3
    delay_between_requests: float = 1.0
    user_agent: str = "Mozilla/5.0"


@dataclass
class OutputConfig:
    """输出配置"""
    formats: List[str] = field(default_factory=lambda: ["skill", "markdown", "json"])
    include_charts: bool = True
    include_examples: bool = True
    compress: bool = False


@dataclass
class CacheConfig:
    """缓存配置"""
    enabled: bool = True
    ttl: int = 604800  # 7 天
    path: str = ".cache/"


@dataclass
class DistillerConfig:
    """蒸馏器配置"""
    manager_name: str = ""
    fund_house: str = ""
    start_year: int = 2012
    end_year: Optional[int] = None
    
    # 子配置
    ai_extraction: AIConfig = field(default_factory=AIConfig)
    crawler: CrawlerConfig = field(default_factory=CrawlerConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    cache: CacheConfig = field(default_factory=CacheConfig)
    
    # 数据源
    sources: Dict[str, bool] = field(default_factory=lambda: {
        "efund": True,
        "ttjj": True,
        "media": True
    })
    
    # 蒸馏参数
    min_corpus_size: int = 10
    method_min_frequency: int = 3
    viewpoint_min_confidence: float = 0.6
    similarity_threshold: float = 0.8
    time_decay: float = 0.95
    
    # 其他
    verbose: bool = False
    logging_level: str = "INFO"
    
    def __post_init__(self):
        # 设置默认结束年份为当前年份
        if self.end_year is None:
            from datetime import datetime
            self.end_year = datetime.now().year


def load_config(config_file: str = "config.yaml") -> DistillerConfig:
    """
    从 YAML 配置文件加载配置
    
    Args:
        config_file: 配置文件路径
        
    Returns:
        DistillerConfig 对象
    """
    
    config_path = Path(config_file)
    
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_file}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # 解析各个配置段
    ai_config = AIConfig(**data.get('ai_extraction', {}))
    crawler_config = CrawlerConfig(**data.get('crawler', {}))
    output_config = OutputConfig(**data.get('output', {}))
    cache_config = CacheConfig(**data.get('cache', {}))
    
    # 创建主配置对象
    config = DistillerConfig(
        ai_extraction=ai_config,
        crawler=crawler_config,
        output=output_config,
        cache=cache_config,
        sources=data.get('sources', {}),
    )
    
    return config
