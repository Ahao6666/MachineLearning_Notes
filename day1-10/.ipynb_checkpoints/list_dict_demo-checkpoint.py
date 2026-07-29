#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表（list）与字典（dict）数据类型练习脚本（list_dict_demo.py）

本脚本系统性地演示了 Python 中最常用的两种数据结构 —— 列表和字典，
涵盖它们的创建、增删改查、遍历、推导式、排序、嵌套等核心操作。

每个章节都包含：
  1. 语法说明（注释）
  2. 示例代码
  3. 预期输出（注释中标出）

适用人群：Python 初学者 / 希望巩固基础的数据结构学习者。
运行方式：python3 list_dict_demo.py
"""

import copy  # 用于深拷贝演示
from collections import defaultdict, Counter  # 用于高级字典用法


# ============================================================================
# 第一部分：列表（list）
# ============================================================================
# 列表是 Python 中最常用的序列类型，用方括号 [] 表示。
# 特点：有序、可变（可增删改）、可存放任意类型的元素。
# ============================================================================

print("=" * 60)
print("📋 第一部分：列表（list）基础操作")
print("=" * 60)

# ---------------------------------------------------------------------------
# 1.1 创建列表
# ---------------------------------------------------------------------------
print("\n--- 1.1 创建列表 ---")

# 空列表
empty_list = []
print(f"空列表: {empty_list}")

# 用 list() 构造函数创建空列表
empty_list2 = list()
print(f"用 list() 创建空列表: {empty_list2}")

# 包含整数元素的列表
numbers = [10, 20, 30, 40, 50]
print(f"整数列表: {numbers}")

# 包含字符串元素的列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"字符串列表: {fruits}")

# 混合类型列表（Python 列表可以存放不同类型的数据）
mixed = [1, "hello", 3.14, True, None]
print(f"混合类型列表: {mixed}")

# 用 range() 快速生成整数列表
# range(start, stop, step) 生成从 start 到 stop-1 的整数序列
range_list = list(range(1, 11))  # 1 到 10
print(f"用 range() 生成的列表: {range_list}")

# 列表推导式（list comprehension）—— 简洁地创建列表
# 语法：[表达式 for 变量 in 可迭代对象 if 条件]
squares = [x ** 2 for x in range(1, 6)]  # 1², 2², ..., 5²
print(f"列表推导式（平方）: {squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]  # 1~20 中的偶数
print(f"列表推导式（1~20 偶数）: {evens}")

# ---------------------------------------------------------------------------
# 1.2 访问列表元素
# ---------------------------------------------------------------------------
print("\n--- 1.2 访问列表元素 ---")

fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 正索引：从 0 开始
print(f"第一个元素（索引 0）: {fruits[0]}")
print(f"第三个元素（索引 2）: {fruits[2]}")

# 负索引：从 -1 开始表示最后一个元素
print(f"最后一个元素（索引 -1）: {fruits[-1]}")
print(f"倒数第二个元素（索引 -2）: {fruits[-2]}")

# 切片（slicing）：[start:stop:step] 提取子列表
# 注意：切片是左闭右开区间，即包含 start 但不包含 stop
print(f"前三个元素 [:3]: {fruits[:3]}")
print(f"从第二个到最后一个 [1:]: {fruits[1:]}")
print(f"倒数两个 [-2:]: {fruits[-2:]}")
print(f"步长为 2 [::2]: {fruits[::2]}")
print(f"反转列表 [::-1]: {fruits[::-1]}")

# ---------------------------------------------------------------------------
# 1.3 修改列表（增、删、改）
# ---------------------------------------------------------------------------
print("\n--- 1.3 修改列表（增、删、改）---")

# ---------- 增 ----------
animals = ["猫", "狗"]

# append()：在末尾追加一个元素
animals.append("兔子")
print(f"追加后: {animals}")

# insert(index, element)：在指定位置插入一个元素
animals.insert(1, "仓鼠")  # 在索引 1 处插入
print(f"插入后: {animals}")

# extend() 或 +=：将一个列表的所有元素追加到末尾
animals.extend(["乌龟", "金鱼"])
print(f"扩展后: {animals}")

# ---------- 删 ----------
# remove(value)：删除第一个匹配的元素（按值删除）
animals.remove("仓鼠")
print(f"删除 '仓鼠' 后: {animals}")

# pop(index)：删除并返回指定位置的元素（按索引删除），不传索引则删除最后一个
popped = animals.pop()  # 删除并返回最后一个
print(f"pop() 弹出的元素: {popped}")
print(f"pop() 后的列表: {animals}")

popped_at = animals.pop(1)  # 删除索引 1 的元素
print(f"pop(1) 弹出的元素: {popped_at}")

# del 语句：删除指定索引或整个列表
del animals[0]
print(f"del animals[0] 后: {animals}")

# clear()：清空整个列表
animals.clear()
print(f"clear() 后: {animals}")

# ---------- 改 ----------
numbers = [10, 20, 30, 40, 50]

# 通过索引直接赋值修改
numbers[0] = 100
print(f"修改第一个元素后: {numbers}")

# 通过切片批量修改
numbers[1:3] = [200, 300]  # 将索引 1~2 替换为 200, 300
print(f"切片批量修改后: {numbers}")

# ---------------------------------------------------------------------------
# 1.4 列表的常用方法和函数
# ---------------------------------------------------------------------------
print("\n--- 1.4 列表的常用方法和函数 ---")

scores = [85, 92, 78, 90, 88, 76, 95, 89]

# len()：获取列表长度（元素个数）
print(f"列表长度 len(): {len(scores)}")

# max() / min()：获取最大值 / 最小值
print(f"最大值 max(): {max(scores)}")
print(f"最小值 min(): {min(scores)}")

# sum()：求和
print(f"总和 sum(): {sum(scores)}")

# sorted()：返回排序后的新列表（原列表不变）
sorted_scores = sorted(scores)
print(f"升序排序 sorted(): {sorted_scores}")
sorted_desc = sorted(scores, reverse=True)  # 降序
print(f"降序排序 sorted(reverse=True): {sorted_desc}")

# sort()：原地排序（直接修改原列表）
scores_copy = scores.copy()
scores_copy.sort()
print(f"原地升序 sort(): {scores_copy}")

# count()：统计某个元素出现的次数
nums = [1, 2, 2, 3, 2, 4, 2]
print(f"2 的出现次数 count(2): {nums.count(2)}")

# index()：查找某个元素首次出现的索引
print(f"3 的索引 index(3): {nums.index(3)}")

# in 运算符：判断元素是否在列表中
print(f"5 是否在列表中: {5 in nums}")
print(f"2 是否在列表中: {2 in nums}")

# reverse()：原地反转列表
nums_copy = nums.copy()
nums_copy.reverse()
print(f"原地反转 reverse(): {nums_copy}")

# ---------------------------------------------------------------------------
# 1.5 遍历列表
# ---------------------------------------------------------------------------
print("\n--- 1.5 遍历列表 ---")

students = ["Alice", "Bob", "Charlie", "Diana"]

# 方式一：直接遍历元素
print("方式一：直接遍历元素")
for s in students:
    print(f"  👤 {s}")

# 方式二：使用索引遍历（配合 range() + len()）
print("方式二：使用索引遍历")
for i in range(len(students)):
    print(f"  [{i}] {students[i]}")

# 方式三：使用 enumerate() 同时获取索引和元素（最推荐）
print("方式三：使用 enumerate()")
for i, name in enumerate(students):
    print(f"  [{i}] {name}")

# enumerate() 可以指定起始编号
for i, name in enumerate(students, start=1):
    print(f"  [{i}] {name}")

# 方式四：使用 zip() 同时遍历多个列表
names = ["小明", "小红", "小刚"]
ages = [18, 19, 20]
print("方式四：使用 zip() 同时遍历多个列表")
for name, age in zip(names, ages):
    print(f"  {name} 今年 {age} 岁")

# ---------------------------------------------------------------------------
# 1.6 列表的复制 —— 浅拷贝 vs 深拷贝
# ---------------------------------------------------------------------------
print("\n--- 1.6 列表的复制（浅拷贝 vs 深拷贝）---")

# 直接赋值 = 只是给列表多了一个别名，两个变量指向同一个内存地址
original = [[1, 2], [3, 4]]
alias = original
alias[0][0] = 999
print(f"直接赋值后 original 也被改了: {original}")  # 被改动了！

# 浅拷贝：copy() 或 [:] —— 只复制外层列表，内层列表仍然是引用
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999
print(f"浅拷贝后 original 也被改了: {original}")  # 也被改动了！

# 深拷贝：copy.deepcopy() —— 完全独立的副本
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(f"深拷贝后 original 不受影响: {original}")  # 保持 [1, 2]

# ---------------------------------------------------------------------------
# 1.7 列表的常用技巧
# ---------------------------------------------------------------------------
print("\n--- 1.7 列表的常用技巧 ---")

# 列表拼接：+ 运算符
list_a = [1, 2, 3]
list_b = [4, 5, 6]
merged = list_a + list_b
print(f"列表拼接: {merged}")

# 列表重复：* 运算符
repeated = [0] * 5
print(f"列表重复: {repeated}")

# 列表拆分解包（unpacking）
first, second, *rest = [10, 20, 30, 40, 50]
print(f"解包: first={first}, second={second}, rest={rest}")

# 用 * 合并多个列表（Python 3.5+）
combined = [*list_a, *list_b]
print(f"用 * 解包合并: {combined}")

# any() / all()：判断列表中是否有 / 是否全部满足条件
nums = [1, 3, 5, 7, 9]
print(f"是否有偶数 any(x%2==0): {any(x % 2 == 0 for x in nums)}")
print(f"是否全是奇数 all(x%2!=0): {all(x % 2 != 0 for x in nums)}")

# filter()：按条件过滤（返回迭代器）
filtered = list(filter(lambda x: x > 5, [3, 7, 1, 9, 4]))
print(f"filter() 过滤大于 5 的元素: {filtered}")

# map()：对所有元素执行函数（返回迭代器）
mapped = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(f"map() 每个元素乘以 2: {mapped}")


# ============================================================================
# 第二部分：字典（dict）
# ============================================================================
# 字典是 Python 中映射类型的代表，用花括号 {} 表示键值对。
# 特点：无序（Python 3.7+ 保留插入顺序）、可变、键必须唯一且不可变。
# ============================================================================

print("\n" + "=" * 60)
print("📖 第二部分：字典（dict）基础操作")
print("=" * 60)

# ---------------------------------------------------------------------------
# 2.1 创建字典
# ---------------------------------------------------------------------------
print("\n--- 2.1 创建字典 ---")

# 空字典
empty_dict = {}
print(f"空字典: {empty_dict}")

# 用 dict() 构造函数创建空字典
empty_dict2 = dict()
print(f"用 dict() 创建空字典: {empty_dict2}")

# 直接使用花括号创建键值对
student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "grades": [85, 92, 78],
}
print(f"学生信息字典: {student}")

# 使用 dict() 关键字参数创建（键名必须是合法标识符）
person = dict(name="李四", age=25, city="北京")
print(f"用 dict() 创建: {person}")

# 使用 dict() 传入元组列表
pairs = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"从元组列表创建: {pairs}")

# 使用 zip() 将两个列表合并为字典
keys = ["name", "age", "city"]
values = ["王五", 22, "上海"]
merged_dict = dict(zip(keys, values))
print(f"用 zip() 创建字典: {merged_dict}")

# 字典推导式（dictionary comprehension）
# 语法：{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"字典推导式（平方）: {squares_dict}")

even_odd = {x: ("偶数" if x % 2 == 0 else "奇数") for x in range(1, 11)}
print(f"字典推导式（奇偶判断）: {even_odd}")

# ---------------------------------------------------------------------------
# 2.2 访问字典元素
# ---------------------------------------------------------------------------
print("\n--- 2.2 访问字典元素 ---")

student = {"name": "张三", "age": 20, "major": "计算机科学"}

# 方式一：用方括号 [] 访问（键不存在时会抛出 KeyError）
print(f"name（方括号访问）: {student['name']}")

# 方式二：用 get() 方法（键不存在时返回 None 或指定默认值，更安全）
print(f"age（get() 访问）: {student.get('age')}")
print(f"未存在的键 get() 返回: {student.get('gender')}")
print(f"get() 设置默认值: {student.get('gender', '未知')}")

# 访问嵌套字典
users = {
    "user1": {"name": "Alice", "scores": {"math": 95, "english": 88}},
    "user2": {"name": "Bob", "scores": {"math": 72, "english": 91}},
}
print(f"嵌套字典访问: {users['user1']['scores']['math']}")  # 输出 95

# ---------------------------------------------------------------------------
# 2.3 修改字典（增、删、改）
# ---------------------------------------------------------------------------
print("\n--- 2.3 修改字典（增、删、改）---")

# ---------- 增 / 改 ----------
info = {"name": "小明"}

# 直接赋值：键不存在时新增，存在时更新
info["age"] = 18         # 新增键 "age"
info["name"] = "小红"    # 更新键 "name"
print(f"新增和更新后: {info}")

# update()：批量更新或合并另一个字典
info.update({"city": "深圳", "age": 19})
print(f"update() 后: {info}")

# setdefault(key, default)：键不存在时设置默认值并返回，存在时返回原值
city = info.setdefault("country", "中国")
print(f"setdefault() 返回: {city}")
print(f"setdefault() 后字典: {info}")

# ---------- 删 ----------
# pop(key[, default])：删除指定键并返回其值，键不存在时返回 default 或抛出 KeyError
removed = info.pop("country")
print(f"pop() 删除了: {removed}")

# del 语句：删除指定键或整个字典
del info["city"]
print(f"del city 后: {info}")

# popitem()：删除并返回最后一个插入的键值对（Python 3.7+ 有序）
last_item = info.popitem()
print(f"popitem() 删除了: {last_item}")

# clear()：清空字典
info.clear()
print(f"clear() 后: {info}")

# ---------------------------------------------------------------------------
# 2.4 遍历字典
# ---------------------------------------------------------------------------
print("\n--- 2.4 遍历字典 ---")

student = {"name": "张三", "age": 20, "major": "计算机科学", "grade": 88}

# 方式一：遍历键（默认）
print("方式一：遍历键")
for key in student:
    print(f"  {key}: {student[key]}")

# 方式二：遍历值
print("方式二：遍历值")
for value in student.values():
    print(f"  {value}")

# 方式三：遍历键值对（最常用）
print("方式三：遍历键值对")
for key, value in student.items():
    print(f"  {key} -> {value}")

# 方式四：同时遍历多个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
    print(f"  {k1}={v1}, {k2}={v2}")

# ---------------------------------------------------------------------------
# 2.5 字典的常用方法和操作
# ---------------------------------------------------------------------------
print("\n--- 2.5 字典的常用方法和操作 ---")

inventory = {"苹果": 10, "香蕉": 5, "橙子": 8, "葡萄": 3}

# keys()：获取所有键
print(f"所有键: {list(inventory.keys())}")

# values()：获取所有值
print(f"所有值: {list(inventory.values())}")

# items()：获取所有键值对（元组形式）
print(f"所有键值对: {list(inventory.items())}")

# in 运算符：判断键是否存在
print(f"'苹果' 是否在字典中: {'苹果' in inventory}")
print(f"'西瓜' 是否在字典中: {'西瓜' in inventory}")

# len()：获取键值对数量
print(f"字典长度: {len(inventory)}")

# 合并字典（Python 3.9+ 用 | 运算符）
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}  # 注意 y 重复
merged_dicts = a | b  # 后面的会覆盖前面的
print(f"用 | 合并字典（3.9+）: {merged_dicts}")

# 另一种合并方式：** 解包
merged_dicts2 = {**a, **b}
print(f"用 ** 解包合并: {merged_dicts2}")

# ---------------------------------------------------------------------------
# 2.6 字典的常见应用场景
# ---------------------------------------------------------------------------
print("\n--- 2.6 字典的常见应用场景 ---")

# 场景一：使用字典作为计数器（统计词频）
text = "hello world hello python hello world"
word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f"词频统计: {word_counts}")

# 更优雅的方式：使用 get()
word_counts2 = {}
for word in text.split():
    word_counts2[word] = word_counts2.get(word, 0) + 1
print(f"词频统计（get 方式）: {word_counts2}")

# 更更优雅的方式：使用 collections.Counter
word_counts3 = Counter(text.split())
print(f"词频统计（Counter）: {dict(word_counts3)}")

# 场景二：用字典分组数据
students_data = [
    ("Alice", "A班", 85),
    ("Bob", "B班", 92),
    ("Charlie", "A班", 78),
    ("Diana", "B班", 95),
    ("Eve", "A班", 88),
]
classes = {}
for name, cls, score in students_data:
    if cls not in classes:
        classes[cls] = []
    classes[cls].append({"name": name, "score": score})
print(f"按班级分组:")
for cls, members in classes.items():
    print(f"  {cls}: {members}")

# 场景三：用字典做缓存（记忆化）
def fibonacci(n, cache={}):
    """带缓存的斐波那契数列"""
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

print(f"斐波那契(10) = {fibonacci(10)}")
print(f"缓存内容: {fibonacci.__defaults__[0]}")

# ---------------------------------------------------------------------------
# 2.7 defaultdict —— 带默认值的字典
# ---------------------------------------------------------------------------
print("\n--- 2.7 defaultdict 的使用 ---")

# defaultdict 在键不存在时会自动调用工厂函数生成默认值
# 参数可以是 list, int, set, str 等类型

# 例1：统计每个字母出现的位置
from collections import defaultdict

positions = defaultdict(list)
for i, char in enumerate("abracadabra"):
    positions[char].append(i)
print(f"字母位置（defaultdict）: {dict(positions)}")

# 例2：统计每个类别的总分
scores_data = [
    ("math", 90),
    ("english", 85),
    ("math", 95),
    ("english", 88),
    ("science", 92),
]
subject_totals = defaultdict(int)
for subject, score in scores_data:
    subject_totals[subject] += score
print(f"科目总分（defaultdict）: {dict(subject_totals)}")


# ============================================================================
# 第三部分：列表与字典的嵌套与综合练习
# ============================================================================

print("\n" + "=" * 60)
print("🔗 第三部分：列表与字典的嵌套及综合练习")
print("=" * 60)

# ---------------------------------------------------------------------------
# 3.1 列表嵌套字典 —— 表格数据的常见表示方式
# ---------------------------------------------------------------------------
print("\n--- 3.1 列表嵌套字典（类似表格/JSON 数据） ---")

# 每个字典代表一条记录，整个列表代表一个数据集
employees = [
    {"id": 101, "name": "张三", "department": "技术部", "salary": 15000},
    {"id": 102, "name": "李四", "department": "市场部", "salary": 12000},
    {"id": 103, "name": "王五", "department": "技术部", "salary": 18000},
    {"id": 104, "name": "赵六", "department": "人事部", "salary": 13000},
    {"id": 105, "name": "钱七", "department": "市场部", "salary": 11000},
]

# 查询：找出所有技术部的员工
tech_emps = [e for e in employees if e["department"] == "技术部"]
print(f"技术部员工: {tech_emps}")

# 查询：工资高于 13000 的员工
high_salary = [e["name"] for e in employees if e["salary"] > 13000]
print(f"工资高于 13000 的员工: {high_salary}")

# 聚合：按部门分组并统计平均工资
dept_salaries = defaultdict(list)
for emp in employees:
    dept_salaries[emp["department"]].append(emp["salary"])

for dept, salaries in dept_salaries.items():
    avg = sum(salaries) / len(salaries)
    print(f"  {dept} 平均工资: {avg:.0f}")

# 排序：按工资从高到低排序
sorted_emps = sorted(employees, key=lambda e: e["salary"], reverse=True)
print(f"按工资排序（前三）:")
for emp in sorted_emps[:3]:
    print(f"  {emp['name']}: {emp['salary']}")

# ---------------------------------------------------------------------------
# 3.2 字典嵌套列表
# ---------------------------------------------------------------------------
print("\n--- 3.2 字典嵌套列表 ---")

course = {
    "name": "Python 编程",
    "teacher": "陈老师",
    "students": [
        {"name": "小明", "scores": [88, 92, 85]},
        {"name": "小红", "scores": [95, 89, 91]},
        {"name": "小刚", "scores": [70, 75, 80]},
    ],
}

# 遍历嵌套结构
print(f"课程: {course['name']}, 老师: {course['teacher']}")
for s in course["students"]:
    avg_score = sum(s["scores"]) / len(s["scores"])
    print(f"  学生: {s['name']}, 平均分: {avg_score:.1f}")

# 计算全班平均分
all_scores = [score for s in course["students"] for score in s["scores"]]
class_avg = sum(all_scores) / len(all_scores)
print(f"  全班平均分: {class_avg:.1f}")

# ---------------------------------------------------------------------------
# 3.3 综合练习：学生成绩管理系统（迷你版）
# ---------------------------------------------------------------------------
print("\n--- 3.3 综合练习：迷你学生成绩管理系统 ---")


def demonstrate_grade_system():
    """
    一个迷你学生成绩管理系统，综合运用列表和字典的各种操作。
    """
    # 数据存储：列表嵌套字典
    students = []

    def add_student(name, scores):
        """添加学生"""
        students.append({"name": name, "scores": scores, "total": sum(scores)})
        print(f"✅ 已添加学生: {name}")

    def find_student(name):
        """查找学生"""
        for s in students:
            if s["name"] == name:
                return s
        return None

    def remove_student(name):
        """删除学生"""
        for i, s in enumerate(students):
            if s["name"] == name:
                removed = students.pop(i)
                print(f"🗑️ 已删除学生: {removed['name']}")
                return
        print(f"❌ 未找到学生: {name}")

    def list_students():
        """列出所有学生（按总分降序）"""
        sorted_students = sorted(
            students, key=lambda s: s["total"], reverse=True
        )
        print(f"{'排名':<4} {'姓名':<6} {'总分':<6} {'平均分':<6}")
        print("-" * 24)
        for rank, s in enumerate(sorted_students, 1):
            avg = s["total"] / len(s["scores"])
            print(f"{rank:<4} {s['name']:<6} {s['total']:<6} {avg:<6.1f}")

    def group_by_performance():
        """按成绩分组（优秀 >= 85，及格 >= 60，不及格 < 60）"""
        groups = {"优秀": [], "及格": [], "不及格": []}
        for s in students:
            avg = s["total"] / len(s["scores"])
            if avg >= 85:
                groups["优秀"].append(s["name"])
            elif avg >= 60:
                groups["及格"].append(s["name"])
            else:
                groups["不及格"].append(s["name"])
        return groups

    # ---- 使用示例 ----
    add_student("Alice", [85, 92, 78])
    add_student("Bob", [72, 65, 58])
    add_student("Charlie", [95, 90, 92])
    add_student("Diana", [60, 55, 70])

    print()
    list_students()

    print()
    print("按成绩分组:", group_by_performance())

    print()
    bob = find_student("Bob")
    if bob:
        print(f"🔍 找到 Bob: {bob}")

    remove_student("Bob")

    print()
    print("删除 Bob 后的学生列表:")
    list_students()


demonstrate_grade_system()


# ============================================================================
# 第四部分：常用技巧总结
# ============================================================================

print("\n" + "=" * 60)
print("💡 第四部分：常用技巧速查")
print("=" * 60)

tips = [
    ("列表去重（保持顺序）", "list(dict.fromkeys([1,2,2,3,1]))"),
    ("字典获取值（含默认值）", "dic.get(key, default)"),
    ("列表扁平化", "[item for sublist in nested for item in sublist]"),
    ("两个列表转字典", "dict(zip(keys, values))"),
    ("按值排序字典", "sorted(dic.items(), key=lambda x: x[1])"),
    ("统计列表元素频率", "collections.Counter(lst).most_common(n)"),
    ("列表分组", "collections.defaultdict(list)"),
    ("深拷贝", "copy.deepcopy(obj)"),
]

for i, (title, code) in enumerate(tips, 1):
    print(f"  {i}. {title}")
    print(f"     代码: {code}")
    print()

print("=" * 60)
print("✅ 练习脚本运行完毕！希望你有所收获 🚀")
print("=" * 60)
