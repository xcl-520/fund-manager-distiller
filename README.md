# 🔬 Fund Manager Distiller | 基金经理蒸馏模型

> **一行命令蒸馏任意基金经理的投资观点、方法论和持仓特征**

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Type](https://img.shields.io/badge/Type-Universal%20Framework-black)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 核心特性

- ✅ **完全通用** - 输入任何基金经理名字即可启动蒸馏流程
- ✅ **自动化爬取** - 从易方达、天天基金等官方数据源自动获取
- ✅ **多维度蒸馏** - 语料 → 方法论 → 持仓特征 → 评分卡
- ✅ **溯源可验证** - 每个观点都标注来源和时间
- ✅ **Agent Skill 格式** - 原生支持 Claude Code 等 AI 工具
- ✅ **跨平台适配** - ChatGPT、Gemini、Cursor 等都能用

## 🚀 快速开始

### 方式一：命令行一键蒸馏

```bash
# 安装依赖
pip install -r requirements.txt

# 蒸馏指定基金经理
python main.py --manager "郑希" --fund-house "易方达"

# 蒸馏多个经理
python main.py --manager-list managers.txt

# 输出为 Agent Skill
python main.py --manager "郑希" --output-format skill
```

### 方式二：Python API

```python
from core.distiller import FundManagerDistiller

# 初始化蒸馏器
distiller = FundManagerDistiller()

# 蒸馏基金经理
result = distiller.distill(
    manager_name="郑希",
    fund_house="易方达",
    start_year=2012,
    end_year=2026
)

# 输出
print(result.to_skill_format())
```

## 📂 项目结构

```
fund-manager-distiller/
├── README.md
├── requirements.txt
├── config.yaml                    # 配置文件
├── main.py                        # CLI 入口
├── core/
│   ├── __init__.py
│   ├── distiller.py              # 核心蒸馏引擎
│   ├── data_crawler.py           # 数据爬取（官方 API）
│   ├── corpus_builder.py         # 语料库构建
│   ├── method_extractor.py       # 方法论提取
│   ├── fund_analyzer.py          # 持仓分析
│   └── scorecard_generator.py    # 评分卡生成
├── sources/
│   ├── efund_spider.py           # 易方达爬虫
│   ├── ttjj_spider.py            # 天天基金爬虫
│   ├── media_spider.py           # 媒体报道爬虫
│   └── official_api.py           # 官方 API 调用
├── models/
│   ├── manager.py                # 经理人模型
│   ├── fund.py                   # 基金模型
│   ├── viewpoint.py              # 观点模型
│   └── method_framework.py       # 方法框架模型
├── prompts/
│   ├── extraction.yaml           # 观点提取提示词
│   ├── method_distill.yaml       # 方法论蒸馏提示词
│   └── scoring_rules.yaml        # 评分规则提示词
├── templates/
│   ├── skill_template.md         # Skill 模板
│   ├── method_template.md        # 方法论模板
│   ├── corpus_template.md        # 语料库模板
│   └── scorecard_template.md     # 评分卡模板
├── output/
│   └── [manager_name]/           # 输出目录（自动生成）
│       ├── SKILL.md
│       ├── README.md
│       ├── references/
│       │   ├── method.md
│       │   ├── scorecard.md
│       │   ├── corpus/
│       │   ├── fund_data/
│       │   └── all_funds/
│       └── scripts/
└── tests/
    ├── test_distiller.py
    ├── test_crawlers.py
    └── test_extractors.py
```

## 🔧 配置指南

编辑 `config.yaml`：

```yaml
# 数据源
sources:
  efund: true              # 易方达官方数据
  ttjj: true              # 天天基金
  media: true             # 媒体报道
  
# AI 提取（可选，提升准确度）
ai_extraction:
  enabled: true
  provider: "openai"      # openai / claude / gemini
  model: "gpt-4"
  api_key: "${OPENAI_API_KEY}"

# 输出格式
output:
  formats: ["skill", "markdown", "json"]
  include_charts: true
  
# 爬虫设置
crawler:
  timeout: 30
  retry: 3
  delay: 1
```

## 📊 蒸馏流程

```
┌─────────────────────────────────────┐
│  输入：基金经理名字 & 基金公司      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Step 1: 数据爬取                   │
│  • 定期报告（季报/年报）           │
│  • 基金经理手记                    │
│  • 媒体采访报道                    │
│  • 持仓数据快照                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Step 2: 语料库构建                 │
│  • 文本清洗 & 分段                 │
│  • 时间标注                        │
│  • 出处溯源                        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Step 3: 观点提取 (AI 辅助)        │
│  • 聚类相同主题观点                │
│  • 标注立场（看好/看淡/中立）     │
│  • 提取关键论据                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Step 4: 方法论蒸馏                 │
│  • 投资框架识别                    │
│  • 选股逻辑提取                    │
│  • 风险管理方法                    │
│  • 周期判断标准                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Step 5: 持仓特征分析               │
│  • 风格漂移跟踪                    │
│  • 换手率 / 集中度分析              │
│  • 行业偏好识别                    │
│  • 持仓与表述对照                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Step 6: 评分卡生成                 │
│  • 多维度评分规则                  │
│  • 对标其他经理人                  │
│  • 历史表现印证                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  输出：完整 Agent Skill             │
│  • SKILL.md (Claude 原生支持)      │
│  • method.md (方法论文档)          │
│  • corpus/ (语料库)                │
│  • fund_data/ (基金数据)           │
│  • scripts/ (交互脚本)             │
└─────────────────────────────────────┘
```

## 💡 使用示例

### 示例1：完整蒸馏郑希

```bash
python main.py --manager "郑希" --fund-house "易方达" --verbose
```

输出：
```
✅ 已获取 24 份季度报告 (2012-2026)
✅ 已获取 18 篇基金经理手记
✅ 已获取 45 篇媒体报道
✅ 已提取 156 个核心观点
✅ 已蒸馏 8 条方法论框架
✅ 已分析 8 只基金持仓数据
✅ 已生成 6 维评分卡
✅ Agent Skill 已生成至 output/郑希/
```

### 示例2：批量蒸馏多个经理

创建 `managers.txt`：
```
郑希,易方达
葛兰,中欧基金
张坤,易方达
杨东,中金基金
```

运行：
```bash
python main.py --manager-list managers.txt --parallel
```

### 示例3：自定义参数蒸馏

```python
from core.distiller import FundManagerDistiller
from core.config import DistillerConfig

config = DistillerConfig(
    manager_name="葛兰",
    fund_house="中欧基金",
    start_year=2015,
    end_year=2026,
    data_sources=["efund", "ttjj", "media"],
    ai_extraction=True,
    output_format="skill",
    include_charts=True
)

distiller = FundManagerDistiller(config)
result = distiller.run()
result.save_to_disk()
```

## ⚖️ 约束与声明

✅ **可以做的**：
- 基于公开数据蒸馏投资方法
- 溯源问答与观点验证
- 持仓特征分析与对标

❌ **不能做的**：
- 编造经理人没说过的话
- 预测涨跌或给投资建议
- 侵犯隐私或商业秘密

⚠️ **免责声明**：
- 仅供研究学习使用
- 非投资建议
- 数据可能存在延迟

## 📝 License

MIT License - 开放使用和修改

## 🔗 相关资源

- [zhengxi-views](https://github.com/lyra81604/zhengxi-views) - 原型项目
- [Agent Skill 规范](https://claude.ai/docs/skills) - Claude 官方文档
- [基金数据 API](https://www.ttjj.com/api) - 天天基金 API

---

**有问题？** 提交 Issue 或 Discussion
