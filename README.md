# 📊 Tableau 电商销售分析项目

一个完整的 Tableau 学习项目，包含真实业务场景数据、详细教程和最佳实践指南。适合 Tableau 初学者快速上手，制作专业的动态仪表盘。

[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 项目特色

- ✅ **真实业务场景**：电商销售数据，包含订单、客户、产品、目标等多维度信息
- ✅ **4个完整数据集**：50条销售记录、29个客户、51个产品、5个月销售目标
- ✅ **零基础友好**：从安装到发布的完整教程，一步步带您上手
- ✅ **最佳实践指南**：包含数据连接、图表制作、仪表盘设计、交互设置等
- ✅ **可扩展性强**：提供 Python 脚本生成更多样本数据

---

## 📁 项目结构

```
Tableau/
├── data/                           # 📊 数据文件
│   ├── sales_data.csv             # 销售交易数据（50条记录）
│   ├── customer_info.csv          # 客户主数据（29个客户）
│   ├── product_catalog.csv        # 产品目录（51个产品）
│   ├── targets.csv                # 月度销售目标
│   └── sample_data.csv            # 初始示例数据
│
├── scripts/                        # 🐍 数据处理脚本（可选）
│   ├── data_preparation.py        # 数据清洗和准备
│   ├── generate_extended_data.py  # 生成扩展数据
│   └── requirements.txt           # Python 依赖
│
├── workbooks/                      # 💼 Tableau 工作簿（您创建的）
│   └── README.md                  # 工作簿说明
│
├── exports/                        # 📤 导出的图表和报告
│   └── README.md                  # 导出文件说明
│
├── README.md                       # 📖 项目说明（本文件）
├── DASHBOARD_GUIDE.md             # 📚 详细技术指南
├── 快速入门指南.md                # 🚀 分步操作教程
├── 项目进度记录.md                # 📝 学习进度跟踪
└── .gitignore                     # ⚙️ Git 配置
```

---

## 🚀 快速开始

### 前置要求

1. **安装 Tableau**（选择其一）
   - [Tableau Public](https://public.tableau.com/app/discover)（免费，功能完整）
   - [Tableau Desktop](https://www.tableau.com/products/trial)（14天免费试用）

2. **可选：Python 环境**（仅用于数据预处理）
   ```bash
   python --version  # Python 3.x
   ```

### 第一步：克隆或下载项目

```bash
git clone https://github.com/Jamie0807/Tableau.git
cd Tableau
```

### 第二步：开始学习

#### 🎓 方式 1：跟随快速入门指南（推荐新手）

1. 打开 `快速入门指南.md`
2. 按照步骤一步步操作
3. 30分钟完成第一个仪表盘

#### 📚 方式 2：查看详细技术指南

1. 打开 `DASHBOARD_GUIDE.md`
2. 深入了解 Tableau 功能和最佳实践
3. 学习高级技巧和优化方法

### 第三步：在 Tableau 中操作

1. **打开 Tableau Desktop/Public**

2. **连接数据**
   - 点击 "文本文件"
   - 选择 `data/sales_data.csv`
   - 查看数据预览

3. **创建您的第一个图表**
   - 拖动 "订单日期" 到列
   - 拖动 "销售额" 到行
   - 🎉 折线图自动生成！

4. **保存工作**
   - 文件 → 保存
   - 保存到 `workbooks/` 文件夹

---

## 📊 数据集说明

### 1. sales_data.csv - 销售数据（核心）
- **50条交易记录**，时间跨度：2024年1-5月
- **字段**：订单ID、订单日期、客户ID、客户类型、地区、省份、城市、产品名称、产品类别、子类别、销售额、数量、折扣、利润、运输方式

### 2. customer_info.csv - 客户信息
- **29个客户档案**
- **字段**：客户ID、客户名称、客户类型（企业/个人）、注册日期、信用等级、年度预算、联系方式

### 3. product_catalog.csv - 产品目录
- **51个产品**，涵盖电子产品和办公用品两大类
- **字段**：产品ID、产品名称、类别、子类别、单价、成本、供应商、库存量、安全库存、上架日期

### 4. targets.csv - 销售目标
- **按月度、地区、类别设定的 KPI 目标**
- **字段**：月份、地区、产品类别、销售目标、利润目标

---

## 🎨 推荐的仪表盘

### 1️⃣ 销售总览仪表盘
- 📈 月度销售趋势线图
- 📊 各地区销售对比柱状图
- 🥧 产品类别占比饼图
- 📋 关键指标卡片（总销售额、总利润、利润率）

### 2️⃣ 产品分析仪表盘
- 🏆 Top 10 产品排行
- 💰 利润率散点图
- 📦 库存预警表格
- 💸 折扣影响分析

### 3️⃣ 客户分析仪表盘
- 👥 客户细分（企业 vs 个人）
- 💎 客户价值分层
- 🏆 Top 客户贡献
- 📈 客户增长趋势

### 4️⃣ 运营分析仪表盘
- 🚚 运输方式分析
- 🎯 目标达成情况（实际 vs 目标）
- ⏱️ 时间模式分析
- 📉 异常订单识别

---

## 💡 学习路径

### 第1天：基础入门
- [ ] 安装 Tableau
- [ ] 连接数据源
- [ ] 创建第一个图表
- [ ] 了解维度和度量

### 第2-3天：图表制作
- [ ] 创建 5 种基础图表
- [ ] 添加筛选器和颜色
- [ ] 设置标签和格式
- [ ] 排序和计算

### 第4-5天：仪表盘设计
- [ ] 组合多个图表
- [ ] 调整布局
- [ ] 添加交互功能
- [ ] 美化设计

### 第6-7天：高级功能
- [ ] 创建计算字段
- [ ] 使用参数控件
- [ ] 数据混合
- [ ] 表计算

### 持续实践
- [ ] 完成 4 个推荐仪表盘
- [ ] 使用真实数据练习
- [ ] 发布到 Tableau Public
- [ ] 获取社区反馈

---

## 🛠️ 可选：使用 Python 脚本

如果您想用 Python 预处理数据或生成更多样本：

### 安装依赖
```bash
cd scripts
pip install -r requirements.txt
```

### 运行数据清洗脚本
```bash
python data_preparation.py
```

### 生成扩展数据集
```bash
python generate_extended_data.py
```

---

## 📚 文档索引

| 文档 | 用途 | 适合人群 |
|------|------|---------|
| `README.md` | 项目总览和快速开始 | 所有人 |
| `快速入门指南.md` | 一步步操作教程 | 完全新手 |
| `DASHBOARD_GUIDE.md` | 详细技术指南和最佳实践 | 进阶学习 |
| `项目进度记录.md` | 学习进度跟踪 | 自我管理 |

---

## ❓ 常见问题

### Q1: 我是完全新手，从哪里开始？
**A:** 按顺序阅读：
1. 本 README（了解项目）
2. `快速入门指南.md`（动手操作）
3. `DASHBOARD_GUIDE.md`（深入学习）

### Q2: 需要编程基础吗？
**A:** 不需要！Tableau 是拖拽式操作，零代码。Python 脚本完全可选。

### Q3: 数据可以商用吗？
**A:** 本项目数据是模拟生成的示例数据，仅供学习使用。

### Q4: Tableau Public 和 Desktop 有什么区别？
**A:** 
- **Tableau Public**：免费，但所有作品必须公开发布
- **Tableau Desktop**：付费，可以保存到本地，功能更全

### Q5: 如何保存我的工作？
**A:** 
- 文件 → 保存
- 选择 `workbooks/` 文件夹
- 文件格式：`.twb`（不含数据）或 `.twbx`（含数据）

### Q6: 可以用自己的数据吗？
**A:** 当然可以！准备 CSV/Excel 格式的数据，放入 `data/` 文件夹即可。

---

## 🎯 项目目标

通过本项目，您将学会：

- ✅ Tableau 基本操作和界面
- ✅ 数据连接和准备
- ✅ 10+ 种常用图表制作
- ✅ 创建交互式仪表盘
- ✅ 数据分析最佳实践
- ✅ 可视化设计原则
- ✅ 发布和分享作品

---

## 🤝 贡献

欢迎提出建议和改进！

- 📧 提交 Issue
- 🔧 发起 Pull Request
- 💬 分享您的仪表盘作品

---

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 🔗 相关资源

### 官方资源
- [Tableau 官网](https://www.tableau.com/)
- [Tableau 学习中心](https://www.tableau.com/learn/training)
- [Tableau 社区](https://community.tableau.com/)
- [Tableau Public 作品库](https://public.tableau.com/gallery)

### 推荐学习
- [Tableau 官方 YouTube 频道](https://www.youtube.com/user/tableausoftware)
- [Tableau eLearning（免费）](https://elearning.tableau.com/)
- [Tableau 认证考试](https://www.tableau.com/learn/certification)

---

## ⭐ 如果这个项目对您有帮助，请给个 Star！

**祝您学习愉快，成为 Tableau 高手！** 🚀📊✨

---

*最后更新：2025年11月20日*
