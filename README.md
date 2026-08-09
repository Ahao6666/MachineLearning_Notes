# 学习笔记 

## Coursera-[Advanced Learning Algorithms](https://www.coursera.org/learn/advanced-learning-algorithms/home/welcome)

## **第一周：神经网络**

神经网络从介绍生物的神经元与大脑开始，引入神经网络模型，需要掌握用TensorFlow库构建基础神经网络模型的能力。

## **第二周：神经网络训练**

在使用TensorFlow训练神经网络模型的过程中需要注意代码的前后关系。隐藏层的激活函数一般为relu，输出层的激活函数为linear，在模型编译中设置加上from_logits=True。介绍了softmax输出的神经网络，理解多标签(multi-label)和分类(multi-class)的区别。

介绍了反向传播求导的计算方法

## **第三周：应用机器学习的建议**

机器学习的诊断：判断为了提升性能，学习算法中哪些起了因素重要的作用

评估模型：将数据分为训练集和测试集，分别计算训练集和测试集的代价函数，从而判断训练的结果是否合理

将数据集分为**训练数据**（training set）60%/**交叉验证**（cross validation）20%/**测试数据**（test set）20% 

交叉验证集（cross validation set）或者称为验证集（validation set）/开发集（dev set）的作用是什么？

采用多项式回归和神经网络两种算法评估模型，以下是部分代码

```python
# Initialize lists to save the errors, models, and feature transforms
train_mses = []
cv_mses = []
models = []
polys = []
scalers = []

# Loop over 10 times. Each adding one more degree of polynomial higher than the last.
for degree in range(1,11):
    
    # Add polynomial features to the training set
    poly = PolynomialFeatures(degree, include_bias=False)
    X_train_mapped = poly.fit_transform(x_train)
    polys.append(poly)
    
    # Scale the training set
    scaler_poly = StandardScaler()
    X_train_mapped_scaled = scaler_poly.fit_transform(X_train_mapped)
    scalers.append(scaler_poly)
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train_mapped_scaled, y_train )
    models.append(model)
    
    # Compute the training MSE
    yhat = model.predict(X_train_mapped_scaled)
    train_mse = mean_squared_error(y_train, yhat) / 2
    train_mses.append(train_mse)
    
    # Add polynomial features and scale the cross validation set
    X_cv_mapped = poly.transform(x_cv)
    X_cv_mapped_scaled = scaler_poly.transform(X_cv_mapped)
    
    # Compute the cross validation MSE
    yhat = model.predict(X_cv_mapped_scaled)
    cv_mse = mean_squared_error(y_cv, yhat) / 2
    cv_mses.append(cv_mse)
    
# Plot the results
degrees=range(1,11)
utils.plot_train_cv_mses(degrees, train_mses, cv_mses, title="degree of polynomial vs. train and CV MSEs")
```



```python
# Initialize lists that will contain the errors for each model
nn_train_mses = []
nn_cv_mses = []

# Build the models
nn_models = utils.build_models()

# Loop over the the models
for model in nn_models:
    
    # Setup the loss and optimizer
    model.compile(
    loss='mse',
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    )

    print(f"Training {model.name}...")
    
    # Train the model
    model.fit(
        X_train_mapped_scaled, y_train,
        epochs=300,
        verbose=0
    )
    
    print("Done!\n")

    
    # Record the training MSEs
    yhat = model.predict(X_train_mapped_scaled)
    train_mse = mean_squared_error(y_train, yhat) / 2
    nn_train_mses.append(train_mse)
    
    # Record the cross validation MSEs 
    yhat = model.predict(X_cv_mapped_scaled)
    cv_mse = mean_squared_error(y_cv, yhat) / 2
    nn_cv_mses.append(cv_mse)

    
# print results
print("RESULTS:")
for model_num in range(len(nn_train_mses)):
    print(
        f"Model {model_num+1}: Training MSE: {nn_train_mses[model_num]:.2f}, " +
        f"CV MSE: {nn_cv_mses[model_num]:.2f}"
        )
```

分类回归

```python
# Initialize lists that will contain the errors for each model
nn_train_error = []
nn_cv_error = []

# Build the models
models_bc = utils.build_models()

# Loop over each model
for model in models_bc:
    
    # Setup the loss and optimizer
    model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    )

    print(f"Training {model.name}...")

    # Train the model
    model.fit(
        x_bc_train_scaled, y_bc_train,
        epochs=200,
        verbose=0
    )
    
    print("Done!\n")
    
    # Set the threshold for classification
    threshold = 0.5
    
    # Record the fraction of misclassified examples for the training set
    yhat = model.predict(x_bc_train_scaled)
    yhat = tf.math.sigmoid(yhat)
    yhat = np.where(yhat >= threshold, 1, 0)
    train_error = np.mean(yhat != y_bc_train)
    nn_train_error.append(train_error)

    # Record the fraction of misclassified examples for the cross validation set
    yhat = model.predict(x_bc_cv_scaled)
    yhat = tf.math.sigmoid(yhat)
    yhat = np.where(yhat >= threshold, 1, 0)
    cv_error = np.mean(yhat != y_bc_cv)
    nn_cv_error.append(cv_error)

# Print the result
for model_num in range(len(nn_train_error)):
    print(
        f"Model {model_num+1}: Training Set Classification Error: {nn_train_error[model_num]:.5f}, " +
        f"CV Set Classification Error: {nn_cv_error[model_num]:.5f}"
        )
    
# Select the model with the lowest error
model_num = 3

# Compute the test error
yhat = models_bc[model_num-1].predict(x_bc_test_scaled)
yhat = tf.math.sigmoid(yhat)
yhat = np.where(yhat >= threshold, 1, 0)
nn_test_error = np.mean(yhat != y_bc_test)

print(f"Selected Model: {model_num}")
print(f"Training Set Classification Error: {nn_train_error[model_num-1]:.4f}")
print(f"CV Set Classification Error: {nn_cv_error[model_num-1]:.4f}")
print(f"Test Set Classification Error: {nn_test_error:.4f}")
```

诊断bias和variance：

训练数据计算的代价函数高，验证数据计算的代价函数高，则一般是欠拟合，高偏差bias

训练数据计算的代价函数低，验证数据计算的代价函数高，则一般是过拟合，高方差variance

训练数据计算的代价函数高，验证数据计算的代价函数远大于训练数据的代价函数，则一般既有高偏差bias又有高方差variance

训练数据计算的代价函数低，验证数据计算的代价函数低，则一般是希望的拟合结果

![image-20260807135539545](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260807135539545.png)

**模型结构选择（多项式级数）**和**正则化参数lamdba选择**对训练模型的影响。

![image-20260807135501027](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260807135501027.png)

确定评估基线水平需要考虑三点：1人类的水平，2竞品的水平，3基于实验的猜测

若训练集的代价函数与基线水平之间有较大误差，则认为训练的偏差较大

若验证集的代价函数与训练集的代价函数之间有较大偏差，则认为训练的方差较大

学习曲线：

随着训练集数据的增加，学习曲线（代价函数）可能上升。可以根据学习曲线，判断是否需要更加训练的数据集。若存在大偏差，则增加训练集的大小效果并不明显，若存在较大的方差，则可以增加训练集的数据。

![image-20260807134851640](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260807134851640.png) 

![image-20260807135057084](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260807135057084.png)

解决高偏差和高方差的方式

| 修复高偏差     | 修复高方差           |
| -------------- | -------------------- |
| 增加其他特征   | 获取更多的训练数据集 |
| 添加特征的级数 | 降低特征集的数量     |
| 降低lamdba     | 增加lamdba           |

神经网络和偏差方差

选择合适的lamdba对神经网络的使用基本没有坏处。

使用神经网络训练模型降低偏差和方差的一般流程

![image-20260807141742049](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260807141742049.png)

**机器学习开发迭代循环**

Choose architecture（model，data，etc.）->Train model->Diagnostics(bias, variance and error analysis)

**错误分析**

将错误进行分类，来判断哪些是需要重点解决的，哪些不值得花费大量的时间来处理

**增加数据**

如果增加数据的总量难度比较大，那可以尝试增加数据的类型。

变换已经存在的数据来生成新的数据，比如将图片放大、缩小、镜像、改变透明度，音频增加噪声等

数据合成：生成新的数据集

Transfer Learning: using data from a different task:

首先监督预训练(supervised pretrainng)，随后进行优化调参(fine tuning)

其中预训练的参数一般是事前已经完成的，可以拿来直接使用。之后使用自己的数据来对参数进行优化。

**机器学习项目的全周期**

![image-20260807172037580](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260807172037580.png)

  倾斜数据集的误差指标：**精确性（precision）和召回率（recall）**，解释这两种评价指标的含义和特点

![image-20260809154451370](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260809154451370.png)

增加逻辑回归中的阈值，则精确性会上升，召回率会下降，反制，则精确性会下降，但召回率上升。

![image-20260809171458553](C:\Users\ahous\AppData\Roaming\Typora\typora-user-images\image-20260809171458553.png)

选择阈值采用F1评分的方式，也成为调和平均数。

## 第四周：决策树
