#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV 读取测试脚本（read_csv_demo.py）

本脚本用于演示如何使用 Python 标准库 `csv` 读取本地 CSV 文件，
并打印文件的基本结构信息：列数、行数、列名以及前 5 行数据。
此外，还演示如何按年龄范围、每日使用小时数范围筛选用户 ID，
以及如何同时满足多个条件（例如年龄在 20-30 岁且每日使用 2-5 小时）。

适用场景：
- 快速检查 CSV 文件是否能被正常读取
- 查看数据列名和字段顺序
- 学习如何基于单个或多个列名筛选 CSV 数据
- 作为更复杂数据分析流程的起点

依赖：仅使用 Python 标准库，无需额外安装第三方包。
"""

import csv       # 标准库：用于读取 CSV 格式文件
import sys       # 标准库：用于向标准错误流输出信息并退出程序
from pathlib import Path  # 标准库：用于以面向对象方式处理文件路径

# 获取当前脚本所在目录，并拼接 CSV 文件名。
# 这样无论脚本从哪个目录被运行，都能正确找到同目录下的 CSV 文件。
CSV_FILE = Path(__file__).parent / "social_media_addiction_mental_wellbeing.csv"


def read_csv(path):
    """
    读取 CSV 文件并返回表头和数据行列表。

    参数:
        path (str | pathlib.Path): CSV 文件的路径。

    返回:
        tuple[list[str], list[list[str]]]:
            - 第一个元素是表头（列名）列表
            - 第二个元素是数据行列表，每一行本身也是一个字符串列表

    说明:
        - 使用 `encoding="utf-8"` 确保中文等字符正常读取
        - 使用 `newline=""` 是 csv 模块的官方推荐做法，避免换行符被错误转换
    """
    # 打开文件，创建一个 csv 读取器对象
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        # 读取第一行作为表头
        # next(reader) 会从迭代器中取出下一行，并移动内部指针到第二行
        headers = next(reader)

        # 读取剩余所有行，转换为列表
        rows = list(reader)

    return headers, rows


def filter_users_by_Daily_Usage_Hours_range(headers, rows, min_hours, max_hours):
    """
    根据每日使用小时数范围筛选用户 ID。

    参数:
        headers (list[str]): 表头列表，用于定位列名。
        rows (list[list[str]]): 数据行列表。
        min_hours (float): 每日使用小时数下限（包含）。
        max_hours (float): 每日使用小时数上限（包含）。

    返回:
        list[str]: 符合条件的 User_ID 列表。

    说明:
        - 通过列名查找索引，避免硬编码列号，增强代码健壮性
        - 如果每日使用小时数字段为空或无法转换为浮点数，则跳过该行
    """
    # 根据列名查找对应的列索引
    user_id_index = headers.index("User_ID")
    daily_usage_hours_index = headers.index("Daily_Usage_Hours")

    matched_user_ids = []
    for row in rows:
        # 尝试将 Daily_Usage_Hours 字段转换为浮点数
        try:
            daily_usage_hours = float(row[daily_usage_hours_index])
        except (ValueError, IndexError):
            # 跳过空值或无法解析的每日使用小时数
            continue

        # 判断每日使用小时数是否在指定范围内（包含边界）
        if min_hours <= daily_usage_hours <= max_hours:
            matched_user_ids.append(row[user_id_index])

    return matched_user_ids

def filter_users_by_age_range(headers, rows, min_age, max_age):
    """
    根据年龄范围筛选用户 ID。

    参数:
        headers (list[str]): 表头列表，用于定位列名。
        rows (list[list[str]]): 数据行列表。
        min_age (int): 年龄下限（包含）。
        max_age (int): 年龄上限（包含）。

    返回:
        list[str]: 符合条件的 User_ID 列表。

    说明:
        - 通过列名查找索引，避免硬编码列号，增强代码健壮性
        - 如果年龄字段为空或无法转换为整数，则跳过该行
    """
    # 根据列名查找对应的列索引
    user_id_index = headers.index("User_ID")
    age_index = headers.index("Age")

    matched_user_ids = []
    for row in rows:
        # 尝试将 Age 字段转换为整数
        try:
            age = int(row[age_index])
        except (ValueError, IndexError):
            # 跳过空值或无法解析的年龄
            continue

        # 判断年龄是否在指定范围内（包含边界）
        if min_age <= age <= max_age:
            matched_user_ids.append(row[user_id_index])

    return matched_user_ids


def filter_users_by_age_and_usage(headers, rows, min_age, max_age, min_hours, max_hours):
    """
    同时根据年龄范围和每日使用小时数范围筛选用户 ID。

    参数:
        headers (list[str]): 表头列表，用于定位列名。
        rows (list[list[str]]): 数据行列表。
        min_age (int): 年龄下限（包含）。
        max_age (int): 年龄上限（包含）。
        min_hours (float): 每日使用小时数下限（包含）。
        max_hours (float): 每日使用小时数上限（包含）。

    返回:
        list[str]: 同时满足年龄和使用时长条件的 User_ID 列表。

    说明:
        - 通过列名查找索引，避免硬编码列号，增强代码健壮性
        - 如果年龄或每日使用小时数字段为空或无法转换，则跳过该行
        - 只有年龄和使用时长都落在指定范围内，才会被保留
    """
    # 根据列名查找对应的列索引
    user_id_index = headers.index("User_ID")
    age_index = headers.index("Age")
    daily_usage_hours_index = headers.index("Daily_Usage_Hours")

    matched_user_ids = []
    for row in rows:
        # 尝试将 Age 字段转换为整数
        try:
            age = int(row[age_index])
        except (ValueError, IndexError):
            continue

        # 尝试将 Daily_Usage_Hours 字段转换为浮点数
        try:
            daily_usage_hours = float(row[daily_usage_hours_index])
        except (ValueError, IndexError):
            continue

        # 只有年龄和使用时长同时满足条件才保留
        if (min_age <= age <= max_age and
                min_hours <= daily_usage_hours <= max_hours):
            matched_user_ids.append(row[user_id_index])

    return matched_user_ids


def filter_users_combined(headers, rows, age_range, usage_range):
    """
    通过复用现有筛选函数，返回同时满足年龄和使用时长条件的用户 ID。

    参数:
        headers (list[str]): 表头列表，用于定位列名。
        rows (list[list[str]]): 数据行列表。
        age_range (tuple[int, int]): 年龄范围（下限，上限），包含边界。
        usage_range (tuple[float, float]): 每日使用小时数范围（下限，上限），包含边界。

    返回:
        list[str]: 同时满足两个条件的 User_ID 列表。

    说明:
        - 本函数不直接读取 CSV 数据，而是调用已有的 filter_users_by_age_range
          和 filter_users_by_Daily_Usage_Hours_range 函数
        - 使用 set 集合求交集，逻辑清晰且效率高
        - 如果以后有更多条件（如性别、平台等），可以继续复用相应函数并取交集
    """
    age_min, age_max = age_range
    usage_min, usage_max = usage_range

    # 复用现有函数分别获取满足单个条件的用户集合
    age_users = set(filter_users_by_age_range(headers, rows, age_min, age_max))
    usage_users = set(filter_users_by_Daily_Usage_Hours_range(headers, rows, usage_min, usage_max))

    # 取交集得到同时满足两个条件的用户
    combined_users = age_users & usage_users

    return list(combined_users)


def main():
    """
    脚本主入口：检查 CSV 文件是否存在，读取并打印基本信息及筛选结果。
    """
    # 检查 CSV 文件是否存在，不存在则打印错误信息并退出
    if not CSV_FILE.exists():
        print(f"错误：文件未找到: {CSV_FILE}", file=sys.stderr)
        sys.exit(1)

    # 调用 read_csv 函数读取表头和数据行
    headers, rows = read_csv(CSV_FILE)

    # 打印 CSV 文件的基本结构信息
    print(f"文件路径: {CSV_FILE}")
    print(f"列数: {len(headers)}")
    print(f"数据行数: {len(rows)}")
    print(f"表头（列名）: {headers}")
    print()

    # 打印前 5 行数据，用于快速预览
    print("前 5 行数据:")
    for index, row in enumerate(rows[:5], start=1):
        print(f"  第 {index} 行: {row}")
    print()

    # 筛选年龄在 20-30 岁（含）之间的用户 ID
    min_age = 22
    max_age = 25
    matched_users = filter_users_by_age_range(headers, rows, min_age, max_age)

    print(f"年龄在 {min_age}-{max_age} 岁之间的用户数: {len(matched_users)}")
    display_count = min(10, len(matched_users))
    print(f"前 {display_count} 个符合条件的 User_ID:")
    for user_id in matched_users[:display_count]:
        print(f"  {user_id}")
    
    # 筛选每日使用小时数在 2-5 小时（含）之间的用户 ID
    min_hours = 2.0
    max_hours = 5.0
    matched_users_hours = filter_users_by_Daily_Usage_Hours_range(headers, rows, min_hours, max_hours)
    print(f"每日使用小时数在 {min_hours}-{max_hours} 小时之间的用户数: {len(matched_users_hours)}")
    display_count = min(10, len(matched_users_hours))
    print(f"前 {display_count} 个符合条件的 User_ID:")
    for user_id in matched_users_hours[:display_count]:
        print(f"  {user_id}")
    print()

    # 同时筛选：年龄在 20-30 岁（含）且每日使用小时数在 2-5 小时（含）的用户 ID
    min_age_combined = 20
    max_age_combined = 30
    min_hours_combined = 2.0
    max_hours_combined = 5.0
    matched_users_combined = filter_users_by_age_and_usage(
        headers, rows,
        min_age_combined, max_age_combined,
        min_hours_combined, max_hours_combined
    )

    print(f"年龄 {min_age_combined}-{max_age_combined} 岁且每日使用 "
          f"{min_hours_combined}-{max_hours_combined} 小时的用户数: "
          f"{len(matched_users_combined)}")
    display_count = min(10, len(matched_users_combined))
    print(f"前 {display_count} 个符合条件的 User_ID:")
    for user_id in matched_users_combined[:display_count]:
        print(f"  {user_id}")
    print()

    # 使用复用函数的组合筛选：年龄 20-30 岁（含）且每日使用 2-5 小时（含）
    matched_users_combined_reuse = filter_users_combined(
        headers, rows,
        age_range=(20, 30),
        usage_range=(2.0, 5.0)
    )

    print(f"通过复用函数筛选：年龄 20-30 岁且每日使用 2.0-5.0 小时的用户数: "
          f"{len(matched_users_combined_reuse)}")
    display_count = min(10, len(matched_users_combined_reuse))
    print(f"前 {display_count} 个符合条件的 User_ID:")
    for user_id in matched_users_combined_reuse[:display_count]:
        print(f"  {user_id}")

# 当脚本被直接运行时执行 main() 函数；
# 如果被作为模块导入到其他脚本中，则不会自动执行。
if __name__ == "__main__":
    main()
