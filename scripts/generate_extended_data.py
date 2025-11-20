"""
扩展数据生成脚本
生成更多样本数据用于Tableau仪表盘演示
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 设置随机种子以确保可重复性
random.seed(42)
np.random.seed(42)

# 基础数据配置
regions = {
    '华东': ['上海市', '杭州市', '南京市', '苏州市', '宁波市', '合肥市'],
    '华北': ['北京市', '天津市', '石家庄市'],
    '华南': ['广州市', '深圳市', '厦门市'],
    '西南': ['成都市', '重庆市'],
    '西北': ['西安市'],
    '东北': ['沈阳市']
}

products = {
    '电子产品': {
        '手机': [('智能手机X1', 4999, 3500), ('智能手机X2', 3999, 2800)],
        '电脑': [('笔记本电脑Pro', 8999, 6500), ('笔记本电脑Air', 5999, 4200)],
        '平板': [('平板电脑S2', 3299, 2200), ('平板电脑Mini', 2299, 1500)],
        '外设': [('游戏鼠标RGB', 399, 200), ('机械键盘青轴', 699, 400), ('网络摄像头HD', 459, 250)],
        '音频': [('无线耳机Pro', 899, 500), ('蓝牙音箱便携', 399, 220)]
    },
    '办公用品': {
        '家具': [('办公椅豪华版', 1299, 800), ('办公桌标准版', 2199, 1500), ('书架五层', 899, 550)],
        '耗材': [('打印纸A4', 89, 45), ('订书机套装', 45, 20), ('文件夹套装', 78, 38)]
    }
}

shipping_methods = ['标准配送', '次日达', '加急配送']
customer_types = ['企业客户', '个人客户']

def generate_sales_data(num_records=200, start_date='2024-01-01', end_date='2024-05-31'):
    """生成销售数据"""
    data = []
    order_id = 51
    customer_id = 1
    
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    for _ in range(num_records):
        # 生成随机日期
        days_diff = (end - start).days
        random_days = random.randint(0, days_diff)
        order_date = start + timedelta(days=random_days)
        
        # 选择地区和城市
        region = random.choice(list(regions.keys()))
        city = random.choice(regions[region])
        province = city.replace('市', '')
        
        # 选择产品
        category = random.choice(list(products.keys()))
        subcategory = random.choice(list(products[category].keys()))
        product_info = random.choice(products[category][subcategory])
        product_name, price, cost = product_info
        
        # 生成订单详情
        customer_type = random.choice(customer_types)
        quantity = random.randint(1, 10) if category == '办公用品' else random.randint(1, 3)
        discount = round(random.choice([0, 0.05, 0.1, 0.15, 0.2]), 2)
        
        sales = round(price * quantity * (1 - discount), 2)
        profit = round((price - cost) * quantity * (1 - discount) * random.uniform(0.7, 0.95), 2)
        
        shipping = random.choice(shipping_methods)
        
        data.append({
            '订单ID': f'ORD{order_id:03d}',
            '订单日期': order_date.strftime('%Y-%m-%d'),
            '客户ID': f'C{customer_id:03d}',
            '客户类型': customer_type,
            '地区': region,
            '省份': province,
            '城市': city,
            '产品名称': product_name,
            '产品类别': category,
            '子类别': subcategory,
            '销售额': sales,
            '数量': quantity,
            '折扣': discount,
            '利润': profit,
            '运输方式': shipping
        })
        
        order_id += 1
        customer_id = random.randint(1, 50)
    
    return pd.DataFrame(data)

def calculate_metrics(df):
    """计算关键指标"""
    metrics = {
        '总销售额': df['销售额'].sum(),
        '总利润': df['利润'].sum(),
        '总订单数': len(df),
        '平均订单价值': df['销售额'].mean(),
        '利润率': (df['利润'].sum() / df['销售额'].sum() * 100) if df['销售额'].sum() > 0 else 0,
        '平均折扣率': df['折扣'].mean() * 100
    }
    return metrics

def main():
    """主函数"""
    print("开始生成扩展数据...")
    
    # 生成更多销售数据
    df_extended = generate_sales_data(num_records=200)
    
    # 保存数据
    output_file = '../data/sales_data_extended.csv'
    df_extended.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"✓ 扩展数据已保存: {output_file}")
    print(f"  - 记录数: {len(df_extended)}")
    
    # 计算并显示关键指标
    metrics = calculate_metrics(df_extended)
    print("\n关键指标概览:")
    for key, value in metrics.items():
        if '率' in key:
            print(f"  - {key}: {value:.2f}%")
        elif '额' in key or '利润' in key:
            print(f"  - {key}: ¥{value:,.2f}")
        else:
            print(f"  - {key}: {value:,.2f}")
    
    print("\n数据生成完成!")

if __name__ == "__main__":
    main()
