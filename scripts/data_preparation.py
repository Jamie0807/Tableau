"""
数据准备和清洗脚本
用于预处理数据，为 Tableau 分析做准备
"""

import pandas as pd
import os

# 设置路径
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
INPUT_FILE = os.path.join(DATA_DIR, 'sample_data.csv')
OUTPUT_FILE = os.path.join(DATA_DIR, 'cleaned_data.csv')


def load_data(file_path):
    """加载数据文件"""
    try:
        df = pd.read_csv(file_path)
        print(f"成功加载数据: {len(df)} 行")
        return df
    except Exception as e:
        print(f"加载数据时出错: {e}")
        return None


def clean_data(df):
    """清洗数据"""
    # 删除重复行
    df = df.drop_duplicates()
    
    # 处理缺失值
    df = df.dropna()
    
    # 数据类型转换
    if '日期' in df.columns:
        df['日期'] = pd.to_datetime(df['日期'])
    
    print(f"清洗后数据: {len(df)} 行")
    return df


def add_calculated_fields(df):
    """添加计算字段"""
    # 示例: 计算单价
    if '销售额' in df.columns and '数量' in df.columns:
        df['单价'] = df['销售额'] / df['数量']
    
    # 示例: 添加年月字段
    if '日期' in df.columns:
        df['年'] = df['日期'].dt.year
        df['月'] = df['日期'].dt.month
        df['星期'] = df['日期'].dt.dayofweek + 1
    
    return df


def save_data(df, file_path):
    """保存处理后的数据"""
    try:
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"数据已保存到: {file_path}")
    except Exception as e:
        print(f"保存数据时出错: {e}")


def main():
    """主函数"""
    print("开始数据准备...")
    
    # 加载数据
    df = load_data(INPUT_FILE)
    if df is None:
        return
    
    # 清洗数据
    df = clean_data(df)
    
    # 添加计算字段
    df = add_calculated_fields(df)
    
    # 保存数据
    save_data(df, OUTPUT_FILE)
    
    print("数据准备完成!")


if __name__ == "__main__":
    main()
