# 1. 导入 StandardScaler（数据标准化器，来自 scikit-learn 预处理模块）
from sklearn.preprocessing import StandardScaler

# 2. 准备原始数据 X
#    2 个样本，每个样本有 2 个特征：
#    特征 1（第 1 列）：[0, 1]   —— 数值范围较小
#    特征 2（第 2 列）：[15, -10] —— 数值范围较大（注意两个特征量纲差异大）
X = [[0, 15],
     [1, -10]]

# 3. 标准化（Z-score 归一化）：
#    公式：x_new = (x - 均值) / 标准差
#    - fit(X)      ：计算每列的均值 μ 和标准差 σ（只学习参数，不转换）
#    - transform(X)：用学到的 μ 和 σ 对数据做转换
#    结果：每列变成均值为 0、标准差为 1 的分布
#    特征 1：[0, 1]    → 均值为 0.5，标准差为 0.5  → [-1,  1]
#    特征 2：[15, -10] → 均值为 2.5，标准差为 12.5 → [ 1, -1]
#    最终输出：[[-1,  1],
#              [ 1, -1]]
# scale data according to computed scaling values
print(StandardScaler().fit(X).transform(X))