#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn 数据可视化入门练习脚本（seaborn_demo.py）

本脚本演示如何使用 Seaborn 对 CSV 数据进行可视化分析，
并与 Matplotlib 写法进行对比，帮助理解 Seaborn 的优势。

学习目标：
  1. 理解 Seaborn 与 Matplotlib 的关系（Seaborn 封装了 Matplotlib）
  2. 掌握 Seaborn 核心图表函数的一行调用
  3. 学会用 hue/col/row 参数实现分组可视化
  4. 了解 Seaborn 特有的统计图表类型

对比 Matplotlib：
  Matplotlib:  "乐高积木"—— 自由度高，但砌得慢
  Seaborn:     "预制模块"—— 功能固定，但出图快

运行方式：python3 seaborn_demo.py
生成的图表保存在 images/ 文件夹中，文件名为 sns_*.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ============================================================================
# 准备工作：读取数据（用 Pandas，Seaborn 原生支持）
# ============================================================================
#
# Seaborn 的函数通常要求数据以 "长格式"（long-form）传入，
# 即 DataFrame 形式：每行一条记录，每列一个变量。
# Pandas 的 DataFrame 正是为此而生。
#
print("正在读取 CSV 数据...")
import pandas as pd

CSV_FILE = Path(__file__).parent / "social_media_addiction_mental_wellbeing.csv"
OUTPUT_DIR = Path(__file__).parent / "images"
OUTPUT_DIR.mkdir(exist_ok=True)

# 用 Pandas 读取，Seaborn 可以直接使用 DataFrame
df = pd.read_csv(CSV_FILE)
print(f"共读取 {len(df)} 条记录\n")
print(f"列名:\n{list(df.columns)}\n")

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Serif CJK SC", "Droid Sans Fallback", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
sns.set_theme(style="whitegrid", font="Noto Sans CJK SC")  # Seaborn 主题设置

# ============================================================================
# 第一部分：Seaborn vs Matplotlib —— 代码量对比
# ============================================================================
print("=" * 60)
print("📊 第一部分：Seaborn vs Matplotlib 对比")
print("=" * 60)

# ---------------------------------------------------------------------------
# 对比 ①：柱状图
# ---------------------------------------------------------------------------
print("\n--- 对比 ①：柱状图 — 按成瘾级别统计人数 ---")

# Matplotlib 写法（参考 matplotlib_demo.py）
#   counts = [420, 450, ...]
#   ax.bar(labels, counts)
#   for bar, count in zip(bars, counts):
#       ax.text(...)
#   ax.set_title(...)  等等 ≈ 15 行

# Seaborn 写法（只需一行核心代码！）
# 注意：palette + hue 同时使用是新版 Seaborn 的推荐写法
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x="Addiction_Level",
              hue="Addiction_Level",          # ← 新版要求 palette 必须搭配 hue
              order=["Low", "Moderate", "High", "Severe"],
              palette=["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"],
              legend=False,                  # ← x 和 hue 相同，图例无意义
              ax=ax)
ax.set_title("各成瘾级别用户分布（Seaborn）", fontsize=14, fontweight="bold")
ax.set_xlabel("成瘾级别")
ax.set_ylabel("人数")

# 在柱子上方显示具体数字
for p in ax.containers[0]:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, height + 5,
            str(int(height)), ha="center", va="bottom", fontsize=11)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_01_countplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_01_countplot.png  (1 行核心代码 vs Matplotlib 15 行)")

# ---------------------------------------------------------------------------
# 对比 ②：箱线图
# ---------------------------------------------------------------------------
print("\n--- 对比 ②：箱线图 — 各成瘾级别的心理健康评分 ---")

# Matplotlib 写法：
#   box_data = [...]
#   bp = ax.boxplot(box_data, patch_artist=True)
#   ax.set_xticklabels(labels)
#   for patch, color in zip(bp["boxes"], colors):
#       patch.set_facecolor(color)   ≈ 12 行

# Seaborn 写法：
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="Addiction_Level", y="Mental_Wellbeing_Score",
            hue="Addiction_Level",
            order=["Low", "Moderate", "High", "Severe"],
            palette=["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"],
            legend=False,
            ax=ax)
ax.set_title("不同成瘾级别的心理健康评分分布（Seaborn）", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_02_boxplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_02_boxplot.png  (1 行核心代码 vs Matplotlib 12 行)")


# ============================================================================
# 第二部分：Seaborn 核心图表
# ============================================================================
print("\n" + "=" * 60)
print("🎨 第二部分：Seaborn 核心图表")
print("=" * 60)

# ---------------------------------------------------------------------------
# 图 1：直方图 + 核密度曲线 (histplot)
# ---------------------------------------------------------------------------
print("\n📊 图 1：直方图 + 核密度曲线 — 年龄分布")

fig, ax = plt.subplots(figsize=(8, 5))

# Seaborn 的 histplot 自带密度曲线选项
sns.histplot(data=df, x="Age", bins=15, kde=True,   # kde=True 叠加密度曲线
             color="#3498db", edgecolor="white", ax=ax)

ax.axvline(df["Age"].mean(), color="#e74c3c", linestyle="--",
           linewidth=2, label=f"平均年龄: {df['Age'].mean():.1f} 岁")
ax.set_title("用户年龄分布（含核密度曲线）", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_03_histplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_03_histplot.png")

# ---------------------------------------------------------------------------
# 图 2：小提琴图 (violinplot) —— 箱线图的升级版
# ---------------------------------------------------------------------------
print("\n📊 图 2：小提琴图 — 各成瘾级别的心理健康评分分布")
#
# 小提琴图 = 箱线图 + 密度分布
# 宽度越宽 → 该评分的人数越多

fig, ax = plt.subplots(figsize=(8, 5))
sns.violinplot(data=df, x="Addiction_Level", y="Mental_Wellbeing_Score",
               hue="Addiction_Level",
               order=["Low", "Moderate", "High", "Severe"],
               palette=["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"],
               legend=False,
               inner="quartile",    # 内部显示四分位数（替代箱线）
               ax=ax)
ax.set_title("各成瘾级别的心理健康评分分布（小提琴图）", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_04_violinplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_04_violinplot.png")

# ---------------------------------------------------------------------------
# 图 3：散点图 + 回归线 (regplot / lmplot)
# ---------------------------------------------------------------------------
print("\n📊 图 3：散点图 + 回归线 — 使用时长 vs 心理健康评分")

fig, ax = plt.subplots(figsize=(8, 5))

# regplot = 散点图 + 自动线性回归拟合
sns.regplot(data=df, x="Daily_Usage_Hours", y="Mental_Wellbeing_Score",
            scatter_kws={"alpha": 0.3, "s": 10, "color": "#3498db"},
            line_kws={"color": "#e74c3c", "linewidth": 2},
            ax=ax)

# 计算相关系数（与 numpy_demo.py 中的结果对比）
corr = df["Daily_Usage_Hours"].corr(df["Mental_Wellbeing_Score"])
ax.text(0.95, 0.05, f"相关系数 r = {corr:.3f}", transform=ax.transAxes,
        ha="right", va="bottom", fontsize=12,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

ax.set_title("每日使用时长 vs 心理健康评分（含回归线）", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_05_regplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_05_regplot.png")

# ---------------------------------------------------------------------------
# 图 4：热力图 (heatmap) —— 相关性矩阵可视化
# ---------------------------------------------------------------------------
print("\n📊 图 4：热力图 — 各指标相关性矩阵")

# 选取数值列
numeric_cols = [
    "Age", "Daily_Usage_Hours", "Notifications_Per_Day",
    "Anxiety_Score", "Depression_Score", "Sleep_Hours",
    "Mental_Wellbeing_Score"
]
corr_matrix = df[numeric_cols].corr()  # Pandas 的 corr() 自动计算相关系数矩阵

fig, ax = plt.subplots(figsize=(9, 7))

# 中文列名映射
col_names_cn = {
    "Age": "年龄", "Daily_Usage_Hours": "每日使用时长",
    "Notifications_Per_Day": "每日通知数", "Anxiety_Score": "焦虑评分",
    "Depression_Score": "抑郁评分", "Sleep_Hours": "睡眠时长",
    "Mental_Wellbeing_Score": "心理健康评分"
}
corr_matrix_cn = corr_matrix.rename(index=col_names_cn, columns=col_names_cn)

# heatmap — 用颜色深浅表示相关性大小
sns.heatmap(corr_matrix_cn,
            annot=True,           # 在格子中显示数值
            fmt=".2f",            # 数值格式
            cmap="RdBu_r",        # 颜色方案（红蓝渐变）
            center=0,             # 中间值（白色对应 0）
            vmin=-1, vmax=1,      # 取值范围 -1~1
            square=True,          # 正方形格子
            linewidths=0.5,       # 格子间隔
            cbar_kws={"shrink": 0.8, "label": "相关系数"},# 颜色条的设置
            ax=ax)                   # 画在哪个坐标轴上

ax.set_title("各指标相关性矩阵热力图", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_06_heatmap.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_06_heatmap.png")

# ---------------------------------------------------------------------------
# 图 5：分类散点图 (stripplot / swarmplot) 叠加箱线图
# ---------------------------------------------------------------------------
print("\n📊 图 5：分类散点图 + 箱线图 — 各平台的焦虑评分分布")

fig, ax = plt.subplots(figsize=(10, 5))

# 先画箱线图作为背景
#
# sns.boxplot() 参数详解：
#
#   data=df              → 数据源：Pandas DataFrame
#   x="Primary_Platform" → x 轴：按平台类别分组
#   y="Anxiety_Score"    → y 轴：每个组的焦虑评分数值
#                          箱线图会自动统计每组数据的：
#                          上边缘、下边缘、Q1(25%)、中位数(50%)、Q3(75%)、异常值
#   hue="Primary_Platform" → 按平台不同着色（新版要求 palette 必须搭配 hue）
#   palette="Set3"       → 颜色方案：Set3 是一组柔和的配色，
#                          也可用 "Set2"、"pastel"、"muted" 等
#   width=0.5            → 箱子的宽度（0~1，越大越宽）
#   legend=False         → 是否显示图例（因为 x 和 hue 都是平台，图例重复了）
#   ax=ax                → 画到哪个坐标轴上
#
sns.boxplot(data=df, x="Primary_Platform", y="Anxiety_Score",
            hue="Primary_Platform", palette="Set3", width=0.5,
            legend=False, ax=ax)

# 再叠加 stripplot 显示每个数据点
#
# sns.stripplot() 参数详解：
#
#   data=df              → 数据源：Pandas DataFrame
#   x="Primary_Platform" → x 轴：按平台类别分组
#   y="Anxiety_Score"    → y 轴：每个数据点的焦虑评分值
#                           stripplot 会把每个数据点都画出来
#                           可以看到数据的实际分布密度
#   color="#2c3e50"      → 点的颜色（深灰蓝色）
#   alpha=0.3            → 点透明度（0~1，越小越透明）
#                          大量数据叠加时用低透明度可以避免重叠遮挡
#   size=3               → 点的大小（数值越大点越大）
#   jitter=True          → 是否添加随机抖动
#                          同一位置有多个点时，自动错开避免完全重叠
#                          True = 自动抖动宽度
#                          也可以指定数值如 jitter=0.2 控制抖动幅度
#   ax=ax                → 画到哪个坐标轴上
#
# 为什么箱线图 + stripplot 叠加使用？
#   箱线图：展示统计分布（中位数、四分位、异常值）
#   stripplot：展示原始数据点（实际样本分布）
#   两者叠加 = 既看统计概览，又看原始数据，信息更完整
#
sns.stripplot(data=df, x="Primary_Platform", y="Anxiety_Score",
              color="#2c3e50", alpha=0.3, size=3, jitter=True, ax=ax)

ax.set_title("各平台焦虑评分分布（箱线图 + 数据点）", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_07_stripplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_07_stripplot.png")

# ---------------------------------------------------------------------------
# 图 6：配对图 (pairplot) —— 所有数值列两两对比
# ---------------------------------------------------------------------------
print("\n📊 图 6：配对图 — 所有数值列两两对比")
#
# pairplot 是 Seaborn 的"杀手级"功能：
#   对角线：显示每个变量的分布（直方图/密度图）
#   非对角线：显示两个变量的散点图
#   可以通过 hue 参数按类别着色

# 选取部分列，避免图太大
pair_cols = ["Age", "Daily_Usage_Hours", "Anxiety_Score", "Mental_Wellbeing_Score"]

# 用 hue 按 Addiction_Level 着色
#
# sns.pairplot() 参数详解：
#
#   data=df[pair_cols + ["Addiction_Level"]]
#                → 数据源：选取要分析的列 + 用于着色的类别列
#                   pairplot 会自动两两组合所有数值列
#   hue="Addiction_Level"
#                → 按成瘾级别着色，不同级别用不同颜色和标记
#                  在图例中可以区分不同组别的分布差异
#   palette={...}
#                → 自定义颜色映射：手动为每个类别指定颜色
#   diag_kind="kde"
#                → 对角线（每个变量自身的分布）用密度曲线
#                  可选: "hist" 直方图、"kde" 密度曲线、"auto" 自动
#   plot_kws={"alpha": 0.4, "s": 10}
#                → 控制散点图的样式
#                  alpha=0.4  点的透明度
#                  s=10       点的大小
#   height=2.5   → 每个子图的大小（英寸），数字越大图越大
#
# pairplot 的布局结构（以 4 个数值列为例）：
#
#            年龄    使用时长   焦虑评分  心理健康
#            ┌─────────────────────────────────┐
#    年龄    │ 密度曲线 │  散点图  │  散点图  │  散点图  │
#            ├─────────┼─────────┼─────────┼─────────┤
#  使用时长  │  散点图  │ 密度曲线 │  散点图  │  散点图  │
#            ├─────────┼─────────┼─────────┼─────────┤
#  焦虑评分  │  散点图  │  散点图  │ 密度曲线 │  散点图  │
#            ├─────────┼─────────┼─────────┼─────────┤
#  心理健康  │  散点图  │  散点图  │  散点图  │ 密度曲线 │
#            └─────────────────────────────────┘
#              对角线 = 自身分布   非对角线 = 两两散点图
#
pp = sns.pairplot(data=df[pair_cols + ["Addiction_Level"]],
                  hue="Addiction_Level",
                  palette={"Low": "#2ecc71", "Moderate": "#f39c12",
                           "High": "#e67e22", "Severe": "#e74c3c"},
                  diag_kind="kde",        # 对角线用密度曲线
                  plot_kws={"alpha": 0.4, "s": 10},
                  height=2.5)

pp.fig.suptitle("各指标配对分析（按成瘾级别着色）", fontsize=14, fontweight="bold", y=1.02)

pp.savefig(OUTPUT_DIR / "sns_08_pairplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_08_pairplot.png")

# ---------------------------------------------------------------------------
# 图 7：联合分布图 (jointplot) —— 散点 + 直方图组合
# ---------------------------------------------------------------------------
print("\n📊 图 7：联合分布图 — 每日通知数 vs 焦虑评分")

# jointplot 在一个图中同时展示：
#   - 中间：散点图（两个变量的关系）
#   - 上方：x 变量的分布（直方图）
#   - 右侧：y 变量的分布（直方图）
#
# sns.jointplot() 参数详解：
#
#   data=df              → 数据源：Pandas DataFrame
#   x="Notifications_Per_Day" → x 轴变量
#   y="Anxiety_Score"    → y 轴变量
#   kind="scatter"       → 中间图的类型
#                          "scatter" 散点图
#                          "hex"     六边形蜂窝图（数据量大时用）
#                          "kde"     密度等高线图
#                          "reg"     散点图 + 回归线
#   alpha=0.3            → 散点透明度
#   s=5                  → 散点大小
#   color="#9b59b6"      → 整体配色（紫色）
#   marginal_kws={"bins": 30, "alpha": 0.6}
#                → 边缘分布图的参数
#                  bins=30   直方图分成 30 个区间
#                  alpha=0.6 透明度
#
# jointplot 的布局结构：
#
#       ┌─────┬──────────────┐
#       │     │   x 的分布    │
#       │ 空  │  (直方图)     │
#       │     │              │
#       ├─────┼──────────────┤
#       │ y的 │              │
#       │ 分  │   中间图      │
#       │ 布  │  (散点图)     │
#       │ 直  │              │
#       │ 方  │              │
#       │ 图  │              │
#       └─────┴──────────────┘
#
jp = sns.jointplot(data=df, x="Notifications_Per_Day", y="Anxiety_Score",
                   kind="scatter",       # 中间图类型：scatter/hex/kde/reg
                   alpha=0.3, s=5,
                   color="#9b59b6",
                   marginal_kws={"bins": 30, "alpha": 0.6})

jp.fig.suptitle("每日通知数 vs 焦虑评分（联合分布）", fontsize=14, fontweight="bold", y=1.02)

# 计算相关系数
corr_na = df["Notifications_Per_Day"].corr(df["Anxiety_Score"])
jp.ax_joint.text(0.95, 0.05, f"r = {corr_na:.2f}", transform=jp.ax_joint.transAxes,
                 ha="right", va="bottom", fontsize=12,
                 bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

jp.savefig(OUTPUT_DIR / "sns_09_jointplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_09_jointplot.png")


# ============================================================================
# 第三部分：Seaborn 的 hue 分组魔法
# ============================================================================
print("\n" + "=" * 60)
print("🎯 第三部分：hue 参数 — 一键分组着色")
print("=" * 60)
#
# hue 是 Seaborn 最强大的参数 —— 按某个类别列自动分组并着色。
# 在 Matplotlib 中需要手写循环 + 手动配色的功能，在 Seaborn 中加一个参数就行。
#

print("\n📊 带 hue 的箱线图 — 按性别分组的成瘾级别分析")

fig, ax = plt.subplots(figsize=(10, 5))

#
# sns.boxplot() 参数详解（带 hue 版本）：
#
#   data=df                  → 数据源
#   x="Addiction_Level"      → x 轴：成瘾级别（分四组）
#   y="Mental_Wellbeing_Score" → y 轴：心理健康评分
#   hue="Gender"             → 按性别再分组（每个 x 组内再分 Male/Female/Non-binary）
#                              箱线图会为每个 (x, hue) 组合画一个箱子
#   order=["Low",...]        → x 轴类别的显示顺序
#   palette={...}            → 为 hue 的每个类别指定颜色
#   ax=ax                    → 画到哪个坐标轴上
#
sns.boxplot(data=df, x="Addiction_Level", y="Mental_Wellbeing_Score",
            hue="Gender",                        # ← 按性别分组
            order=["Low", "Moderate", "High", "Severe"],
            palette={"Male": "#3498db", "Female": "#e74c3c", "Non-binary": "#2ecc71"},
            ax=ax)

ax.set_title("各成瘾级别的心理健康评分（按性别分组）", fontsize=14, fontweight="bold")
ax.legend(title="性别", loc="lower left")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_10_hue_boxplot.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_10_hue_boxplot.png")

print("\n📊 带 hue 的散点图 — 按成瘾级别着色的使用时长分析")

fig, ax = plt.subplots(figsize=(8, 5))

#
# sns.scatterplot() 参数详解：
#
#   data=df                  → 数据源
#   x="Daily_Usage_Hours"    → x 轴：每日使用时长
#   y="Mental_Wellbeing_Score" → y 轴：心理健康评分
#   hue="Addiction_Level"    → 按成瘾级别着色（4 种颜色对应 4 个级别）
#   style="Addiction_Level"  → 不同级别用不同标记形状
#                              hue 控制颜色，style 控制形状
#                              两者叠加使区分更明显（即使打印黑白也看得出）
#   alpha=0.5                → 点透明度（0~1）
#   s=20                     → 点的大小
#   palette={...}            → 为 hue 的每个类别指定颜色
#   ax=ax                    → 画到哪个坐标轴上
#
# 与普通散点图的区别：
#   普通 scatter:           所有点同色，只能看整体趋势
#   带 hue 的 scatterplot:  按类别着色，可以区分不同组别的分布差异
#
sns.scatterplot(data=df, x="Daily_Usage_Hours", y="Mental_Wellbeing_Score",
                hue="Addiction_Level",           # ← 按成瘾级别着色
                style="Addiction_Level",         # ← 不同级别用不同标记
                alpha=0.5, s=20,
                palette={"Low": "#2ecc71", "Moderate": "#f39c12",
                         "High": "#e67e22", "Severe": "#e74c3c"},
                ax=ax)

ax.set_title("使用时长 vs 心理健康（按成瘾级别着色）", fontsize=14, fontweight="bold")
ax.legend(title="成瘾级别")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_11_hue_scatter.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_11_hue_scatter.png")


# ============================================================================
# 第四部分：综合大图 — 多子图面板
# ============================================================================
print("\n" + "=" * 60)
print("🧩 第四部分：综合大图 — 多维度分析面板")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("社交媒体与心理健康 — Seaborn 多维度分析", fontsize=18, fontweight="bold")

# 子图 1：带 hue 的柱状图 — 性别 × 成瘾级别
ax1 = axes[0, 0]
sns.countplot(data=df, x="Gender", hue="Addiction_Level",
              hue_order=["Low", "Moderate", "High", "Severe"],
              palette=["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"],
              ax=ax1)
ax1.set_title("性别 × 成瘾级别", fontsize=12, fontweight="bold")
ax1.legend(title="成瘾级别", fontsize=8)
ax1.set_xlabel("性别")
ax1.set_ylabel("人数")

# 子图 2：小提琴图 — 各平台使用时长分布
ax2 = axes[0, 1]
sns.violinplot(data=df, x="Primary_Platform", y="Daily_Usage_Hours",
               hue="Primary_Platform", palette="Set3", legend=False, ax=ax2)
ax2.set_title("各平台每日使用时长分布", fontsize=12, fontweight="bold")
ax2.set_xlabel("平台")
ax2.set_ylabel("使用时长（小时）")

# 子图 3：箱线图 — 各成瘾级别 × 焦虑评分（带 hue）
ax3 = axes[1, 0]
sns.boxplot(data=df, x="Addiction_Level", y="Anxiety_Score",
            hue="Addiction_Level",
            order=["Low", "Moderate", "High", "Severe"],
            palette=["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"],
            legend=False, ax=ax3)
ax3.set_title("各成瘾级别焦虑评分分布", fontsize=12, fontweight="bold")

# 子图 4：热力图（小版本）
ax4 = axes[1, 1]
small_corr = df[numeric_cols].corr()
sns.heatmap(small_corr, annot=True, fmt=".2f", cmap="RdBu_r",
            center=0, vmin=-1, vmax=1, square=True,
            linewidths=0.5, cbar=False, ax=ax4)
ax4.set_title("指标相关性矩阵", fontsize=12, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sns_12_dashboard.png", dpi=150)
plt.close()
print(f"  已保存: images/sns_12_dashboard.png")


# ============================================================================
# 第五部分：Seaborn vs Matplotlib 总结
# ============================================================================
print("\n" + "=" * 60)
print("📖 Seaborn vs Matplotlib 对比总结")
print("=" * 60)

comparison = [
    ("代码量", "多（需手动配置细节）", "少（一行核心代码）"),
    ("默认美观度", "一般，需手动调样式", "高，内置美观主题"),
    ("数据格式", "NumPy 数组 / 列表", "Pandas DataFrame（原生支持）"),
    ("分组着色", "手写循环 + 手动配色", "hue 参数一键搞定"),
    ("统计图表", "需手动计算统计量", "内置统计（密度/回归/聚类）"),
    ("灵活性", "高（乐高积木）", "中（预制模块）"),
    ("学习曲线", "平缓", "略陡（需先了解 Matplotlib 基础）"),
]

print(f"\n{'对比项':<16} {'Matplotlib':<20} {'Seaborn':<20}")
print("-" * 56)
for item, mpl, sbn in comparison:
    print(f"{item:<16} {mpl:<20} {sbn:<20}")

print("\n💡 最佳实践：")
print("    Seaborn 画图（快速出图）→ Matplotlib 微调（细节美化）")
print("    两者互补，不是替代关系！")
print()
print(f"✅ 所有图表已保存至 {OUTPUT_DIR}/ 目录（文件名 sns_*.png）")
print(f"   共生成 12 张图表")
print("=" * 60)
