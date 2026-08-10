# Unsupervised Learning 学习笔记

> 课程来源：[Unsupervised Learning, Recommenders, Reinforcement Learning](https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning?specialization=machine-learning-introduction)

---

## 第一周：无监督学习

### 聚类Clustering

聚类的概念：彼此相似的点组

**K均值算法**

反复执行两件不同的事：1）聚类质心分配点，2）移动聚类质心

也即首先根据与初始的聚类质心的距离，将所有点进行分配，然后计算一个聚类的均值中点，将聚类移动到计算的均值点，之后再进行分类。

**优化目标：**

代价函数也称为失真函数（Distortion）
$$
J(x^{(1)},...,x^{(m)},\mu_1,...,\mu_K) = \frac{1}{m} \sum_{i=1}^{m} \left\| x^{(i)} - \mu_{c^{(i)}} \right\|^2
$$
初始化K-means：

- 随机初始化聚类点
- 将聚类点设置到几个训练数据集中

为了避免陷入局部最优解，可以多次（50-1000次）生成随机聚类点，多次计算代价函数并选择其中最小的J

**如何选择聚类的数量**

1）Elbow method肘部算法：绘制聚类数量与成本函数J之间的关系

2）根据下游的需求确定聚类数量

### 异常检测Anomaly detection

## 第二周：推荐系统

## 第三周：强化学习