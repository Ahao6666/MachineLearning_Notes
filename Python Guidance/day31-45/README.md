# Day 31-45：监督学习算法实战与巩固训练

本文件夹是 5 个基础算法脚本学完之后进入实战的阶段，内容按"基础 → 实践 "两个层次组织：

1. **基础脚本（5 个）**：围绕 `predictive_maintenance.csv` 演示 KNN、SVM、梯度提升树、交叉验证和超参数调优，建立完整的表格数据机器学习流程概念。
2. **实践脚本（1 个）**：把学到的流程应用到新数据集——心脏病的表格数据分类（`heart.ipynb`）。

## 运行环境

建议使用 `ml-industrial` Conda 环境：

```bash
conda activate ml-industrial
jupyter lab
```

主要依赖版本：

- Python 3.11
- pandas 3.0.3
- scikit-learn 1.9.0
- XGBoost 3.2.0
- LightGBM 4.6.0
- matplotlib 3.8.0
- seaborn 0.13.2
- PyTorch 与 torchvision（仅图像分类脚本需要）

也可以在项目根目录或本目录下批量执行 notebook：

```bash
conda activate ml-industrial
jupyter nbconvert --to notebook --execute --inplace knn_predictive_maintenance.ipynb
```

## 推荐学习顺序

### 第一部分：基础脚本（预测性维护系列）

1. `knn_predictive_maintenance.ipynb`
   先理解距离、标准化、K 值和分类阈值。

2. `svm_predictive_maintenance.ipynb`
   理解最大间隔、支持向量、参数 C 和决策边界。

3. `xgboost_lightgbm_predictive_maintenance.ipynb`
   理解集成学习、梯度提升树、早停和类别不平衡处理。

4. `kfold_cross_validation.ipynb`
   学习如何更可靠地评估模型，而不是只依赖一次训练/测试划分。

5. `hyperparameter_tuning_grid_random.ipynb`
   学习如何系统或随机地搜索超参数，并用独立测试集验证结果。

### 第二部分：实践脚本（换数据集练手）

6. `heart.ipynb`
   用第一部分的标准流程（预处理、训练、评估指标）做心脏病预测，练习快速套用到新表格数据集。



## 文件说明

### Notebook

| 文件 | 说明 |
|---|---|
| `knn_predictive_maintenance.ipynb` | 演示 K 近邻算法：标准化、One-Hot 编码、K 值选择、距离加权 KNN、概率阈值调整，以及在漏报和误报之间做业务权衡。 |
| `svm_predictive_maintenance.ipynb` | 演示支持向量机：二维最大间隔分界线、支持向量、线性 SVM、参数 C、类别权重和决策阈值。 |
| `xgboost_lightgbm_predictive_maintenance.ipynb` | 演示梯度提升树：XGBoost 与 LightGBM、验证集早停、类别不平衡处理、特征重要度和阈值调整。 |
| `kfold_cross_validation.ipynb` | 演示 Stratified K-Fold 交叉验证：比较多个模型的均值、标准差和每折波动，用箱线图评估模型稳定性。 |
| `hyperparameter_tuning_grid_random.ipynb` | 演示超参数调优：使用 `GridSearchCV` 穷举搜索、`RandomizedSearchCV` 随机搜索，并在独立测试集上比较结果。 |
| `heart.ipynb` | 心脏病预测实践：ColumnTransformer 预处理、多种分类器对比、混淆矩阵与分类报告。 |

### 数据集

| 文件 | 说明 |
|---|---|
| `predictive_maintenance.csv` | 设备运行记录，10000 条、12 列字段，用于基础脚本系列。 |
| `heart.csv` | 心脏病数据集，用于 `heart.ipynb`。 |

## 预测性维护数据集字段

目标变量：

- `Machine failure`：`1` 表示设备故障，`0` 表示正常。

基础脚本系列使用的输入特征：

- `Type`：设备类型；
- `Air temperature`：空气温度；
- `Process temperature`：过程温度；
- `Rotational speed`：转速；
- `Torque`：扭矩；
- `Tool wear`：刀具磨损。

以下字段是故障原因或故障模式指示变量：

- `TWF`
- `HDF`
- `PWF`
- `OSF`
- `RNF`

这些字段与目标变量关系过强，直接作为输入特征会造成标签泄露，因此 notebook 中没有把它们作为普通特征使用。

## 注意事项

1. 预测性维护和心脏病预测都是类别不平衡任务：负类样本远多于正类，因此不能只看 Accuracy。
2. 故障/疾病预测通常更关注 Recall、Precision、F1 以及漏报/误报数量。
3. Pipeline 中的预处理会在交叉验证的每一折里重新拟合，避免验证折信息泄露到训练过程。
4. `best_score_` 或交叉验证分数只是调参依据，最终仍应查看未参与调参的测试集结果。
5. 阈值调整不是重新训练模型，而是移动"判定为正类"的概率边界。
