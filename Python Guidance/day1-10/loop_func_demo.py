#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环与函数使用技巧练习脚本（loop_func_demo.py）

本脚本系统性地演示了 Python 中两大核心编程概念 —— 循环和函数，
涵盖它们的语法、进阶用法、常见陷阱和实用技巧。

每个章节都包含：
  1. 语法说明（详细注释）
  2. 示例代码
  3. 预期输出（注释中标出）

适用人群：Python 初学者 / 希望巩固基础的编程学习者。
运行方式：python3 loop_func_demo.py
"""

import sys
from functools import reduce, wraps, partial


# ============================================================================
# 第一部分：循环（Loops）
# ============================================================================
# Python 中有两种循环：for 循环（遍历可迭代对象）和 while 循环（条件循环）。
# 配合 break、continue、else 子句可以实现灵活的控制流。
# ============================================================================

print("=" * 60)
print("🔁 第一部分：循环（Loops）基础与进阶")
print("=" * 60)


# ---------------------------------------------------------------------------
# 1.1 for 循环 —— 遍历各种数据类型
# ---------------------------------------------------------------------------
print("\n--- 1.1 for 循环：遍历各种数据类型 ---")

# --- 1.1.1 遍历 range（数字序列）---
print("【遍历 range】")
# range(stop)        → 0 ~ stop-1
# range(start, stop) → start ~ stop-1
# range(start, stop, step) → 按步长
for i in range(3):
    print(f"  range(3): {i}", end="  ")
print()  # 换行

for i in range(1, 6, 2):  # 1, 3, 5
    print(f"  range(1,6,2): {i}", end="  ")
print()

# --- 1.1.2 遍历列表 ---
print("\n【遍历列表】")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"  {fruit}", end="  ")
print()

# --- 1.1.3 遍历字符串（字符）---
print("\n【遍历字符串】")
for char in "Python":
    print(f"  '{char}'", end=" ")
print()

# --- 1.1.4 遍历字典 ---
print("\n【遍历字典】")
info = {"name": "张三", "age": 20, "city": "北京"}
for key in info:                  # 遍历键
    print(f"  键: {key}", end="  ")
print()
for value in info.values():       # 遍历值
    print(f"  值: {value}", end="  ")
print()
for k, v in info.items():         # 遍历键值对
    print(f"  {k}={v}", end="  ")
print()

# --- 1.1.5 遍历元组列表（解包）---
print("\n【遍历元组列表（解包）】")
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, letter in pairs:
    print(f"  {num} → {letter}", end="  ")
print()


# ---------------------------------------------------------------------------
# 1.2 常用遍历技巧
# ---------------------------------------------------------------------------
print("\n--- 1.2 常用遍历技巧 ---")

# --- enumerate() —— 同时获取索引和值 ---
print("【enumerate() — 带索引遍历】")
colors = ["红", "绿", "蓝"]
for idx, color in enumerate(colors):
    print(f"  索引 {idx}: {color}")

# 指定起始编号
for idx, color in enumerate(colors, start=1):
    print(f"  第 {idx} 个: {color}")

# --- zip() —— 同时遍历多个列表 ---
print("\n【zip() — 同时遍历多个列表】")
names = ["小明", "小红", "小刚"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score} 分（{grade}）")

# zip() 在最短的列表结束时停止（可以改用 zip_longest）
print("\n  zip 在最短处停止：")
list_a = [1, 2, 3, 4]
list_b = ["a", "b", "c"]
for a, b in zip(list_a, list_b):
    print(f"  {a}→{b}", end="  ")
print()

# --- reversed() —— 反向遍历 ---
print("\n【reversed() — 反向遍历】")
for num in reversed([1, 2, 3, 4, 5]):
    print(f"  {num}", end="  ")
print()

# --- sorted() —— 排序后遍历（不修改原列表）---
print("\n【sorted() — 排序后遍历】")
nums = [3, 1, 4, 1, 5, 9]
for n in sorted(nums):
    print(f"  {n}", end="  ")
print()
for n in sorted(nums, reverse=True):  # 降序
    print(f"  {n}", end="  ")
print()


# ---------------------------------------------------------------------------
# 1.3 while 循环
# ---------------------------------------------------------------------------
print("\n--- 1.3 while 循环 ---")

# while 循环：当条件为 True 时持续执行
# 适用于：不确定循环次数，依赖某个条件控制的情况

# --- 基础用法 ---
print("【基础用法：累加 1~5】")
n = 1
total = 0
while n <= 5:
    total += n
    n += 1
print(f"  1+2+3+4+5 = {total}")

# --- 用 break 提前终止 ---
print("\n【while + break：直到遇到 3 为止】")
n = 1
while True:        # 死循环，必须靠内部 break 退出
    print(f"  {n}", end="  ")
    if n == 3:
        print("→ 遇到 3，break 退出")
        break
    n += 1

# --- 用 continue 跳过本次循环 ---
print("\n【while + continue：跳过 3】")
n = 0
while n < 6:
    n += 1
    if n == 3:
        print("  (跳过 3)", end="  ")
        continue   # 跳过本次循环剩余代码
    print(f"  {n}", end="  ")
print()

# --- while + else —— 循环正常结束时执行 ---
print("\n【while + else：正常结束才执行 else】")
n = 1
while n <= 3:
    print(f"  {n}", end="  ")
    n += 1
else:
    print("→ 循环正常结束（没有被 break）")

print("\n  【对比】如果被 break，else 不执行：")
n = 1
while n <= 5:
    print(f"  {n}", end="  ")
    if n == 3:
        print("→ break 了")
        break
    n += 1
else:
    print("→ 这句不会执行")
# 注意：else 只有循环被 break 打断时才不执行，
# 其他情况（包括条件变为 False）都会执行


# ---------------------------------------------------------------------------
# 1.4 for + else —— for 循环也能用 else
# ---------------------------------------------------------------------------
print("\n--- 1.4 for + else 子句 ---")
#
# for-else 的 else 在循环没有被 break 中断时执行。
# 经典应用：查找元素，没找到时给出提示。

print("【for + else：查找素数】")

def is_prime(n):
    """判断 n 是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"  {n} 能被 {i} 整除 → 不是素数")
            break
    else:
        # 只有 for 循环完整跑完（没被 break）才会进入这里
        print(f"  {n} 是素数 ✅")
        return True
    return False

is_prime(7)
is_prime(10)
#
# 关键理解：for-else 的 else 是"没有 break"的意思，
#           不是"循环结束"的意思（循环结束总会执行，
#           而 else 只有在没有被 break 时才执行）。
#


# ---------------------------------------------------------------------------
# 1.5 嵌套循环
# ---------------------------------------------------------------------------
print("\n--- 1.5 嵌套循环 ---")

# 外层循环每执行一次，内层循环完整执行一轮

print("【打印乘法口诀表】")
for i in range(1, 10):           # 外层：行
    for j in range(1, i + 1):    # 内层：列（只到 i）
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()  # 换行

# 嵌套循环中的 break/continue 只作用于当前最内层循环
print("\n【嵌套循环中的 break 只跳出内层】")
for i in range(3):
    for j in range(5):
        if j == 3:
            break      # 只跳出内层 j 循环
        print(f"({i},{j})", end=" ")
    print("  ← 内层 break 后回到外层")
#
# 如果想跳出多层循环，可以用：
#   方法 1：将循环封装成函数 + return
#   方法 2：使用 flag 变量
#   方法 3：for-else（检查内层是否 break）
#


# ---------------------------------------------------------------------------
# 1.6 列表推导式（复习与进阶）
# ---------------------------------------------------------------------------
print("\n--- 1.6 列表推导式（复习与进阶）---")
#
# 列表推导式是 for 循环的"表达式版本"，更简洁。
# 语法：[表达式 for 变量 in 可迭代对象 if 条件]

# 基础：生成平方数
squares = [x ** 2 for x in range(1, 6)]
print(f"平方: {squares}")

# 带条件：过滤偶数
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"偶数: {evens}")

# 双重循环：扁平化
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(f"矩阵扁平化: {flat}")
# ↑ 等价于：
#   flat = []
#   for row in matrix:
#       for num in row:
#           flat.append(num)

# 带条件的三元表达式
parity = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(f"奇偶判断: {parity}")

# 字典推导式
square_dict = {x: x ** 2 for x in range(1, 6)}
print(f"字典推导式: {square_dict}")

# 集合推导式（去重）
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {x ** 2 for x in nums}
print(f"集合推导式（自动去重）: {unique_squares}")


# ---------------------------------------------------------------------------
# 1.7 循环的高级技巧与陷阱
# ---------------------------------------------------------------------------
print("\n--- 1.7 循环的高级技巧与陷阱 ---")

# --- 技巧 ①：用 for 循环实现 do-while ---
# Python 没有 do-while 语法，可以用 while True + break 模拟
print("【模拟 do-while 循环】")
n = 0
while True:
    n += 1
    print(f"  {n}", end="  ")
    if n >= 3:
        break  # 至少执行一次后才检查条件
print("  (至少执行了一次)")

# --- 技巧 ②：用 for 一次遍历多个迭代器（itertools.chain）---
from itertools import chain
print("\n【itertools.chain — 串联多个可迭代对象】")
combined = list(chain([1, 2], [3, 4], "ab"))
print(f"  chain([1,2], [3,4], 'ab') → {combined}")

# --- 技巧 ③：itertools.product — 多层嵌套的扁平写法 ---
from itertools import product
print("\n【itertools.product — 替代多层嵌套循环】")
# 等价于两层 for 循环
for x, y in product([1, 2], ["a", "b"]):
    print(f"  ({x}, {y})", end="  ")
print()

# --- 陷阱 ①：遍历列表时不要删除元素 ---
print("\n【⚠️ 陷阱：遍历时删除元素会出问题】")
nums = [1, 2, 3, 4, 5, 6]
# ❌ 错误做法：边遍历边删除
# for n in nums:
#     if n % 2 == 0:
#         nums.remove(n)  # 索引会错乱！
# ✅ 正确做法：用列表推导式或倒序遍历
nums[:] = [n for n in nums if n % 2 != 0]  # 只保留奇数
print(f"  用推导式过滤后: {nums}")

# --- 陷阱 ②：修改循环变量不影响迭代 ---
print("\n【⚠️ 陷阱：修改循环变量不影响下一次迭代】")
lst = [1, 2, 3, 4, 5]
for x in lst:
    x = x * 10       # 这只改了临时变量 x，不改 lst
print(f"  修改 x 不影响原列表: {lst}")

# 如果想修改，需要用索引
for i in range(len(lst)):
    lst[i] *= 10
print(f"  通过索引修改: {lst}")


# ============================================================================
# 第二部分：函数（Functions）
# ============================================================================
# 函数是 Python 中组织代码的基本单元。
# 用 def 定义，可以有参数、返回值，支持多种参数传递方式。
# ============================================================================

print("\n" + "=" * 60)
print("🔧 第二部分：函数（Functions）基础与进阶")
print("=" * 60)


# ---------------------------------------------------------------------------
# 2.1 函数的定义与调用
# ---------------------------------------------------------------------------
print("\n--- 2.1 函数的定义与调用 ---")

# 基本语法：
#   def 函数名(参数列表):
#       """文档字符串"""
#       函数体
#       return 返回值

def greet(name):
    """向指定的人打招呼"""
    return f"你好，{name}！"

# 调用函数
result = greet("张三")
print(f"  greet('张三') → {result}")

# 没有 return 的函数返回 None
def say_hello(name):
    print(f"  你好，{name}！（没有 return）")

ret = say_hello("李四")
print(f"  返回值: {ret}")  # None


# ---------------------------------------------------------------------------
# 2.2 参数传递详解
# ---------------------------------------------------------------------------
print("\n--- 2.2 参数传递详解 ---")

# --- 2.2.1 位置参数 ---
# 按顺序传递，缺一不可
def student_info(name, age, city):
    """学生信息"""
    return f"{name}, {age}岁, 来自{city}"

print("【位置参数】")
print(f"  {student_info('小明', 18, '北京')}")


# --- 2.2.2 默认参数 ---
# 给参数指定默认值，调用时可以省略
print("\n【默认参数】")

def power(base, exp=2):
    """计算 base 的 exp 次方，默认平方"""
    return base ** exp

print(f"  power(3)     = {power(3)}")     # 3² = 9
print(f"  power(3, 4)  = {power(3, 4)}")  # 3⁴ = 81

# ⚠️ 默认参数的陷阱：不要用可变对象（列表、字典）作为默认值！
print("\n【⚠️ 默认参数的陷阱】")

def add_item(item, items=[]):   # ❌ 危险！默认列表只创建一次
    items.append(item)
    return items

print(f"  第一次: {add_item('a')}")    # ['a']
print(f"  第二次: {add_item('b')}")    # ['a', 'b'] → 不是 ['b']！
# 原因：默认参数在函数定义时只创建一次，后续调用共用同一个列表

# ✅ 正确做法：用 None 作为默认值，内部再创建
def add_item_safe(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(f"  安全版第一次: {add_item_safe('a')}")    # ['a']
print(f"  安全版第二次: {add_item_safe('b')}")    # ['b'] ✅


# --- 2.2.3 关键字参数 ---
# 通过参数名传递，顺序无关
print("\n【关键字参数】")
print(f"  {student_info(city='上海', name='小红', age=20)}")


# --- 2.2.4 强制关键字参数（Python 3+）---
# * 后面的参数必须以关键字形式传递
print("\n【强制关键字参数】")

def connect(host, port, *, timeout=30, ssl=True):
    """连接服务器（timeout 和 ssl 必须用关键字指定）"""
    return f"连接 {host}:{port} (timeout={timeout}, ssl={ssl})"

print(f"  {connect('localhost', 8080)}")
print(f"  {connect('localhost', 8080, timeout=60, ssl=False)}")
# connect('localhost', 8080, 60)  # ❌ 会报错！timeout 是强制关键字参数


# --- 2.2.5 可变位置参数 *args ---
# *args 收集所有额外的位置参数为一个元组
print("\n【*args — 可变位置参数】")

def sum_all(*args):
    """接收任意数量的参数并求和"""
    print(f"  接收到的参数元组: {args}")
    return sum(args)

print(f"  sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"  sum_all(5, 10, 15, 20) = {sum_all(5, 10, 15, 20)}")

# 解包列表/元组作为参数
nums = [1, 2, 3, 4, 5]
print(f"  sum_all(*nums) = {sum_all(*nums)}")  # * 解包


# --- 2.2.6 可变关键字参数 **kwargs ---
# **kwargs 收集所有额外的关键字参数为一个字典
print("\n【**kwargs — 可变关键字参数】")

def print_config(**kwargs):
    """打印配置项"""
    print(f"  接收到的关键字参数字典: {kwargs}")
    for key, value in kwargs.items():
        print(f"    {key} = {value}")

print_config(db="mysql", host="localhost", port=3306, debug=True)

# 解包字典作为参数
config = {"host": "127.0.0.1", "port": 8080}
print_config(**config, debug=False)  # ** 解包字典


# --- 2.2.7 参数传递顺序 ---
print("\n【参数传递顺序（完整版）】")
#
# 定义一个函数同时使用所有类型的参数：
def func(a, b, c=3, *args, d, **kwargs):
#      ↑  ↑  ↑      ↑     ↑    ↑
#      位置 位置 默认   *收集  强制关键字 **收集
#      (必填)        额外位置         额外关键字
    print(f"  a={a}, b={b}, c={c}")
    print(f"  args={args}")
    print(f"  d={d}（强制关键字）")
    print(f"  kwargs={kwargs}")

print("调用: func(1, 2, 4, 5, 6, d=7, e=8, f=9)")
func(1, 2, 4, 5, 6, d=7, e=8, f=9)
# 解释：
#   1  → a
#   2  → b
#   4  → c（覆盖默认值 3）
#   5, 6 → args（被 * 收集）
#   d=7 → d（强制关键字参数）
#   e=8, f=9 → kwargs（被 ** 收集）
#


# ---------------------------------------------------------------------------
# 2.3 返回值
# ---------------------------------------------------------------------------
print("\n--- 2.3 返回值 ---")

# --- 返回单个值 ---
def add(a, b):
    return a + b

# --- 返回多个值（实际是元组）---
def min_max(lst):
    """返回列表的最小值和最大值"""
    return min(lst), max(lst)   # 返回元组

low, high = min_max([3, 1, 4, 1, 5, 9])
print(f"min_max([3,1,4,1,5,9]) → 最小值={low}, 最大值={high}")

# --- 提前 return ---
def divide(a, b):
    """安全的除法"""
    if b == 0:
        return None   # 提前返回
    return a / b

print(f"  divide(10, 2) = {divide(10, 2)}")
print(f"  divide(10, 0) = {divide(10, 0)}")


# ---------------------------------------------------------------------------
# 2.4 变量作用域 —— LEGB 规则
# ---------------------------------------------------------------------------
print("\n--- 2.4 变量作用域（LEGB 规则）---")
#
# Python 查找变量时遵循：Local → Enclosing → Global → Built-in
# （局部 → 外层 → 全局 → 内置）

# 全局变量
global_var = "我是全局变量"

def scope_demo():
    # 外层变量（Enclosing）
    outer_var = "我是外层变量"

    def inner():
        # 局部变量（Local）
        inner_var = "我是内层局部变量"
        print(f"  内层可访问 global_var: {global_var}")
        print(f"  内层可访问 outer_var: {outer_var}")
        print(f"  内层可访问 inner_var: {inner_var}")
    
    inner()

scope_demo()

# global 关键字：在函数内修改全局变量
print("\n【global 关键字】")
count = 0

def increment():
    global count   # 声明要修改全局变量 count
    count += 1

increment()
increment()
print(f"  调用 increment() 两次后 count = {count}")

# nonlocal 关键字：在嵌套函数中修改外层变量
print("\n【nonlocal 关键字】")

def make_counter():
    counter = 0
    def increment():
        nonlocal counter   # 声明要修改外层变量
        counter += 1
        return counter
    return increment

my_counter = make_counter()
print(f"  第一次调用: {my_counter()}")
print(f"  第二次调用: {my_counter()}")
print(f"  第三次调用: {my_counter()}")


# ---------------------------------------------------------------------------
# 2.5 匿名函数 —— lambda
# ---------------------------------------------------------------------------
print("\n--- 2.5 匿名函数 lambda ---")
#
# 📌 什么是 lambda？
#
# lambda 是 Python 中创建"匿名函数"的关键字 —— 即没有名字的函数。
# 适用于只需要用一次的简单逻辑，不用 def 专门定义一个函数。
#
# 语法：
#   lambda 参数1, 参数2, ...: 表达式
#      ↑                      ↑
#   和 def 一样            只能写一个表达式（不能写语句）
#                         自动 return 这个表达式的结果
#
# ┌─────────────────────────────────────────────────────┐
# │  def 版                            lambda 版        │
# │  ───────                            ─────────       │
# │  def square(x):         ←→          square =        │
# │      return x ** 2                  lambda x: x**2  │
# │                                                    │
# │  特点：                         特点：              │
# │  · 有名字                        · 匿名（没名字）    │
# │  · 可以写多行                    · 只能一行表达式    │
# │  · 有显式 return                 · 隐式 return      │
# │  · 可写任意语句                  · 只能用表达式      │
# └─────────────────────────────────────────────────────┘

# ===== ① 基础语法：lambda vs def =====
print("【① lambda vs def — 等价的两种写法】")

# def 写法
def add_def(a, b):
    return a + b

# lambda 写法（一行搞定）
add_lambda = lambda a, b: a + b

print(f"  def 版:       add_def(3, 5) = {add_def(3, 5)}")
print(f"  lambda 版:    add_lambda(3, 5) = {add_lambda(3, 5)}")

# lambda 可以不赋值给变量，直接使用（这才是"匿名"的本意）
print(f"  直接使用:     (lambda a, b: a + b)(3, 5) = {(lambda a, b: a + b)(3, 5)}")

print()
# ===== ② 适用场景一：sorted() 的 key 参数 =====
print("【② 场景：sorted() 排序】")
#
# sorted() 的 key 参数需要一个"函数"来告诉它按什么规则排序。
# 这种临时用一次的函数，最适合用 lambda。

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95},
]

# 按分数降序排序
sorted_by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"  按分数排序: {[s['name'] for s in sorted_by_score]}")

# 按名字长度排序
sorted_by_name_len = sorted(students, key=lambda s: len(s["name"]))
print(f"  按名字长度: {[s['name'] for s in sorted_by_name_len]}")

# 多维排序：（先按分数降序，同分按名字字母序）
sorted_multi = sorted(students, key=lambda s: (-s["score"], s["name"]))
print(f"  多维排序:   {[(s['name'], s['score']) for s in sorted_multi]}")

print()
# ===== ③ 场景：max() / min() 的自定义规则 =====
print("【③ 场景：max() / min() 自定义比较规则】")

words = ["apple", "banana", "cherry", "date"]
# 找出"长度最长"的单词
longest = max(words, key=lambda w: len(w))
print(f"  最长的单词: {longest}")  # banana（6个字符）

# 找出"元音字母最多"的单词
most_vowels = max(words, key=lambda w: sum(1 for c in w if c in "aeiou"))
print(f"  元音最多的: {most_vowels}")  # banana（3个元音）

print()
# ===== ④ 场景：map() — 批量转换 =====
print("【④ 场景：map() — 批量转换】")
#
# map(func, iterable) 对每个元素应用 func
nums = [1, 2, 3, 4, 5]

# ❌ 不用 map 的写法
doubled_manual = []
for n in nums:
    doubled_manual.append(n * 2)

# ✅ 用 map + lambda 的写法
doubled = list(map(lambda x: x * 2, nums))
print(f"  每个元素×2: {doubled}")

# 多个列表输入：两个列表对应元素相加
a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(f"  两两相加:    {summed}")

print()
# ===== ⑤ 场景：filter() — 按条件过滤 =====
print("【⑤ 场景：filter() — 按条件过滤】")
#
# filter(func, iterable) 保留 func 返回 True 的元素
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"  过滤出偶数:  {evens}")

# 过滤出长度 >= 6 的单词
long_words = list(filter(lambda w: len(w) >= 6, words))
print(f"  长单词:      {long_words}")

print()
# ===== ⑥ 场景：reduce() — 累计运算 =====
print("【⑥ 场景：reduce() — 累计运算】")
#
# reduce(func, iterable) 从左到右累计运算
from functools import reduce

# 累加
total = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print(f"  累加 1~5:    {total}")

# 累乘（计算阶乘）
product = reduce(lambda a, b: a * b, range(1, 6))
print(f"  累乘 1~5:    {product}")

# 找出最大值
max_val = reduce(lambda a, b: a if a > b else b, [3, 7, 2, 9, 5])
print(f"  reduce 找最大: {max_val}")

print()
# ===== ⑦ lambda 的局限 =====
print("【⑦ lambda 的局限】")
#
# lambda 只能写一个表达式，不能写赋值、循环、return 等语句。
# 如果逻辑复杂，应该用 def。

# ❌ 下面这些都做不到：
#   lambda x: if x > 0: return x   # 不能用 if 语句
#   lambda x: for i in x: ...      # 不能用循环
#
# ✅ 但可以用"条件表达式"（三元表达式）：
abs_lambda = lambda x: x if x >= 0 else -x
print(f"  绝对值:      lambda x: x if x>=0 else -x")
print(f"    abs_lambda(5) = {abs_lambda(5)}")
print(f"    abs_lambda(-3) = {abs_lambda(-3)}")

# 多个条件判断可以用 and/or 技巧，但可读性差 → 建议用 def
# lambda x: x > 0 and "正数" or x < 0 and "负数" or "零"

print()
# ===== ⑧ lambda 的注意事项 =====
print("【⑧ ⚠️ lambda 的注意事项】")
#
# 陷阱：lambda 在循环中捕获变量时要注意！

# ❌ 常见错误：所有 lambda 都使用循环结束后的变量值
funcs = []
for i in range(5):
    funcs.append(lambda: i)  # 这里 i 是引用，不是当前值
print(f"  ❌ 循环中的 lambda:")
for f in funcs:
    print(f"    f() = {f()}", end="  ")
print("  (全是 4！)")  # 都返回 4，因为 i 最终是 4

# ✅ 修正：用默认参数捕获当前值
funcs2 = []
for i in range(5):
    funcs2.append(lambda x=i: x)  # x=i 把当前 i 作为默认值
print(f"  ✅ 用默认参数修正:")
for f in funcs2:
    print(f"    f() = {f()}", end="  ")
print()

print()
# ===== ⑨ 何时该用 / 不该用 lambda =====
print("【⑨ 使用建议：何时用 lambda？】")
suggestions = [
    ("✅ 推荐用 lambda",
     "作为 sorted()/map()/filter()/max() 等函数的 key 或 func 参数"),
    ("✅ 推荐用 lambda",
     "临时用一次的简单运算（一行表达式能写完）"),
    ("❌ 不该用 lambda",
     "逻辑超过一行 → 用 def 提高可读性"),
    ("❌ 不该用 lambda",
     "需要重复调用 → 用 def 命名更清晰"),
]
for usage, reason in suggestions:
    print(f"  {usage}")
    print(f"    原因: {reason}")


# ---------------------------------------------------------------------------
# 2.6 高阶函数 —— 函数作为参数或返回值
# ---------------------------------------------------------------------------
print("\n--- 2.6 高阶函数 ---")

# 函数可以像普通变量一样传递

def apply_twice(func, value):
    """对 value 应用 func 两次"""
    return func(func(value))

result = apply_twice(lambda x: x + 1, 5)
print(f"  apply_twice(lambda x: x+1, 5) = {result}")  # 5+1+1 = 7

# 函数可以返回函数
def make_multiplier(n):
    """创建一个乘以 n 的函数"""
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")


# ---------------------------------------------------------------------------
# 2.7 装饰器 —— 在不修改函数的前提下增强功能
# ---------------------------------------------------------------------------
print("\n--- 2.7 装饰器（Decorators）---")
#
# 装饰器本质上是一个接受函数并返回新函数的高阶函数。
# 语法糖：@decorator_name

# 基础装饰器：计算函数执行时间
def timer(func):
    """装饰器：打印函数执行时间"""
    @wraps(func)  # 保持原函数的元信息（名字、文档等）
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  ⏱ {func.__name__} 耗时: {elapsed:.6f} 秒")
        return result
    return wrapper

# 使用装饰器
@timer
def slow_sum(n):
    """计算 1~n 的和（模拟耗时操作）"""
    total = 0
    for i in range(n):
        total += i
    return total

result = slow_sum(1000000)
print(f"  slow_sum(1000000) = {result}")

# 多层装饰器
print("\n【多层装饰器】")

def bold(func):
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"*{func(*args, **kwargs)}*"
    return wrapper

@bold
@italic
def say(text):
    return text

# 等价于 bold(italic(say))
print(f"  @bold @italic say('Hello') → {say('Hello')}")

# 带参数的装饰器
print("\n【带参数的装饰器】")

def repeat(times):
    """装饰器工厂：让函数重复执行 times 次"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet_alice():
    print("  你好 Alice！")

print("  @repeat(times=3) 调用 greet_alice():")
greet_alice()


# ---------------------------------------------------------------------------
# 2.8 递归函数
# ---------------------------------------------------------------------------
print("\n--- 2.8 递归函数 ---")
#
# 递归 = 函数调用自身
# 必须要有：终止条件 + 递归调用

def factorial(n):
    """计算 n!（阶乘）"""
    if n <= 1:          # 终止条件
        return 1
    return n * factorial(n - 1)  # 递归调用

print(f"  5! = {factorial(5)}")   # 5×4×3×2×1 = 120

def fibonacci(n):
    """斐波那契数列第 n 项（带缓存优化）"""
    cache = {0: 0, 1: 1}
    def _fib(n):
        if n in cache:
            return cache[n]
        cache[n] = _fib(n - 1) + _fib(n - 2)
        return cache[n]
    return _fib(n)

print(f"  fibonacci(10) = {fibonacci(10)}")
print(f"  fibonacci(50) = {fibonacci(50)}")  # 没有缓存会非常慢

# 递归的局限：Python 默认递归深度限制约 1000
print(f"\n  Python 最大递归深度: {sys.getrecursionlimit()}")


# ---------------------------------------------------------------------------
# 2.9 生成器 —— yield 关键字
# ---------------------------------------------------------------------------
print("\n--- 2.9 生成器（Generator）与 yield ---")
#
# 生成器是"惰性求值"的函数，每次 yield 返回一个值，下次继续执行。

def count_up_to(n):
    """生成器：从 1 数到 n"""
    i = 1
    while i <= n:
        yield i   # 返回 i，但函数不会退出，下次从这继续
        i += 1

print("【基础生成器】")
counter = count_up_to(5)
print(f"  类型: {type(counter)}")
for num in counter:
    print(f"  {num}", end="  ")
print()

# 生成器 vs 列表 — 内存对比
print("\n【生成器 vs 列表 — 内存效率】")
# 列表推导式：一次性生成所有元素
list_squares = [x ** 2 for x in range(10)]
print(f"  列表推导式: {list_squares}")
print(f"  占用内存: {sys.getsizeof(list_squares)} 字节")

# 生成器表达式：逐个生成元素
gen_squares = (x ** 2 for x in range(10))
print(f"  生成器表达式: {gen_squares}")
print(f"  占用内存: {sys.getsizeof(gen_squares)} 字节")
for val in gen_squares:
    print(f"  {val}", end="  ")
print()

# yield from —— 委托给另一个可迭代对象
print("\n【yield from — 扁平化嵌套列表】")

def flatten(nested):
    """扁平化嵌套列表"""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # 递归委托
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]]]
print(f"  嵌套列表: {nested}")
print(f"  扁平化后: {list(flatten(nested))}")


# ---------------------------------------------------------------------------
# 2.10 函数式编程工具
# ---------------------------------------------------------------------------
print("\n--- 2.10 函数式编程工具 ---")

# --- map —— 批量转换 ---
print("【map — 批量转换】")
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(f"  map(平方): {squared}")

# 多个输入列表
a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(f"  map(两两相加): {summed}")

# --- filter —— 按条件过滤 ---
print("\n【filter — 按条件过滤】")
filtered = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6]))
print(f"  filter(>3): {filtered}")

# --- reduce —— 累计运算 ---
print("\n【reduce — 累计运算】")
total = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print(f"  reduce(累加): {total}")

# --- partial —— 冻结部分参数 ---
print("\n【partial — 偏函数（冻结参数）】")
#
# partial(func, *args, **kwargs) 的作用：
#   "冻结" func 的部分参数，创建一个参数更少的新函数。
#
#   就像做汉堡 —— 提前把"生菜"和"番茄"夹好，
#   之后每次只需要说"加牛肉"就行了。
#

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)      # 固定 exp=2 → 变成"平方函数"
cube = partial(power, exp=3)        # 固定 exp=3 → 变成"立方函数"
print(f"  square(5) = {square(5)}")  # 25
print(f"  cube(5) = {cube(5)}")      # 125
# ↑ 等价于 power(5, exp=2) 和 power(5, exp=3)

# ===== 实际应用：int() 的 base 参数 =====
print('\n【实际应用：用 partial 创建"二进制转十进制"函数】')
#
# int() 的完整签名是：int(x, base=10)
#   - int("1010")        → 1010     （按十进制解析）
#   - int("1010", base=2) → 10      （按二进制解析）
#
# 问题：每次都要写 base=2 很麻烦
# 解决：用 partial "冻结" base 参数
#

int_base2 = partial(int, base=2)
# ↑ 等价于定义了一个新函数：
#   def int_base2(x):
#       return int(x, base=2)

print(f"  普通 int('1010')        = {int('1010')}")
print(f"  int('1010', base=2)     = {int('1010', base=2)}")
print(f"  int_base2('1010')       = {int_base2('1010')}")
print(f"  int_base2('1111')       = {int_base2('1111')}")  # 15
print(f"  int_base2('10000000')   = {int_base2('10000000')}")  # 128

# 还可以再创建十六进制版
int_base16 = partial(int, base=16)
print(f"  int_base16('FF')        = {int_base16('FF')}")    # 255
print(f"  int_base16('A')         = {int_base16('A')}")     # 10


# ---------------------------------------------------------------------------
# 2.11 类型注解（Type Hints）
# ---------------------------------------------------------------------------
print("\n--- 2.11 类型注解（Type Hints）---")
#
# Python 3.5+ 支持类型注解，提高代码可读性（不影响运行）

from typing import List, Tuple, Optional, Dict

def calculate_bmi(weight: float, height: float) -> Optional[float]:
    """计算 BMI（体重/身高²），带类型注解"""
    if height <= 0:
        return None
    return round(weight / (height ** 2), 1)

def filter_adults(people: List[Dict[str, object]]) -> List[Dict[str, object]]:
    """过滤成年人的列表"""
    return [p for p in people if p.get("age", 0) >= 18]

# 调用时类型注解不会强制检查，但 IDE 会给出提示
bmi = calculate_bmi(70, 1.75)
print(f"  体重70kg, 身高1.75m → BMI = {bmi}")


# ============================================================================
# 第三部分：综合练习
# ============================================================================

print("\n" + "=" * 60)
print("🧩 第三部分：综合练习 — 管道处理（Pipeline）")
print("=" * 60)


def pipeline_demo():
    """
    综合运用函数和循环，实现一个数据处理管道。

    场景：从原始数据 → 清洗 → 转换 → 过滤 → 统计
    """
    # ---------- 原始数据 ----------
    raw_data = [
        "  alice,85,90,78  ",
        "bob,72,65,58",
        "  charlie,95,90,92",
        "",                    # 空行
        "  diana,60,55,70 ",
        "  eve,abc,80,90",    # 脏数据
        " frank,,80,75",      # 脏数据
        "  ",                  # 空白行
    ]

    print("原始数据:")
    for line in raw_data:
        print(f"  {repr(line)}")

    # ---------- 定义处理步骤（每个步骤是一个函数）----------
    def step1_strip(lines):
        """步骤1：去除每行首尾空白"""
        return (line.strip() for line in lines)  # 生成器，惰性处理

    def step2_remove_empty(lines):
        """步骤2：移除空行"""
        return (line for line in lines if line)

    def step3_split(lines):
        """步骤3：按逗号分割为列表"""
        for line in lines:
            yield line.split(",")

    def step4_validate(records):
        """步骤4：校验数据有效性（需要3个数字类型的成绩）"""
        for record in records:
            if len(record) != 4:
                continue  # 字段数不对
            name, *score_strs = record
            try:
                scores = [int(s) for s in score_strs]
                yield name.strip(), scores
            except ValueError:
                continue  # 成绩不是有效数字

    def step5_calc_average(records):
        """步骤5：计算平均分"""
        for name, scores in records:
            avg = sum(scores) / len(scores)
            yield name, scores, avg

    def step6_filter(records, min_avg=60):
        """步骤6：过滤掉不及格的学生"""
        return (r for r in records if r[2] >= min_avg)

    # ---------- 组装管道 ----------
    print("\n处理管道:")

    # 管道：原始数据 → 修整 → 去空 → 分割 → 校验 → 算平均 → 过滤
    pipeline = step6_filter(
        step5_calc_average(
            step4_validate(
                step3_split(
                    step2_remove_empty(
                        step1_strip(raw_data)
                    )
                )
            )
        ),
        min_avg=60
    )

    # ---------- 执行管道并输出结果 ----------
    print(f"{'姓名':<10} {'成绩':<20} {'平均分':<8}")
    print("-" * 40)
    for name, scores, avg in pipeline:
        print(f"{name:<10} {str(scores):<20} {avg:<8.1f}")

    # ---------- 统计总结 ----------
    # 注意：pipeline 已被消费完，需要重新创建
    all_records = list(
        step5_calc_average(
            step4_validate(
                step3_split(
                    step2_remove_empty(
                        step1_strip(raw_data)
                    )
                )
            )
        )
    )

    print("\n📊 统计汇总:")
    print(f"  总记录数: {len(all_records)}")
    averages = [avg for _, _, avg in all_records]
    if averages:
        print(f"  最高平均分: {max(averages):.1f}")
        print(f"  最低平均分: {min(averages):.1f}")
        print(f"  全班平均分: {sum(averages) / len(averages):.1f}")

    return all_records


pipeline_demo()


# ============================================================================
# 第四部分：常见陷阱与最佳实践总结
# ============================================================================

print("\n" + "=" * 60)
print("💡 第四部分：常见陷阱与最佳实践总结")
print("=" * 60)

traps_and_tips = [
    ("默认参数陷阱",
     "不要用可变对象（[]/{}）做默认参数，改用 None + 内部判断"),
    ("循环修改列表",
     "遍历时不要增删元素，改用列表推导式或倒序遍历"),
    ("for-else 含义",
     "else 表示'没有被 break'，不是'循环结束'"),
    ("变量作用域",
     "内层修改外层变量用 nonlocal，修改全局用 global"),
    ("*args 和 **kwargs",
     "* 收集位置参数为元组，** 收集关键字参数为字典"),
    ("递归深度限制",
     "默认约 1000 层，深递归改迭代或设置 sys.setrecursionlimit()"),
    ("生成器一次性",
     "生成器只能遍历一次，需要多次使用请转为列表"),
    ("装饰器保留元信息",
     "自定义装饰器加上 @functools.wraps(func)"),
    ("is 和 == 区别",
     "is 比较内存地址，== 比较值"),
]

for i, (title, tip) in enumerate(traps_and_tips, 1):
    print(f"  {i}. {title}")
    print(f"     {tip}")
    print()

print("=" * 60)
print("✅ 练习脚本运行完毕！希望你有所收获 🚀")
print("=" * 60)
