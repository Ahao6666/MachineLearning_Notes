#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NumPy 数据处理入门练习脚本（numpy_demo.py）

本脚本演示如何使用 NumPy （Numerical Python）处理结构化数据，
并与纯 Python 写法进行对比，帮助理解 NumPy 的优势。

学习目标：
  1. 理解 NumPy 数组（ndarray）与 Python 列表的区别
  2. 掌握布尔索引（Boolean Indexing）筛选数据
  3. 掌握向量化运算（避免手写循环）
  4. 掌握常用的统计函数
  5. 对比 NumPy 与纯 Python 的代码风格和性能

运行方式：python3 numpy_demo.py
"""

import numpy as np
import time
from pathlib import Path

# ============================================================================
# 第一部分：NumPy 基础入门
# ============================================================================
print("=" * 60)
print("🧮 第一部分：NumPy 基础入门")
print("=" * 60)

# ---------------------------------------------------------------------------
# 1.1 创建 NumPy 数组
# ---------------------------------------------------------------------------
print("\n--- 1.1 创建 NumPy 数组 ---")

# 从列表创建
py_list = [1, 2, 3, 4, 5]
np_array = np.array(py_list)
print(f"Python 列表: {py_list}")
print(f"NumPy 数组:  {np_array}")
print(f"数组类型:    {type(np_array)}")
print(f"数据类型:    {np_array.dtype}")  # int64（64位整数）
print(f"数组形状:    {np_array.shape}")  # (5,) — 一维，5个元素
print(f"维度:        {np_array.ndim}")   # 1

# 二维数组（矩阵）
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n二维数组:\n{matrix}")
print(f"形状: {matrix.shape}")   # (2, 3) — 2行3列
print(f"维度: {matrix.ndim}")    # 2

# 特殊数组
print(f"\n全零数组:\n{np.zeros((2, 3))}")
print(f"\n全一数组:\n{np.ones((2, 3))}")
print(f"\n单位矩阵:\n{np.eye(3)}")
print(f"\n等间隔数组:\n{np.arange(0, 10, 2)}")    # 类似 range()
print(f"\n均匀分布:\n{np.linspace(0, 1, 5)}")     # 0~1 等分5份


# ---------------------------------------------------------------------------
# 1.2 数组与列表的关键区别
# ---------------------------------------------------------------------------
print("\n--- 1.2 数组与列表的关键区别 ---")

# 区别 ①：NumPy 数组的所有元素类型必须相同
mixed_list = [1, "hello", 3.14]
mixed_array = np.array(mixed_list)
print(f"Python 列表可以混类型: {mixed_list}")
print(f"NumPy 数组自动统一类型: {mixed_array}")   # 都变成字符串
print(f"数据类型: {mixed_array.dtype}")            # <U5（字符串）

# 区别 ②：运算方式不同
py_list = [1, 2, 3]
print(f"\nPython 列表 [1,2,3] + [4,5,6] = {py_list + [4, 5, 6]}")  # 拼接
print(f"NumPy 数组 [1,2,3] + [4,5,6] = {np.array(py_list) + np.array([4,5,6])}")  # 对应相加

# 区别 ③：NumPy 支持广播（Broadcasting）
print(f"\n广播: [1,2,3] * 10 = {np.array([1, 2, 3]) * 10}")  # 每个元素乘以10


# ---------------------------------------------------------------------------
# 1.3 向量化运算（对比手写循环）
# ---------------------------------------------------------------------------
print("\n--- 1.3 向量化运算（对比手写循环）---")

scores = [85, 92, 78, 90, 88]

# Python 写法：手写循环
scores_py = []
for s in scores:
    scores_py.append(s * 1.1 + 5)
print(f"Python 循环: {scores_py}")

# NumPy 写法：向量化（一行搞定，不用循环）
scores_np = np.array(scores) * 1.1 + 5
print(f"NumPy 向量化: {scores_np}")
#
# 关键理解：NumPy 的运算会"自动"应用到每个元素，
#           不用写 for 循环，代码更简洁、速度更快。
#


# ============================================================================
# 第二部分：用 NumPy 读取和探索 CSV 数据
# ============================================================================
print("\n" + "=" * 60)
print("📂 第二部分：用 NumPy 读取 CSV 数据")
print("=" * 60)

CSV_FILE = Path(__file__).parent / "social_media_addiction_mental_wellbeing.csv"

# ---------------------------------------------------------------------------
# 2.1 读取 CSV——genfromtxt
# ---------------------------------------------------------------------------
print("\n--- 2.1 读取 CSV 文件 ---")
#
# np.genfromtxt 是 NumPy 读取 CSV 的常用函数。
# 参数说明：
#   delimiter=","   → 逗号分隔
#   dtype=None      → 自动推断数据类型
#   encoding="utf-8"→ 支持中文
#   names=True      → 第一行作为列名
#   missing_values  → 指定哪些值算"缺失"
#   filling_values  → 缺失值填充为 0

data = np.genfromtxt(
    CSV_FILE,
    delimiter=",",
    dtype=None,
    encoding="utf-8",
    names=True,
    missing_values=["", " "],
    filling_values=0
)

print(f"数据类型: {type(data)}")
print(f"形状:     {data.shape}")     # (行数, 列数)
print(f"列名:     {data.dtype.names}")
print(f"列数:     {len(data.dtype.names)}")


# ---------------------------------------------------------------------------
# 2.2 通过列名访问数据
# ---------------------------------------------------------------------------
print("\n--- 2.2 通过列名访问数据 ---")
#
# 因为用了 names=True，可以通过 data["列名"] 直接访问某一列。

ages = data["Age"]
print(f"年龄列（前10个）: {ages[:10]}")
print(f"数据类型:          {ages.dtype}")
print(f"形状:              {ages.shape}")

# 数值列会自动转为浮点数
wellbeing = data["Mental_Wellbeing_Score"]
print(f"\n心理健康评分（前10个）: {wellbeing[:10]}")
print(f"数据类型: {wellbeing.dtype}")

# 字符串列会自动转为字符串
platforms = data["Primary_Platform"]
print(f"\n主要平台（前10个）: {platforms[:10]}")
print(f"数据类型: {platforms.dtype}")


# ---------------------------------------------------------------------------
# 2.3 快速统计概览
# ---------------------------------------------------------------------------
print("\n--- 2.3 快速统计概览 ---")

# 数值列的基本统计量
numeric_cols = [
    "Age", "Daily_Usage_Hours", "Notifications_Per_Day",
    "Anxiety_Score", "Depression_Score", "Mental_Wellbeing_Score"
]

print(f"{'列名':<25} {'最小值':<8} {'最大值':<8} {'平均值':<8} {'标准差':<8} {'缺失数':<8}")
print("-" * 65)
for col in numeric_cols:
    col_data = data[col]
    # 判断哪些是有效值（非 NaN）
    valid = col_data[~np.isnan(col_data.astype(float))]
    if len(valid) > 0:
        min_val = np.min(valid)
        max_val = np.max(valid)
        mean_val = np.mean(valid)
        std_val = np.std(valid)
        # NaN 的数量
        nan_count = np.sum(np.isnan(col_data.astype(float)))
        print(f"{col:<25} {min_val:<8.2f} {max_val:<8.2f} {mean_val:<8.2f} {std_val:<8.2f} {int(nan_count):<8}")


# ============================================================================
# 第三部分：NumPy 筛选与分类
# ============================================================================
print("\n" + "=" * 60)
print("🔍 第三部分：NumPy 筛选与分类（对比纯 Python）")
print("=" * 60)

# ---------------------------------------------------------------------------
# 3.1 布尔索引（Boolean Indexing）—— NumPy 最强大的功能之一
# ---------------------------------------------------------------------------
print("\n--- 3.1 布尔索引 — 按条件筛选 ---")
#
# 布尔索引 = 用一个 True/False 数组来选取数据。
# data[条件] 会自动选出条件为 True 的行。
#

# 示例：筛选出心理健康评分 > 8 的用户
print("【例1】心理健康评分 > 8 的用户")

# Python 写法
py_start = time.perf_counter()
# （这里只演示概念，不实际运行完整 Python 版本）

# NumPy 写法（一行搞定！）
mask = data["Mental_Wellbeing_Score"] > 8  # 返回布尔数组
print(f"  条件数组（前10个）: {mask[:10]}")
print(f"  满足条件的人数: {np.sum(mask)}")  # True=1, False=0, 求和即计数

# 用布尔索引取出满足条件的数据
high_wellbeing = data[mask]
print(f"  筛选后形状: {high_wellbeing.shape}")
print(f"  前3个用户ID: {high_wellbeing['User_ID'][:3]}")
print(f"  前3个心理健康评分: {high_wellbeing['Mental_Wellbeing_Score'][:3]}")

# 多条件组合：&（与）、|（或）、~（非）
print("\n【例2】多条件组合：年龄 20-30 且每日使用时长 > 5 小时")
mask2 = (data["Age"] >= 20) & (data["Age"] <= 30) & (data["Daily_Usage_Hours"] > 5)
print(f"  满足条件人数: {np.sum(mask2)}")

# 选出满足条件的用户 ID 和评分
filtered = data[mask2]
print(f"  前5个用户ID: {filtered['User_ID'][:5]}")
print(f"  平均心理健康评分: {np.mean(filtered['Mental_Wellbeing_Score']):.2f}")


# ---------------------------------------------------------------------------
# 3.2 按类别分组统计 —— 对比两种写法
# ---------------------------------------------------------------------------
print("\n--- 3.2 按类别分组统计（对比纯 Python vs NumPy）---")
#
# 需求：按 Addiction_Level 分组，计算每组平均 Anxiety_Score
#

# 获取所有不同的成瘾级别
levels = np.unique(data["Addiction_Level"])
print(f"成瘾级别: {levels}")

# ---------- 写法 A：纯 Python（手写循环） ----------
print("\n【写法 A】纯 Python 手写分组:")
py_start = time.perf_counter()

py_result = {}
for level in levels:
    scores = []
    for row in data:  # 遍历每一行
        if row["Addiction_Level"] == level:
            try:
                scores.append(float(row["Anxiety_Score"]))
            except (ValueError, TypeError):
                pass
    if scores:
        py_result[level] = round(sum(scores) / len(scores), 2)

py_time = time.perf_counter() - py_start
for level in levels:
    print(f"  {level}: {py_result.get(level, 'N/A')}")

# ---------- 写法 B：NumPy 布尔索引 ----------
print("\n【写法 B】NumPy 布尔索引（一行一个分组）:")
np_start = time.perf_counter()

np_result = {}
for level in levels:
    mask_level = data["Addiction_Level"] == level       # 布尔索引
    scores_level = data["Anxiety_Score"][mask_level]     # 取出该组数据
    valid = scores_level[~np.isnan(scores_level)]        # 去掉 NaN
    if len(valid) > 0:
        np_result[level] = round(np.mean(valid), 2)

np_time = time.perf_counter() - np_start
for level in levels:
    print(f"  {level}: {np_result.get(level, 'N/A')}")

# 速度对比
print(f"\n⏱ 速度对比:")
print(f"  纯 Python: {py_time:.6f} 秒")
print(f"  NumPy:     {np_time:.6f} 秒")
print(f"  加速比:    {py_time / np_time:.1f}x")


# ---------------------------------------------------------------------------
# 3.3 向量化运算实战
# ---------------------------------------------------------------------------
print("\n--- 3.3 向量化运算实战 ---")
#
# 需求：计算"综合压力指数" = 焦虑评分×0.4 + 抑郁评分×0.3 + 孤独感评分×0.3
#

print("【计算综合压力指数】")

# Python 写法：手写循环
def calc_stress_python(data):
    """纯 Python 循环计算"""
    result = []
    for row in data:
        try:
            anxiety = float(row["Anxiety_Score"])
            depression = float(row["Depression_Score"])
            loneliness = float(row["Loneliness_Score"])
            stress = anxiety * 0.4 + depression * 0.3 + loneliness * 0.3
            result.append(round(stress, 2))
        except (ValueError, TypeError):
            result.append(None)
    return result

# NumPy 写法：向量化（不用循环！）
def calc_stress_numpy(data):
    """NumPy 向量化计算"""
    anxiety = data["Anxiety_Score"].astype(float)
    depression = data["Depression_Score"].astype(float)
    loneliness = data["Loneliness_Score"].astype(float)
    # 向量化运算 — 直接对数组做数学运算
    stress = anxiety * 0.4 + depression * 0.3 + loneliness * 0.3
    return np.round(stress, 2)

stress_np = calc_stress_numpy(data)
print(f"  前10个用户的综合压力指数: {stress_np[:10]}")
print(f"  平均压力指数: {np.mean(stress_np[~np.isnan(stress_np)]):.2f}")
print(f"  最高压力指数: {np.nanmax(stress_np):.2f}")
print(f"  最低压力指数: {np.nanmin(stress_np):.2f}")

# 按成瘾级别分析平均压力指数
print("\n【按成瘾级别分析平均压力指数】")
for level in levels:
    mask_level = data["Addiction_Level"] == level
    level_stress = stress_np[mask_level]
    valid = level_stress[~np.isnan(level_stress)]
    if len(valid) > 0:
        print(f"  {level}: {np.mean(valid):.2f}（共 {len(valid)} 人）")


# ---------------------------------------------------------------------------
# 3.4 高级筛选：按百分比分段
# ---------------------------------------------------------------------------
print("\n--- 3.4 高级筛选：按百分比分段 ---")
#
# 需求：找出每日使用时长最长的前 10% 的用户

usage = data["Daily_Usage_Hours"].astype(float)
# 计算第 90 百分位数
threshold = np.percentile(usage[~np.isnan(usage)], 90)
print(f"前 10% 阈值（每日使用时长 > {threshold:.1f} 小时）")

# 布尔索引筛选
top_10_mask = usage > threshold
top_users = data[top_10_mask]
print(f"前 10% 用户数: {np.sum(top_10_mask)}")

# 分析这些重度用户的特征
print(f"  平均年龄: {np.mean(top_users['Age']):.1f}")
print(f"  平均焦虑评分: {np.mean(top_users['Anxiety_Score']):.2f}")
print(f"  平均心理健康评分: {np.mean(top_users['Mental_Wellbeing_Score']):.2f}")

# 对比：后 10% 用户
threshold1 = np.percentile(usage[~np.isnan(usage)], 10)
print(f"\n后 10% 阈值（每日使用时长 < {threshold1:.1f} 小时）")
bottom_10_mask = usage < threshold1
bottom_users = data[bottom_10_mask]
print(f"后 10% 用户数: {np.sum(bottom_10_mask)}")
print(f"  平均年龄: {np.mean(bottom_users['Age']):.1f}")
print(f"  平均焦虑评分: {np.mean(bottom_users['Anxiety_Score']):.2f}")
print(f"  平均心理健康评分: {np.mean(bottom_users['Mental_Wellbeing_Score']):.2f}")


# ---------------------------------------------------------------------------
# 3.5 相关性分析
# ---------------------------------------------------------------------------
print("\n--- 3.5 相关性分析 ---")
#
# np.corrcoef 计算相关系数矩阵
# 数值范围 -1 ~ 1：
#   1        → 完全正相关（同增同减）
#   0        → 无相关性
#   -1       → 完全负相关（一增一减）

print("【各指标与心理健康评分的相关性】")
target = "Mental_Wellbeing_Score"
features = [
    "Daily_Usage_Hours", "Notifications_Per_Day",
    "Anxiety_Score", "Depression_Score",
    "Sleep_Hours", "FOMO_Score"
]

# 提取数据，处理缺失值
n = len(data)
wellbeing_col = data[target].astype(float)

print(f"{'指标':<25} {'相关系数':<10} {'相关强度'}")
print("-" * 50)
for feat in features:
    feat_col = data[feat].astype(float)
    # 去掉任一列为 NaN 的行
    valid_mask = ~np.isnan(wellbeing_col) & ~np.isnan(feat_col)
    wb = wellbeing_col[valid_mask]
    ft = feat_col[valid_mask]
    if len(wb) > 2:
        corr = np.corrcoef(wb, ft)[0, 1]
        # 判断相关强度
        if abs(corr) >= 0.5:
            strength = "强相关"
        elif abs(corr) >= 0.3:
            strength = "中等相关"
        elif abs(corr) >= 0.1:
            strength = "弱相关"
        else:
            strength = "几乎无关"
        print(f"{feat:<25} {corr:<+10.4f} {strength}")


# ============================================================================
# 第四部分：综合实战 — NumPy 完整分析管道
# ============================================================================
print("\n" + "=" * 60)
print("🚀 第四部分：综合实战 — NumPy 完整分析管道")
print("=" * 60)


def numpy_analysis_pipeline():
    """
    用 NumPy 实现完整的数据分析管道。

    步骤：
      1. 读取数据
      2. 数据清洗（处理缺失值）
      3. 创建新特征（综合压力指数）
      4. 分组统计
      5. 输出结论
    """
    print("\n【步骤 1】读取数据...")
    raw = np.genfromtxt(
        CSV_FILE, delimiter=",", dtype=None,
        encoding="utf-8", names=True,
        missing_values=["", " "], filling_values=np.nan
    )
    print(f"  共 {len(raw)} 条记录")

    print("\n【步骤 2】数据清洗 — 处理缺失值...")
    # 统计每列的缺失情况
    for col in raw.dtype.names:
        col_data = raw[col]
        # 尝试转数值
        try:
            numeric = col_data.astype(float)
            nan_count = np.sum(np.isnan(numeric))
            if nan_count > 0:
                print(f"  {col}: {nan_count} 个缺失值（已自动填充为 NaN）")
        except (ValueError, TypeError):
            pass  # 字符串列跳过

    print("\n【步骤 3】创建新特征：压力指数分组...")
    anxiety = raw["Anxiety_Score"].astype(float)
    depression = raw["Depression_Score"].astype(float)
    loneliness = raw["Loneliness_Score"].astype(float)
    stress_index = anxiety * 0.4 + depression * 0.3 + loneliness * 0.3

    # 按压力指数分组
    low_stress = stress_index < 3
    mid_stress = (stress_index >= 3) & (stress_index < 6)
    high_stress = stress_index >= 6

    print(f"  低压组 (<3):   {np.nansum(low_stress):>4} 人")
    print(f"  中压组 (3~6):  {np.nansum(mid_stress):>4} 人")
    print(f"  高压组 (≥6):   {np.nansum(high_stress):>4} 人")

    print("\n【步骤 4】交叉分析：压力组 × 成瘾级别...")
    stress_groups = [
        ("低压", low_stress),
        ("中压", mid_stress),
        ("高压", high_stress),
    ]
    # 表头
    print(f"{'':<10}", end="")
    for lv in levels:
        print(f"{lv:<10}", end="")
    print()
    print("-" * (10 + 10 * len(levels)))

    for sg_name, sg_mask in stress_groups:
        print(f"{sg_name:<10}", end="")
        for lv in levels:
            # 同时满足压力组和成瘾级别的条件
            count = np.sum(sg_mask & (raw["Addiction_Level"] == lv))
            print(f"{count:<10}", end="")
        print()

    print("\n【步骤 5】结论...")
    high_stress_severe = np.sum(high_stress & (raw["Addiction_Level"] == "Severe"))
    low_stress_low = np.sum(low_stress & (raw["Addiction_Level"] == "Low"))
    print(f"  高压组中 Severe 的人数: {high_stress_severe}")
    print(f"  低压组中 Low 的人数:    {low_stress_low}")

    # 最有价值的发现
    if high_stress_severe > 0 and low_stress_low > 0:
        print(f"\n  💡 压力指数与成瘾级别有较强的关联性。")
        print(f"     说明心理健康干预可能有助于减少社交媒体成瘾风险。")


numpy_analysis_pipeline()


# ============================================================================
# 第五部分：NumPy 常用函数速查
# ============================================================================
print("\n" + "=" * 60)
print("📖 第五部分：NumPy 常用函数速查")
print("=" * 60)

cheatsheet = [
    ("创建数组", "np.array([1,2,3])"),
    ("全零数组", "np.zeros((3,4))"),
    ("等间隔", "np.arange(0, 10, 2)"),
    ("等分", "np.linspace(0, 1, 5)"),
    ("随机数", "np.random.randn(100)"),
    ("形状", "arr.shape"),
    ("重塑", "arr.reshape(2, 5)"),
    ("类型", "arr.dtype"),
    ("求和", "np.sum(arr)"),
    ("均值", "np.mean(arr)"),
    ("中位数", "np.median(arr)"),
    ("标准差", "np.std(arr)"),
    ("最大值", "np.max(arr) / np.nanmax(arr)"),
    ("最小值", "np.min(arr) / np.nanmin(arr)"),
    ("百分位数", "np.percentile(arr, 90)"),
    ("相关系数", "np.corrcoef(x, y)"),
    ("唯一值", "np.unique(arr)"),
    ("条件筛选", "arr[arr > 5]   (布尔索引)"),
    ("多条件", "arr[(a>1) & (b<5)]   (与 &, 或 |)"),
    ("数组运算", "arr * 2 + 1   (向量化)"),
    ("排序", "np.sort(arr)"),
    ("拼接", "np.concatenate([a, b])"),
]

for i, (name, code) in enumerate(cheatsheet, 1):
    print(f"  {i:2d}. {name:<12}  {code}")

print("\n" + "=" * 60)
print("✅ NumPy 练习脚本运行完毕！🚀")
print("=" * 60)
