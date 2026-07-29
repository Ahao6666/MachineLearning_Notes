#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据分类处理综合练习脚本（classify_demo.py）

本脚本综合运用了前面三个脚本的知识点：
  - read_csv_demo.py  →  CSV 文件读取
  - list_dict_demo.py  →  列表与字典的创建、嵌套、遍历
  - loop_func_demo.py  →  循环遍历、函数封装、lambda 排序

功能：对社交媒体成瘾数据按不同维度进行分类统计，如：
  1. 按成瘾级别分组
  2. 按性别分组
  3. 按主要平台分组
  4. 多条件筛选与统计

适用人群：Python 初学者 / 希望看到综合运用的学习者。
运行方式：python3 classify_demo.py
"""

import csv
from pathlib import Path
from collections import defaultdict

# ============================================================================
# 第一步：读取 CSV 数据（复用 read_csv_demo.py 的思路）
# ============================================================================

CSV_FILE = Path(__file__).parent / "social_media_addiction_mental_wellbeing.csv"


def read_csv_to_dicts(path):
    """
    读取 CSV 文件，将每一行转换为字典（列名→值）。

    参数:
        path (str | Path): CSV 文件路径。

    返回:
        list[dict]: 列表嵌套字典，每个字典代表一条记录。

    对比 read_csv_demo.py：
      之前的 read_csv() 返回的是 [表头, [行列表]]，
      这里返回的是 [{列名: 值}, {列名: 值}, ...]，
      用字典访问更方便：row["Age"] 而不是 row[age_index]
    """
    records = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # ← csv.DictReader 直接把每行转成字典！
        for row in reader:
            records.append(row)
    return records


# ============================================================================
# 第二步：定义分类处理函数（运用 函数 + 循环 + 列表/字典）
# ============================================================================

# ---------------------------------------------------------------------------
# 分类 ①：按成瘾级别分组（Addiction_Level）
# ---------------------------------------------------------------------------
def group_by_addiction_level(records):
    """
    按成瘾级别对用户分组。

    参数:
        records (list[dict]): 用户数据列表。

    返回:
        dict: {成瘾级别: [用户列表]}，其中用户列表里每个用户是字典

    知识点：
      - 字典的键是成瘾级别（Low, Moderate, High, Severe）
      - 字典的值是列表，存放该级别的所有用户
      - 使用 defaultdict(list) 避免手动判断键是否存在
    """
    groups = defaultdict(list)
    for user in records:
        level = user["Addiction_Level"]
        groups[level].append(user)
    return dict(groups)  # 转回普通 dict 便于打印


# ---------------------------------------------------------------------------
# 分类 ②：按性别分组 + 统计平均心理健康评分
# ---------------------------------------------------------------------------
def group_by_gender_with_avg(records):
    """
    按性别分组，并统计每组平均心理健康评分。

    参数:
        records (list[dict]): 用户数据列表。

    返回:
        dict: {性别: {"count": 人数, "avg_wellbeing": 平均分}}

    知识点：
      - 字典的值可以是另一个字典（嵌套字典）
      - float() 转换字符串为数字，处理空值用 try/except
    """
    result = {}
    for user in records:
        gender = user["Gender"]
        if not gender:  # 跳过空值
            continue

        # 如果这个性别还没在 result 中，初始化
        if gender not in result:
            result[gender] = {"count": 0, "total_score": 0.0}

        result[gender]["count"] += 1

        # 尝试转换 Mental_Wellbeing_Score，空值则跳过
        try:
            score = float(user["Mental_Wellbeing_Score"])
            result[gender]["total_score"] += score
        except (ValueError, TypeError):
            pass

    # 计算平均分（循环遍历字典的 items()）
    for gender, data in result.items():
        if data["count"] > 0:
            data["avg_wellbeing"] = round(data["total_score"] / data["count"], 2)
        else:
            data["avg_wellbeing"] = 0.0
        del data["total_score"]  # 删除中间变量

    return result


# ---------------------------------------------------------------------------
# 分类 ③：按主要平台分组 + 统计人数并排序
# ---------------------------------------------------------------------------
def group_by_platform_sorted(records):
    """
    按主要平台分组，统计人数，按人数从多到少排序。

    参数:
        records (list[dict]): 用户数据列表。

    返回:
        list[tuple]: [(平台名, 人数), ...] 按人数降序排列

    知识点：
      - sorted() + lambda 对字典 items() 排序
      - 空值处理（Primary_Platform 可能为空）
    """
    platform_counts = defaultdict(int)

    for user in records:
        platform = user["Primary_Platform"]
        if platform:  # 跳过空值
            platform_counts[platform] += 1

    # sorted() 按人数降序排列
    # key=lambda x: x[1] 表示按元组的第二个元素（人数）排序
    sorted_platforms = sorted(
        platform_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_platforms


# ---------------------------------------------------------------------------
# 分类 ④：按年龄区间分组
# ---------------------------------------------------------------------------
def group_by_age_range(records):
    """
    按年龄区间分组：青少年(≤19)、青年(20-35)、中年(36-50)、老年(51+)。

    参数:
        records (list[dict]): 用户数据列表。

    返回:
        dict: {年龄段: 用户列表}
    """
    groups = {"青少年(≤19)": [], "青年(20-35)": [], "中年(36-50)": [], "老年(51+)": []}

    for user in records:
        try:
            age = int(user["Age"])
        except (ValueError, TypeError):
            continue  # 跳过无效年龄

        if age <= 19:
            groups["青少年(≤19)"].append(user)
        elif age <= 35:
            groups["青年(20-35)"].append(user)
        elif age <= 50:
            groups["中年(36-50)"].append(user)
        else:
            groups["老年(51+)"].append(user)

    return groups


# ---------------------------------------------------------------------------
# 分类 ⑤：双条件交叉分析 —— 性别 × 成瘾级别
# ---------------------------------------------------------------------------
def cross_analysis_gender_addiction(records):
    """
    交叉分析：每个性别在不同成瘾级别上的人数分布。

    参数:
        records (list[dict]): 用户数据列表。

    返回:
        dict: {性别: {成瘾级别: 人数}}

    知识点：
      - 两层嵌套字典
      - 双重循环遍历
    """
    # 外层字典：性别 → 内层字典；内层字典：成瘾级别 → 人数
    cross = defaultdict(lambda: defaultdict(int))

    for user in records:
        gender = user["Gender"]
        level = user["Addiction_Level"]
        if gender and level:  # 都不为空
            cross[gender][level] += 1

    # 转回普通 dict 便于打印
    return {k: dict(v) for k, v in cross.items()}


# ---------------------------------------------------------------------------
# 统计汇总：计算各成瘾级别的平均指标
# ---------------------------------------------------------------------------
def summary_by_level(records):
    """
    按成瘾级别统计若干指标的平均值。

    参数:
        records (list[dict]): 用户数据列表。

    返回:
        dict: {成瘾级别: {指标名: 平均值}}

    知识点：
      - 多层嵌套：字典→字典→列表
      - 数值转换与异常处理
    """
    # 要统计的字段列表
    fields = [
        ("Daily_Usage_Hours", "每日使用时长"),
        ("Notifications_Per_Day", "每日通知数"),
        ("Anxiety_Score", "焦虑评分"),
        ("Depression_Score", "抑郁评分"),
        ("Sleep_Hours", "睡眠时长"),
        ("Mental_Wellbeing_Score", "心理健康评分"),
    ]

    # 数据结构：{级别: {字段英文名: [数值列表]}}
    data = defaultdict(lambda: defaultdict(list))

    for user in records:
        level = user["Addiction_Level"]
        if not level:
            continue
        for eng_name, _ in fields:
            try:
                val = float(user[eng_name])
                data[level][eng_name].append(val)
            except (ValueError, TypeError):
                pass

    # 计算平均值
    result = {}
    for level, field_dict in data.items():
        result[level] = {}
        for eng_name, ch_name in fields:
            values = field_dict.get(eng_name, [])
            if values:
                avg = round(sum(values) / len(values), 2)
            else:
                avg = None
            result[level][ch_name] = avg

    return result


# ============================================================================
# 第三步：主函数 —— 运行所有分类并打印结果
# ============================================================================

def main():
    """主函数：读取数据 → 执行分类 → 打印结果"""
    print("=" * 60)
    print("📊 数据分类处理综合演示")
    print("=" * 60)

    # ---------- 读取数据 ----------
    print("\n📂 正在读取 CSV 文件...")
    records = read_csv_to_dicts(CSV_FILE)
    print(f"   共读取 {len(records)} 条用户记录\n")

    # ---------- ① 按成瘾级别分组 ----------
    print("=" * 60)
    print("📌 分类 ①：按成瘾级别分组")
    print("=" * 60)

    level_groups = group_by_addiction_level(records)
    for level, users in level_groups.items():
        print(f"  {level}: {len(users)} 人")

    # 进一步：列出每个级别前 3 个用户的 ID
    print("\n  每个级别前 3 名用户 ID：")
    for level, users in level_groups.items():
        ids = [u["User_ID"] for u in users[:3]]
        print(f"    {level}: {', '.join(ids)}")

    # ---------- ② 按性别分组 + 平均心理健康评分 ----------
    print("\n" + "=" * 60)
    print("📌 分类 ②：按性别分组 + 平均心理健康评分")
    print("=" * 60)

    gender_stats = group_by_gender_with_avg(records)
    for gender, stats in gender_stats.items():
        print(f"  {gender}: {stats['count']} 人, 平均心理健康评分 {stats['avg_wellbeing']}")

    # ---------- ③ 按主要平台分组并排序 ----------
    print("\n" + "=" * 60)
    print("📌 分类 ③：按主要平台分组（按人数降序）")
    print("=" * 60)

    platform_list = group_by_platform_sorted(records)
    for rank, (platform, count) in enumerate(platform_list, 1):
        bar = "█" * (count // 10)  # 简单可视化
        print(f"  {rank}. {platform:<12} {count:>4} 人 {bar}")

    # ---------- ④ 按年龄区间分组 ----------
    print("\n" + "=" * 60)
    print("📌 分类 ④：按年龄区间分组")
    print("=" * 60)

    age_groups = group_by_age_range(records)
    for age_range, users in age_groups.items():
        print(f"  {age_range}: {len(users)} 人")

    # ---------- ⑤ 交叉分析 ----------
    print("\n" + "=" * 60)
    print("📌 分类 ⑤：交叉分析 — 性别 × 成瘾级别")
    print("=" * 60)

    cross = cross_analysis_gender_addiction(records)
    # 获取所有成瘾级别并排序
    all_levels = ["Low", "Moderate", "High", "Severe"]
    # 打印表头
    header = f"{'性别':<12}" + "".join(f"{lv:<10}" for lv in all_levels)
    print(f"  {header}")
    print(f"  {'-' * (12 + 10 * len(all_levels))}")
    # 打印每行
    for gender in sorted(cross.keys()):
        row = f"{gender:<12}"
        for lv in all_levels:
            count = cross[gender].get(lv, 0)
            row += f"{count:<10}"
        print(f"  {row}")

    # ---------- ⑥ 各成瘾级别平均指标 ----------
    print("\n" + "=" * 60)
    print("📌 分类 ⑥：各成瘾级别平均指标对比")
    print("=" * 60)

    level_summary = summary_by_level(records)
    # 打印表头
    all_levels_sorted = sorted(level_summary.keys())
    # 获取指标名
    first_level = all_levels_sorted[0]
    indicators = list(level_summary[first_level].keys())

    header = f"{'指标':<16}" + "".join(f"{lv:<12}" for lv in all_levels_sorted)
    print(f"  {header}")
    print(f"  {'-' * (16 + 12 * len(all_levels_sorted))}")
    for ind in indicators:
        row = f"{ind:<16}"
        for lv in all_levels_sorted:
            val = level_summary[lv].get(ind, "")
            if val is not None:
                row += f"{val:<12}"
            else:
                row += f"{'N/A':<12}"
        print(f"  {row}")

    # ---------- 简单结论 ----------
    print("\n" + "=" * 60)
    print("💡 简单发现")
    print("=" * 60)

    # 找出人数最多的平台
    top_platform, top_count = platform_list[0]
    print(f"  • 最受欢迎的平台: {top_platform}（{top_count} 人）")

    # 找出人数最多的年龄段
    max_age_group = max(age_groups, key=lambda k: len(age_groups[k]))
    print(f"  • 人数最多的年龄段: {max_age_group}（{len(age_groups[max_age_group])} 人）")

    # 比较 Low 和 Severe 的平均心理健康评分
    low_wb = level_summary.get("Low", {}).get("心理健康评分", 0)
    severe_wb = level_summary.get("Severe", {}).get("心理健康评分", 0)
    if low_wb and severe_wb:
        print(f"  • Low 组平均心理健康评分: {low_wb}")
        print(f"  • Severe 组平均心理健康评分: {severe_wb}")
        print(f"  • 差异: {round(severe_wb - low_wb, 2)} 分")

    print("\n✅ 分类处理完成！")
    print("=" * 60)


# ============================================================================
# 启动
# ============================================================================
if __name__ == "__main__":
    main()
