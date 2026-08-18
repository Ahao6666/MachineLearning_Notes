#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pandas 数据处理入门练习脚本（pandas_demo.py）

本脚本演示 Pandas 的核心功能，包括数据读取、查看、筛选、分组、
新增列、处理缺失值、合并数据等操作。

学习目标：
  1. 理解 DataFrame 和 Series 的概念
  2. 掌握数据查看与探索的方法
  3. 掌握条件筛选与布尔索引
  4. 掌握分组统计与聚合
  5. 学会处理缺失值和新增列

运行方式：python3 pandas_demo.py
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================================
# 第一部分：创建与读取数据
# ============================================================================
print("=" * 60)
print("📂 第一部分：创建与读取数据")
print("=" * 60)

# ---------------------------------------------------------------------------
# 1.1 创建 Series（一列数据）
# ---------------------------------------------------------------------------
print("\n--- 1.1 创建 Series（一列数据）---")

# Series = 带标签的一维数组，类似 Excel 中的一列
scores = pd.Series([85, 92, 78, 90, 88], name="考试成绩")
print("Series:")
print(scores)
print(f"  类型: {type(scores)}")
print(f"  平均值: {scores.mean():.1f}")
print(f"  最大值: {scores.max()}")

# 可以自定义索引（行名）
scores_with_index = pd.Series(
    [85, 92, 78, 90, 88],
    index=["张三", "李四", "王五", "赵六", "钱七"],
    name="考试成绩"
)
print("\n带索引的 Series:")
print(scores_with_index)
print(f"  张三的成绩: {scores_with_index['张三']}")


# ---------------------------------------------------------------------------
# 1.2 创建 DataFrame（一个表格）
# ---------------------------------------------------------------------------
print("\n--- 1.2 创建 DataFrame（一个表格）---")

# DataFrame = 多个 Series 组成的表格，类似 Excel 工作表
df_manual = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [20, 21, 19, 22],
    "成绩": [85, 92, 78, 90],
    "城市": ["北京", "上海", "广州", "深圳"],
})
print("手动创建的 DataFrame:")
print(df_manual)
print(f"  形状: {df_manual.shape}")  # (行数, 列数)
print(f"  列名: {list(df_manual.columns)}")


# ---------------------------------------------------------------------------
# 1.3 读取 CSV 文件（工作中最常用）
# ---------------------------------------------------------------------------
print("\n--- 1.3 读取 CSV 文件 ---")

CSV_FILE = Path(__file__).parent / "social_media_addiction_mental_wellbeing.csv"
df = pd.read_csv(CSV_FILE)
print(f"形状: {df.shape}")          # (1500, 30)  ← 1500 行 30 列
print(f"行数: {len(df)}")
print(f"列数: {len(df.columns)}")
print(f"列名:\n{list(df.columns)}")


# ============================================================================
# 第二部分：数据探索与查看
# ============================================================================
print("\n" + "=" * 60)
print("🔍 第二部分：数据探索与查看")
print("=" * 60)

# ---------------------------------------------------------------------------
# 2.1 查看数据概览
# ---------------------------------------------------------------------------
print("\n--- 2.1 查看数据概览 ---")

print("【前 3 行】")                # head() 看前几行
print(df.head(3).to_string(index=False))  # to_string() 美化打印

print("\n【后 3 行】")              # tail() 看后几行
print(df.tail(3).to_string(index=False))

print("\n【基本信息】")              # info() 显示列名、类型、非空数
df.info()

print("\n【统计概览】")              # describe() 数值列的统计量
print(df.describe().round(2))


# ---------------------------------------------------------------------------
# 2.2 访问列与行
# ---------------------------------------------------------------------------
print("\n--- 2.2 访问列与行 ---")

# 访问一列 → Series
ages = df["Age"]
print(f"年龄列（前 5 个）: {ages.head().values}")
print(f"年龄列类型: {type(ages)}")

# 访问多列 → DataFrame
subset = df[["User_ID", "Age", "Gender", "Addiction_Level"]]
print(f"\n多列（前 3 行）:")
print(subset.head(3).to_string(index=False))

# 访问行 → 用 iloc（索引位置）或 loc（标签名）
print(f"\n第 0 行（第一行）: {df.iloc[0]['User_ID']}")
print(f"第 0~2 行: {df.iloc[0:3]['User_ID'].values}")

# 同时筛选行和列
print(f"\n第 0~4 行的 User_ID 和 Age:")
print(df.loc[0:4, ["User_ID", "Age"]].to_string(index=False))


# ---------------------------------------------------------------------------
# 2.3 唯一值与计数
# ---------------------------------------------------------------------------
print("\n--- 2.3 唯一值与计数 ---")

print(f"成瘾级别分类: {df['Addiction_Level'].unique()}")    # 有哪些类别
print(f"成瘾级别数量: {df['Addiction_Level'].nunique()}")   # 几种类别
print(f"\n各级别人数:")
print(df["Addiction_Level"].value_counts())                 # 每个类别的人数

print(f"\n性别分布:")
print(df["Gender"].value_counts())


# ============================================================================
# 第三部分：数据筛选（布尔索引）
# ============================================================================
print("\n" + "=" * 60)
print("🎯 第三部分：数据筛选（布尔索引）")
print("=" * 60)

# ---------------------------------------------------------------------------
# 3.1 单条件筛选
# ---------------------------------------------------------------------------
print("\n--- 3.1 单条件筛选 ---")

# 筛选：年龄大于 30 岁的用户
mask_age = df["Age"] > 30
print(f"年龄 > 30 岁的条件（前 5 个）: {mask_age.head().values}")
print(f"年龄 > 30 岁的人数: {mask_age.sum()}")

# 取出满足条件的数据
senior_users = df[mask_age]
print(f"年龄 > 30 岁的用户（前 3 行）:")
print(senior_users[["User_ID", "Age"]].head(3).to_string(index=False))

# 一行写完（不用中间变量）
young_users = df[df["Age"] <= 20]
print(f"\n年龄 ≤ 20 岁的用户数: {len(young_users)}")


# ---------------------------------------------------------------------------
# 3.2 多条件筛选
# ---------------------------------------------------------------------------
print("\n--- 3.2 多条件筛选 ---")
#
# 注意：Pandas 中不能用 and/or，必须用 &（与）、|（或）、~（非）
# 每个条件必须用括号括起来

# 筛选：年龄 20-30 岁 且 每日使用时长 > 5 小时 的男性
mask = (df["Age"] >= 20) & (df["Age"] <= 30) & (df["Daily_Usage_Hours"] > 5) & (df["Gender"] == "Male")
result = df[mask]
print(f"符合条件的用户数: {len(result)}")
print(f"平均心理健康评分: {result['Mental_Wellbeing_Score'].mean():.2f}")

# or 的例子：成瘾级别为 High 或 Severe 的用户
heavy_users = df[(df["Addiction_Level"] == "High") | (df["Addiction_Level"] == "Severe")]
print(f"\nHigh 或 Severe 的用户数: {len(heavy_users)}")


# ---------------------------------------------------------------------------
# 3.3 isin() 筛选 —— 多个值取其一
# ---------------------------------------------------------------------------
print("\n--- 3.3 isin() 筛选 ---")

# 等价于上面的 | 写法，更简洁
heavy_users2 = df[df["Addiction_Level"].isin(["High", "Severe"])]
print(f"isin 写法 - High 或 Severe 的用户数: {len(heavy_users2)}")

# 筛选特定平台
platforms = ["Instagram", "TikTok"]
platform_users = df[df["Primary_Platform"].isin(platforms)]
print(f"{platforms} 用户数: {len(platform_users)}")


# ---------------------------------------------------------------------------
# 3.4 query() 方法 —— 更自然的写法
# ---------------------------------------------------------------------------
print("\n--- 3.4 query() 方法 ---")
#
# query() 可以用字符串写条件，不用加括号和 & 符号

result_q = df.query("20 <= Age <= 30 and Daily_Usage_Hours > 5 and Gender == 'Male'")
print(f"query 写法 - 符合条件的用户数: {len(result_q)}")
# ↑ 等价于上面的多条件筛选，但可读性更好


# ============================================================================
# 第四部分：分组统计
# ============================================================================
print("\n" + "=" * 60)
print("📊 第四部分：分组统计（groupby）")
print("=" * 60)

# ---------------------------------------------------------------------------
# 4.1 单列分组 + 单列聚合
# ---------------------------------------------------------------------------
print("\n--- 4.1 单列分组 + 单列聚合 ---")

# 按成瘾级别分组，计算平均心理健康评分
grouped = df.groupby("Addiction_Level")["Mental_Wellbeing_Score"].mean()
print("各成瘾级别的平均心理健康评分:")
print(grouped.round(2))

# 按性别分组，计算平均年龄
gender_age = df.groupby("Gender")["Age"].mean()
print("\n各性别的平均年龄:")
print(gender_age.round(1))


# ---------------------------------------------------------------------------
# 4.2 单列分组 + 多列聚合
# ---------------------------------------------------------------------------
print("\n--- 4.2 单列分组 + 多列聚合 ---")

# 按成瘾级别分组，同时计算多个指标的平均值
agg_cols = ["Daily_Usage_Hours", "Anxiety_Score", "Mental_Wellbeing_Score", "Sleep_Hours"]
summary = df.groupby("Addiction_Level")[agg_cols].mean()
print("各成瘾级别的多指标平均值:")
print(summary.round(2))


# ---------------------------------------------------------------------------
# 4.3 多列分组
# ---------------------------------------------------------------------------
print("\n--- 4.3 多列分组 ---")

# 按性别和成瘾级别双重分组，计算人数和平均心理健康评分
cross = df.groupby(["Gender", "Addiction_Level"]).agg(
    人数=("User_ID", "count"),
    平均心理健康=("Mental_Wellbeing_Score", "mean")
)
print("性别 × 成瘾级别 交叉分析:")
print(cross.round(2))


# ---------------------------------------------------------------------------
# 4.4 排序
# ---------------------------------------------------------------------------
print("\n--- 4.4 排序 ---")

# 按 Daily_Usage_Hours 降序排列，取前 5
top_usage = df.sort_values("Daily_Usage_Hours", ascending=False)
print("每日使用时长最长的前 5 名用户:")
print(top_usage[["User_ID", "Daily_Usage_Hours", "Addiction_Level"]].head(5).to_string(index=False))

# 按多列排序：先按成瘾级别，再按年龄
sorted_multi = df.sort_values(["Addiction_Level", "Age"], ascending=[True, False])
print("\n按成瘾级别 + 年龄排序（前 5）:")
print(sorted_multi[["User_ID", "Addiction_Level", "Age"]].head(5).to_string(index=False))


# ============================================================================
# 第五部分：新增列与数据处理
# ============================================================================
print("\n" + "=" * 60)
print("🛠 第五部分：新增列与数据处理")
print("=" * 60)

# ---------------------------------------------------------------------------
# 5.1 新增列（基于已有列计算）
# ---------------------------------------------------------------------------
print("\n--- 5.1 新增列 ---")

# 复制一份数据，避免修改原数据
df_copy = df.copy()

# 新增列：综合压力指数 = 焦虑×0.4 + 抑郁×0.3 + 孤独×0.3
df_copy["压力指数"] = (
    df_copy["Anxiety_Score"] * 0.4 +
    df_copy["Depression_Score"] * 0.3 +
    df_copy["Loneliness_Score"] * 0.3
)
print("前 5 名用户的压力指数:")
print(df_copy[["User_ID", "压力指数"]].head(5).to_string(index=False))

# 新增列：使用时长分类
def classify_usage(hours):
    """将使用时长分类"""
    if hours < 2:
        return "轻度使用"
    elif hours < 5:
        return "中度使用"
    else:
        return "重度使用"

# apply() 对每一行应用函数
df_copy["使用分类"] = df_copy["Daily_Usage_Hours"].apply(classify_usage)
print("\n使用时长分类统计:")
print(df_copy["使用分类"].value_counts())


# ---------------------------------------------------------------------------
# 5.2 处理缺失值
# ---------------------------------------------------------------------------
print("\n--- 5.2 处理缺失值 ---")

# 查看每列的缺失值数量
missing = df.isnull().sum()
print("各列缺失值数量（前 10 列）:")
print(missing[missing > 0].head(10))

# 缺失值比例
total = len(df)
missing_ratio = (missing / total * 100).round(2)
print(f"\n缺失比例（前 5 列）:")
print(missing_ratio[missing_ratio > 0].head(5))

# 填充缺失值（用平均值填充）
df_filled = df.copy()
cols_to_fill = ["Daily_Usage_Hours", "Anxiety_Score", "Mental_Wellbeing_Score"]
for col in cols_to_fill:
    mean_val = df_filled[col].mean()
    df_filled[col] = df_filled[col].fillna(mean_val)
    print(f"  {col}: 用平均值 {mean_val:.2f} 填充 {df[col].isnull().sum()} 个缺失值")


# ---------------------------------------------------------------------------
# 5.3 删除重复值
# ---------------------------------------------------------------------------
print("\n--- 5.3 删除重复值 ---")

# 检查 User_ID 是否有重复
print(f"总行数: {len(df)}")
print(f"唯一 User_ID 数: {df['User_ID'].nunique()}")
print(f"是否有重复行: {df.duplicated().any()}")


# ============================================================================
# 第六部分：综合实战 —— 数据分析管道
# ============================================================================
print("\n" + "=" * 60)
print("🚀 第六部分：综合实战 —— 数据分析管道")
print("=" * 60)


def analysis_pipeline():
    """
    用 Pandas 实现完整的数据分析管道。

    步骤：
      1. 读取数据
      2. 清洗数据（处理缺失值）
      3. 新增派生列
      4. 分组分析
      5. 输出结论
    """
    print("\n【步骤 1】读取数据...")
    data = pd.read_csv(CSV_FILE)
    print(f"  共 {len(data)} 条记录")

    print("\n【步骤 2】清洗数据...")
    # 用平均值填充数值列的缺失值
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    before = data[numeric_cols].isnull().sum().sum()
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
    after = data[numeric_cols].isnull().sum().sum()
    print(f"  填充了 {before} 个缺失值，剩余 {after} 个")

    print("\n【步骤 3】新增派生列...")
    # 压力指数
    data["压力指数"] = (
        data["Anxiety_Score"] * 0.4 +
        data["Depression_Score"] * 0.3 +
        data["Loneliness_Score"] * 0.3
    )
    # 使用分类
    data["使用分类"] = pd.cut(
        data["Daily_Usage_Hours"],
        bins=[0, 2, 5, 24],
        labels=["轻度", "中度", "重度"]
    )
    print("  已创建: 压力指数、使用分类")

    print("\n【步骤 4】分组分析...")
    # 按使用分类 × 成瘾级别 统计
    result = data.groupby(["使用分类", "Addiction_Level"], observed=False).agg(
        人数=("User_ID", "count"),
        平均年龄=("Age", "mean"),
        平均压力=("压力指数", "mean"),
        平均心理健康=("Mental_Wellbeing_Score", "mean"),
    ).round(2)

    print("交叉分析结果:")
    print(result.to_string())

    print("\n【步骤 5】分析结论...")
    # 重度使用者中 Severe 的比例
    heavy = data[data["使用分类"] == "重度"]
    severe_in_heavy = (heavy["Addiction_Level"] == "Severe").mean() * 100

    mild = data[data["使用分类"] == "轻度"]
    low_in_mild = (mild["Addiction_Level"] == "Low").mean() * 100

    print(f"  重度使用者中 Severe 比例: {severe_in_heavy:.1f}%")
    print(f"  轻度使用者中 Low 比例:    {low_in_mild:.1f}%")
    print(f"  💡 使用时长越长，成瘾程度越严重的趋势明显")


analysis_pipeline()


# ============================================================================
# 第七部分：Pandas 速查表
# ============================================================================
print("\n" + "=" * 60)
print("📖 Pandas 常用操作速查")
print("=" * 60)

cheatsheet = [
    ("读取 CSV", "pd.read_csv('file.csv')"),
    ("读取 Excel", "pd.read_excel('file.xlsx')"),
    ("查看数据", "df.head(10) / df.tail(5)"),
    ("基本信息", "df.info() / df.describe()"),
    ("形状", "df.shape"),
    ("列名", "df.columns"),
    ("选取列", "df['列名'] / df[['列1', '列2']]"),
    ("选取行", "df.iloc[0:5] / df.loc[0:5]"),
    ("条件筛选", "df[df['年龄'] > 30]"),
    ("多条件", "df[(条件1) & (条件2)]"),
    ("query筛选", "df.query('年龄 > 30 and 性别 == \"男\"')"),
    ("分组统计", "df.groupby('类别')['数值'].mean()"),
    ("多列聚合", "df.groupby('类别').agg({'分1': 'mean', '分2': 'sum'})"),
    ("排序", "df.sort_values('列名', ascending=False)"),
    ("新增列", "df['新列'] = df['列1'] + df['列2']"),
    ("apply", "df['列'].apply(函数)"),
    ("缺失值", "df.isnull().sum()"),
    ("填充缺失", "df.fillna(平均值)"),
    ("删除缺失", "df.dropna()"),
    ("唯一值", "df['列'].unique() / .nunique() / .value_counts()"),
    ("写入CSV", "df.to_csv('output.csv', index=False)"),
]

for i, (name, code) in enumerate(cheatsheet, 1):
    print(f"  {i:2d}. {name:<12} {code}")

print("\n" + "=" * 60)
print("✅ Pandas 练习脚本运行完毕！🚀")
print("=" * 60)
