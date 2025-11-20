# Tableau 项目

这是一个 Tableau 数据可视化项目。

## 项目结构

```
Tableau/
├── data/           # 数据源文件 (CSV, Excel, JSON等)
├── scripts/        # 数据处理和准备脚本
├── workbooks/      # Tableau工作簿文件 (.twb, .twbx)
├── exports/        # 导出的可视化图表和报告
└── README.md       # 项目说明文档
```

## 开始使用

### 1. 准备数据
将您的数据文件放在 `data/` 文件夹中。支持的格式包括：
- CSV
- Excel (.xlsx, .xls)
- JSON
- 数据库连接配置

### 2. 数据预处理
如果需要清洗或转换数据，可以在 `scripts/` 文件夹中创建Python脚本。

### 3. 创建可视化
使用 Tableau Desktop 打开或创建工作簿，并保存在 `workbooks/` 文件夹中。

### 4. 导出结果
将最终的可视化图表、仪表板或报告导出到 `exports/` 文件夹。

## 依赖项

- Tableau Desktop 或 Tableau Public
- Python 3.x (用于数据预处理，可选)
- pandas, numpy (如果使用Python脚本)

## 注意事项

- 不要将敏感数据提交到版本控制
- 考虑在 `.gitignore` 中排除大型数据文件
- 定期备份工作簿文件
