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

通过计算样本出现的概率来判断该样本是不是异常值

高斯分布/正态分布：
$$
p(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{\frac{-(x-\mu)^2}{2\sigma^2}}
$$
其中$$\mu$$表示表示均值，$$\sigma^2$$表示方差。

最大似然估计与上述高斯分布的关系。

异常检测算法：

1. 选择认为可能在异常检测中存在的n个特征点
2. 计算每个特征点集的均值和方差，构成高斯分布函数
3. 给几个新的样本后，计算概率$$p(x)$$，即所有概率相乘之积。若$$p(x)$$小于一定阈值 ，则认为存在异常。

开发异常检测系统的实用技巧：

同样将数据集分为训练集/交叉验证集/测试集三类，其中交叉验证集和测试集中包含部分异常样本，便于调整参数阈值$$\epsilon$$和特征数量$$x_j$$。

**异常检测与监督学习的对比：**

| 异常检测                                                     | 监督学习                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 适用于只有少量的正样本（异常样本）有大量的负样本的情况       | 适用于有大量的正样本和负样本的情况                           |
| 适用于有很多类型的异常；异常情况难以学习；或者未来可能出现的异常情况在当前样本中不存在等 | 有足够的样本数量让算法知道正样本室怎么样的；未来的正样本在训练数据中基本存在 |
| 比如：欺诈行为，制造业中没见过的一些缺陷，数据中心的检测设备 | 比如：垃圾邮件，制造业中一些常见的缺陷，天气预测，疾病分类   |

**选择使用哪些特征**

最好是选择高斯分布的特征，如果不是，尝试将其进行处理，转化为高斯分布

异常检测的误差分析，看看能不能创建新的特征

## 第二周：推荐系统

### 协同过滤Collaborative filtering

以不同人员对电影的评分公式的含义如下：

$r(i,j) = 1$ if user $j$ has rated movie $i$ (0 otherwise)

$y^{(i,j)} =$ rating given by user $j$ on movie $i$ (if defined)

$w^{(j)}, b^{(j)} =$ parameters for user $j$

$x^{(i)} =$ feature vector for movie $i$

For user $j$ and movie $i$, predict rating: $w^{(j)} \cdot x^{(i)} + b^{(j)}$

$m^{(j)} =$ no. of movies rated by user $j$

To learn $w^{(j)}, b^{(j)}$:
$$
\begin{equation}
\min J(w^{(j)},b^{(j)})=\frac{1}{2m^{(j)}} \sum_{i:r(i,j)=1} \left(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)}\right)^2+\frac{\lambda}{2m^{(j)}} \sum_{k=1}^{n} \left(w_k^{(j)}\right)^2
\label{eq:cost_j}
\tag{cost-1}
\end{equation}
$$
式$\ref{eq:cost_j}$为便于计算，可去除常值$$m^{(j)}$$，将代价函数计算公式调整为：
$$
\begin{equation}
\min J(w^{(j)},b^{(j)})=\frac{1}{2} \sum_{i:r(i,j)=1} \left(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)}\right)^2+\frac{\lambda}{2} \sum_{k=1}^{n} \left(w_k^{(j)}\right)^2
\label{eq:cost_j-2}
\tag{cost-2}
\end{equation}
$$
对于所有的用户，如何训练 $w^{(1)}, b^{(1)},\ w^{(2)}, b^{(2)},\ \ldots\ w^{(n_u)}, b^{(n_u)}$ :

$$
\begin{equation}
J\left(\begin{matrix} w^{(1)},\ \ldots,\ w^{(n_u)} \\ b^{(1)},\ \ldots,\ b^{(n_u)} \end{matrix}\right)
= \frac{1}{2} \sum_{j=1}^{n_u} \sum_{i:r(i,j)=1} \left( w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)} \right)^2
+ \frac{\lambda}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} \left( w_k^{(j)} \right)^2
\label{eq:cost_j-3}
\tag{cost-3}
\end{equation}
$$

在计算电影特征的时候，代价函数修改为：
$$
\begin{equation}
minJ(x^{(i)})=\frac{1}{2} \sum_{i:r(i,j)=1} \left(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)}\right)^2+\frac{\lambda}{2} \sum_{k=1}^{n} \left(x_k^{(i)}\right)^2
\label{eq:cost_j-4}
\tag{cost-4}
\end{equation}
$$
对所有电影特征的学习，则改为
$$
\begin{equation}
J(x^{(1)},x^{(2)},\ \ldots,\ x^{(n_m)} )
= \frac{1}{2} \sum_{i=1}^{n_m} \sum_{i:r(i,j)=1} \left( w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)} \right)^2
+ \frac{\lambda}{2} \sum_{i=1}^{n_m} \sum_{k=1}^{n} \left( x_k^{(j)} \right)^2
\label{eq:cost_j-5}
\tag{cost-5}
\end{equation}
$$
将以上两个代价函数$\ref{eq:cost_j-3}$和 $\ref{eq:cost_j-5}$组合到一起，则可以得到：
$$
\begin{equation}
J(w,b,x)= \frac{1}{2} \sum_{(i,j):r(i,j)=1} \left( w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)} \right)^2
+ \frac{\lambda}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} \left( w_k^{(j)} \right)^2
+ \frac{\lambda}{2} \sum_{i=1}^{n_m} \sum_{k=1}^{n} \left( x_k^{(j)} \right)^2
\label{eq:cost_j-6}
\tag{cost-6}
\end{equation}
$$
线性回归使用**梯度下降**算法计算代价函数的最小值
$$
\begin{equation}
\begin{aligned}
w_i^{(j)} &= w_i^{(j)} - \alpha \frac{\partial}{\partial w_i^{(j)}} J(w,b,x) \\
b^{(j)} &= b^{(j)} - \alpha \frac{\partial}{\partial b^{(j)}} J(w,b,x) \\
x_k^{(i)} &= x_k^{(i)} - \alpha \frac{\partial}{\partial x_k^{(i)}} J(w,b,x)
\end{aligned}
\label{eq:deri-1}
\tag{deri-1}
\end{equation}
$$
**二进制标签（喜欢/推荐/不喜欢等）**：将打分系统类型的线性回归变为逻辑回归
$$
\begin{equation}
\begin{aligned}
y^{(i,j)}:\quad f_{(w,b,x)}(x) &= g\left(w^{(j)} \cdot x^{(i)} + b^{(j)}\right) \\
L\left(f_{(w,b,x)}(x), y^{(i,j)}\right) &= -y^{(i,j)}\log\left(f_{(w,b,x)}(x)\right) - \left(1-y^{(i,j)}\right)\log\left(1-f_{(w,b,x)}(x)\right) \\
J(w,b,x) &= \sum_{(i,j):r(i,j)=1} L\left(f_{(w,b,x)}(x), y^{(i,j)}\right)
\end{aligned}
\label{eq:cost_7}
\tag{cost-7}
\end{equation}
$$

> 这个不是无监督机器学习系统吗？怎么有$y^{(i,j)}$这个好像表示有标签的值呢？

**推荐系统应用细节**

均值标准化：对已有的分数计算均值，然后将未知评分用均值代替

### 基于内容的过滤算法Content-based filtering

比较与协同过滤算法的异同

使用神经网络将$$x_u$$和$$x_m$$转化为$$v_u$$和$$v_m$$为了实现维度的统一，预测结果为$$v_u·v_m$$

代价函数：
$$
J = \sum_{(i,j):r(i,j)=1} (v_u^{(j)} * v_m^{(i)} - y^{(i,j)})^2 + NN regularization term
$$
为实现快速推荐的目标，将推荐过程分为检索和排序两个步骤。



## 第三周：强化学习