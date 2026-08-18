# 1. 导入随机森林分类器（scikit-learn 中的机器学习算法）
from sklearn.ensemble import RandomForestClassifier

# 2. 创建随机森林分类器对象
#    random_state=0：固定随机种子，保证每次运行结果一致（可复现）
clf = RandomForestClassifier(random_state=0)

# 3. 准备训练数据 X（特征）和 y（标签）
#    X 是一个 2 行 3 列的列表：2 个样本，每个样本有 3 个特征
X = [[ 1,  2,  3],  # 样本 1：特征值为 1, 2, 3
     [11, 12, 13]]  # 样本 2：特征值为 11, 12, 13
y = [0, 1]          # 标签：样本 1 属于类别 0，样本 2 属于类别 1

# 4. 训练模型（fit = 让模型从数据中学习规律）
#    模型会根据 X 和 y 学习如何根据特征判断类别
clf.fit(X, y)

# 5. 用训练好的模型做预测
#    predict(X)：对训练数据本身进行预测，看模型是否学对了（理想情况输出 [0 1]）
print(clf.predict(X))  # 输出: [0 1]

#    predict(新数据)：对 2 个从未见过的新样本做预测
#    新样本 [4, 5, 6] 的特征介于两类之间，[14, 15, 16] 特征更大
print(clf.predict([[4, 5, 6], [14, 15, 16]]))  # 输出: [0 1]