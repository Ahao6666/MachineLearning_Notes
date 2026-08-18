#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matplotlib 数据可视化入门练习脚本（matplotlib_demo.py）

本脚本演示如何使用 Matplotlib 对 CSV 数据进行可视化分析，
涵盖 6 种常用图表类型，每张图都配有详细注释。

学习目标：
  1. 掌握 Matplotlib 的基本绘图流程（figure → plot → show/save）
  2. 了解 6 种常用图表的适用场景
  3. 学会设置标题、标签、图例等图表元素
  4. 学会在一张画布上绘制多个子图

运行方式：python3 matplotlib_demo.py
生成的图表保存在 images/ 文件夹中。
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")  # 使用非交互式后端，确保在无桌面的环境中也能运行
import matplotlib.pyplot as plt
from pathlib import Path

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Serif CJK SC", "Droid Sans Fallback", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
print(f"字体设置: {plt.rcParams['font.sans-serif'][0]}")

# ============================================================================
# 准备工作：读取数据
# ============================================================================
print("正在读取 CSV 数据...")
CSV_FILE = Path(__file__).parent / "social_media_addiction_mental_wellbeing.csv"
OUTPUT_DIR = Path(__file__).parent / "images"
OUTPUT_DIR.mkdir(exist_ok=True)

data = np.genfromtxt(
    CSV_FILE, delimiter=",", dtype=None,
    encoding="utf-8", names=True,
    missing_values=["", " "], filling_values=np.nan
)
print(f"共读取 {len(data)} 条记录\n")

# 常用列的快捷引用
age = data["Age"]
usage = data["Daily_Usage_Hours"].astype(float)
wellbeing = data["Mental_Wellbeing_Score"].astype(float)
anxiety = data["Anxiety_Score"].astype(float)
addiction = data["Addiction_Level"]
platform = data["Primary_Platform"]
gender = data["Gender"]
sleep_hours = data["Sleep_Hours"].astype(float)
notifications = data["Notifications_Per_Day"].astype(float)

# ============================================================================
# 第一部分：基础图表类型
# ============================================================================

# ---------------------------------------------------------------------------
# 图 1：柱状图 —— 按成瘾级别统计人数
# ---------------------------------------------------------------------------
print("📊 图 1：柱状图 — 按成瘾级别统计人数")

# 统计数据
levels = ["Low", "Moderate", "High", "Severe"]
counts = [np.sum(addiction == lv) for lv in levels]

# 设置中英文标签映射
level_labels = {"Low": "低", "Moderate": "中", "High": "高", "Severe": "严重"}
labels_cn = [level_labels[lv] for lv in levels]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制柱状图
bars = ax.bar(labels_cn, counts, color=["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"], width=0.6)

# 在柱子上方显示具体数字
for bar, count in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
            str(count), ha="center", va="bottom", fontsize=12)

# 设置标题和轴标签
ax.set_title("各成瘾级别用户分布", fontsize=16, fontweight="bold")
ax.set_xlabel("成瘾级别", fontsize=12)
ax.set_ylabel("人数", fontsize=12)
ax.set_ylim(0, max(counts) * 1.15)  # 留出顶部空间显示数字

# 保存
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_bar_chart.png", dpi=150)
plt.close()
print(f"  已保存: images/01_bar_chart.png")


# ---------------------------------------------------------------------------
# 图 2：饼图 —— 主要平台占比
# ---------------------------------------------------------------------------
print("📊 图 2：饼图 — 主要平台占比")

# 统计各平台人数
platform_names, platform_counts = np.unique(platform[platform != ""], return_counts=True)

# 按人数降序排序
sorted_idx = np.argsort(-platform_counts)
platform_names = platform_names[sorted_idx]
platform_counts = platform_counts[sorted_idx]

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制饼图
colors = plt.cm.Set3(np.linspace(0, 1, len(platform_names)))
wedges, texts, autotexts = ax.pie(
    platform_counts,
    labels=platform_names,
    autopct="%1.1f%%",       # 显示百分比
    startangle=90,            # 起始角度（12 点钟方向）
    counterclock=False,       # 顺时针排列（配合降序数据，从最大块开始）
    colors=colors,
    textprops={"fontsize": 11}
)

# 设置标题
ax.set_title("用户主要使用平台分布", fontsize=16, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_pie_chart.png", dpi=150)
plt.close()
print(f"  已保存: images/02_pie_chart.png")


# ---------------------------------------------------------------------------
# 图 3：直方图 —— 年龄分布
# ---------------------------------------------------------------------------
print("📊 图 3：直方图 — 年龄分布")

fig, ax = plt.subplots(figsize=(8, 5))

# 绘制直方图
ax.hist(age, bins=15, color="#3498db", edgecolor="white", alpha=0.8)

ax.set_title("用户年龄分布", fontsize=16, fontweight="bold")
ax.set_xlabel("年龄", fontsize=12)
ax.set_ylabel("人数", fontsize=12)

# 标出平均年龄
mean_age = np.mean(age)
ax.axvline(mean_age, color="#e74c3c", linestyle="--", linewidth=2, label=f"平均年龄: {mean_age:.1f} 岁")
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_histogram.png", dpi=150)
plt.close()
print(f"  已保存: images/03_histogram.png")


# ---------------------------------------------------------------------------
# 图 4：箱线图 —— 按成瘾级别分析心理健康评分
# ---------------------------------------------------------------------------
print("📊 图 4：箱线图 — 各成瘾级别的心理健康评分")

fig, ax = plt.subplots(figsize=(8, 5))

# 按成瘾级别分组收集数据
box_data = [wellbeing[addiction == lv][~np.isnan(wellbeing[addiction == lv])] for lv in levels]

# 绘制箱线图
bp = ax.boxplot(box_data, patch_artist=True, widths=0.5)
ax.set_xticklabels(labels_cn)

# 为每个箱子设置不同的颜色
box_colors = ["#2ecc71", "#f39c12", "#e67e22", "#e74c3c"]
for patch, color in zip(bp["boxes"], box_colors):
    patch.set_facecolor(color)  # 给每个箱子设置填充色
    patch.set_alpha(0.7)        # 设置透明度（0=完全透明, 1=不透明）

ax.set_title("不同成瘾级别的心理健康评分分布", fontsize=14, fontweight="bold")
ax.set_xlabel("成瘾级别", fontsize=12)
ax.set_ylabel("心理健康评分", fontsize=12)

# 添加平均参考线
overall_mean = np.nanmean(wellbeing)
ax.axhline(overall_mean, color="#9b59b6", linestyle=":", linewidth=1.5, label=f"总体平均: {overall_mean:.2f}")
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_boxplot.png", dpi=150)
plt.close()
print(f"  已保存: images/04_boxplot.png")


# ---------------------------------------------------------------------------
# 图 5：散点图 —— 每日使用时长 vs 心理健康评分
# ---------------------------------------------------------------------------
print("📊 图 5：散点图 — 每日使用时长 vs 心理健康评分")

# 去掉 NaN 值
valid_mask = ~np.isnan(usage) & ~np.isnan(wellbeing)
usage_valid = usage[valid_mask]
wellbeing_valid = wellbeing[valid_mask]

# 计算相关系数
corr = np.corrcoef(usage_valid, wellbeing_valid)[0, 1]

fig, ax = plt.subplots(figsize=(8, 5))

# 绘制散点图（用浅色半透明点，便于观察密度）
scatter = ax.scatter(usage_valid, wellbeing_valid, alpha=0.3, s=10, c="#3498db")

# 添加趋势线（线性拟合）
m, b = np.polyfit(usage_valid, wellbeing_valid, 1)  # 一次多项式拟合
x_line = np.linspace(usage_valid.min(), usage_valid.max(), 100)
ax.plot(x_line, m * x_line + b, color="#e74c3c", linewidth=2, label=f"趋势线 (斜率={m:.3f})")

ax.set_title("每日使用时长 vs 心理健康评分", fontsize=14, fontweight="bold")
ax.set_xlabel("每日使用时长（小时）", fontsize=12)
ax.set_ylabel("心理健康评分", fontsize=12)
ax.legend(fontsize=11)

# 在图上标注相关系数
ax.text(0.95, 0.05, f"相关系数 r = {corr:.3f}", transform=ax.transAxes,
        ha="right", va="bottom", fontsize=12,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "05_scatter.png", dpi=150)
plt.close()
print(f"  已保存: images/05_scatter.png")


# ---------------------------------------------------------------------------
# 图 6：折线图 —— 不同年龄段的平均心理健康评分
# ---------------------------------------------------------------------------
print("📊 图 6：折线图 — 各年龄段的平均心理健康评分")

# 按年龄段分组
age_bins = np.arange(15, 50, 5)  # 15, 20, 25, ..., 45
age_labels = [f"{a}-{a+4}" for a in age_bins[:-1]]

age_means = []
age_counts = []
for i in range(len(age_bins) - 1):
    mask = (age >= age_bins[i]) & (age < age_bins[i + 1])
    scores = wellbeing[mask]
    valid_scores = scores[~np.isnan(scores)]
    age_means.append(np.mean(valid_scores) if len(valid_scores) > 0 else 0)
    age_counts.append(np.sum(mask))

fig, ax1 = plt.subplots(figsize=(10, 5))

# 折线图（主 y 轴）
color_line = "#2980b9"
ax1.plot(age_labels, age_means, marker="o", color=color_line, linewidth=2.5, markersize=8, label="平均心理健康评分")
ax1.set_xlabel("年龄段", fontsize=12)
ax1.set_ylabel("平均心理健康评分", fontsize=12, color=color_line)
ax1.tick_params(axis="y", labelcolor=color_line)
ax1.set_ylim(5, 8)

# 在每个点上标注具体数值
for label, mean_val in zip(age_labels, age_means):
    ax1.annotate(f"{mean_val:.2f}", (label, mean_val),
                 textcoords="offset points", xytext=(0, 12), ha="center", fontsize=9)

# 柱状图显示人数（副 y 轴）
ax2 = ax1.twinx()
color_bar = "#e74c3c"
ax2.bar(age_labels, age_counts, alpha=0.15, color=color_bar, label="人数")
ax2.set_ylabel("人数", fontsize=12, color=color_bar)
ax2.tick_params(axis="y", labelcolor=color_bar)

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=10)

ax1.set_title("各年龄段平均心理健康评分（折线）与人数（柱状）", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "06_line_chart.png", dpi=150)
plt.close()
print(f"  已保存: images/06_line_chart.png")


# ============================================================================
# 第二部分：综合大图 —— 4 个子图排列在一张画布上
# ============================================================================
print("\n📊 图 7：综合大图 — 多维度分析面板")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("社交媒体与心理健康 — 多维度数据分析", fontsize=18, fontweight="bold")

# ----- 子图 1：柱状图 — 性别 × 成瘾级别 -----
ax1 = axes[0, 0]
genders = ["Male", "Female", "Non-binary"]
gender_labels_cn = ["男性", "女性", "非二元"]
x = np.arange(len(genders))
width = 0.2

for i, lv in enumerate(levels):
    counts_gender = []
    for g in genders:
        counts_gender.append(np.sum((gender == g) & (addiction == lv)))
    ax1.bar(x + i * width, counts_gender, width, label=level_labels[lv])

ax1.set_title("性别 × 成瘾级别", fontsize=12, fontweight="bold")
ax1.set_xticks(x + width * 1.5)
ax1.set_xticklabels(gender_labels_cn)
ax1.legend(fontsize=8)
ax1.set_ylabel("人数")

# ----- 子图 2：散点图 — 每日通知数 vs 焦虑评分 -----
ax2 = axes[0, 1]
valid_n = ~np.isnan(notifications) & ~np.isnan(anxiety)
n_valid = notifications[valid_n]
a_valid = anxiety[valid_n]
ax2.scatter(n_valid, a_valid, alpha=0.2, s=5, c="#9b59b6")
# 趋势线
m2, b2 = np.polyfit(n_valid, a_valid, 1)
x2 = np.linspace(n_valid.min(), n_valid.max(), 100)
ax2.plot(x2, m2 * x2 + b2, "r-", linewidth=2)
corr_notif_anx = np.corrcoef(n_valid, a_valid)[0, 1]
ax2.set_title(f"每日通知数 vs 焦虑评分 (r={corr_notif_anx:.2f})", fontsize=12, fontweight="bold")
ax2.set_xlabel("每日通知数")
ax2.set_ylabel("焦虑评分")

# ----- 子图 3：水平柱状图 — 各平台平均使用时长 -----
ax3 = axes[1, 0]
# 计算每个平台的平均使用时长
platform_means = {}
for pn in np.unique(platform):
    if pn == "":
        continue
    mask_p = platform == pn
    usage_p = usage[mask_p]
    valid_up = usage_p[~np.isnan(usage_p)]
    if len(valid_up) > 0:
        platform_means[pn] = np.mean(valid_up)

sorted_platforms = sorted(platform_means.items(), key=lambda x: x[1])
p_names = [p[0] for p in sorted_platforms]
p_means = [p[1] for p in sorted_platforms]
colors_bar = plt.cm.Set2(np.linspace(0, 1, len(p_names)))
ax3.barh(p_names, p_means, color=colors_bar)
ax3.set_title("各平台平均每日使用时长", fontsize=12, fontweight="bold")
ax3.set_xlabel("平均使用时长（小时）")

# ----- 子图 4：箱线图 — 各成瘾级别的睡眠时长 -----
ax4 = axes[1, 1]
sleep_data = [sleep_hours[(addiction == lv) & ~np.isnan(sleep_hours)] for lv in levels]
bp4 = ax4.boxplot(sleep_data, patch_artist=True, widths=0.5)
ax4.set_xticklabels(labels_cn)
for patch, color in zip(bp4["boxes"], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax4.set_title("各成瘾级别睡眠时长分布", fontsize=12, fontweight="bold")
ax4.set_ylabel("睡眠时长（小时）")
ax4.axhline(np.nanmean(sleep_hours), color="#9b59b6", linestyle=":", label=f"总体平均: {np.nanmean(sleep_hours):.1f}h")
ax4.legend(fontsize=8)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "07_dashboard.png", dpi=150)
plt.close()
print(f"  已保存: images/07_dashboard.png")


# ============================================================================
# 第三部分：图表类型速查
# ============================================================================
print("\n" + "=" * 60)
print("📖 图表类型与适用场景速查")
print("=" * 60)

chart_guide = [
    ("柱状图 (bar)", "对比不同类别的数量", "各个成瘾级别的人数对比"),
    ("饼图 (pie)", "展示各部分的占比", "各平台用户的占比"),
    ("直方图 (hist)", "展示数据分布", "年龄分布、使用时长分布"),
    ("箱线图 (boxplot)", "展示数据分布+异常值", "各组成绩的中位数/四分位/离群点"),
    ("散点图 (scatter)", "展示两个变量的关系", "使用时长 vs 心理健康评分"),
    ("折线图 (plot)", "展示趋势变化", "不同年龄段的平均评分变化"),
    ("水平柱状图 (barh)", "类别名较长时", "各平台平均使用时长"),
    ("组合图 (twinx)", "双 y 轴对比", "折线(评分) + 柱状(人数)"),
    ("子图 (subplots)", "多图排列对比", "2×2 综合面板"),
]

for i, (name, usage, example) in enumerate(chart_guide, 1):
    print(f"  {i}. {name}")
    print(f"     用途: {usage}")
    print(f"     示例: {example}")
    print()

print(f"✅ 所有图表已保存至 {OUTPUT_DIR}/ 目录")
print(f"   共生成 8 张图表（6 张独立 + 1 张综合面板）")
print("=" * 60)
