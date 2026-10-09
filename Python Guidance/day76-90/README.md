# 预测性维护：有监督 vs 无监督学习

本目录包含基于同一份「机器预测性维护」数据集的两个学习项目：

| 文件 | 任务类型 | 方法 |
|---|---|---|
| `predictive_maintenance.ipynb` | 有监督学习（分类） | KNN、SVM、RandomForest + 特征工程 |
| `predictive_maintenance_Unsupervised.ipynb` | 无监督学习（聚类 / 异常检测） | K-Means、Isolation Forest、LOF、One-Class SVM |

---

## 数据集

- 来源：[Machine Predictive Maintenance Classification (Kaggle)](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)
- 本地文件：`predictive_maintenance.csv`，共 10000 行 × 10 列

### 特征

| 特征 | 含义 |
|---|---|
| `Air temperature [K]` | 空气温度 |
| `Process temperature [K]` | 过程温度 |
| `Rotational speed [rpm]` | 转速 |
| `Torque [Nm]` | 转矩 |
| `Tool wear [min]` | 工具磨损 |
| `Type` | 设备类型（类别特征：L/M/H） |

### 标签

- `Target`：二分类（0=正常，1=故障），**故障样本仅约 3.4%，极度不平衡**
- `Failure Type`：更细的故障类型（含 No Failure 共 6 类）

---

## 有监督学习结论（`predictive_maintenance.ipynb`）

### 各方法在测试集上的「故障类」F1 对比

| 方法 | 故障 F1 |
|---|---|
| KNN（K=5） | 0.435 |
| SVM 线性核 | 0.25 |
| SVM RBF | 0.44 |
| SVM RBF + 阈值调整 | 0.618 |
| SMOTE + SVM RBF | 0.45 |
| RandomForest | 0.65 |
| **RandomForest + 特征工程** | **0.80** ✅ |

### 关键结论

1. **类别不平衡是主要瓶颈**：默认模型倾向于全预测为「正常」，导致故障类 recall 很低。
2. **阈值调整最划算**：对 SVM 的概率/决策分数扫阈值，F1 从 0.44 直接提升到 0.618。
3. **SMOTE 收益有限**：因为 SVM 已用 `class_weight="balanced"`，再叠加过采样提升很小。
4. **树模型更适合表格数据**：RandomForest 的 precision（0.69）远高于 SVM（约 0.30）。
5. **特征工程带来最大提升**：构造 `power`（转矩×转速）、`temp_diff`（温差）、`wear_per_torque`、`speed_torque_ratio` 后，F1 达到 0.80。

### 注意事项

- **阈值不能直接在测试集上选**（会有轻微数据泄漏），严谨做法是从训练集再切一份验证集选阈值，最后只在测试集上报一次。
- 评估不平衡分类任务时，应重点看**少数类的 F1 / PR-AUC**，而不是 accuracy。
- 预测故障时通常更看重 **recall**（宁多报、不漏报），可结合业务调整阈值。

---

## 无监督学习结论（`predictive_maintenance_Unsupervised.ipynb`）

### 1. K-Means 聚类（按 `Failure Type` 6 类评估）—— 效果差

- ARI / 同质性 / 完整性都很低。
- **原因**：
  - 6 类极度不平衡（No Failure 占 ~96%），K-Means 会把正常类切成多块；
  - K-Means 假设簇是球形、大小相近，而故障类型在特征空间高度重叠；
  - 业务上更有意义的问题不是「把 6 种故障互相分开」，而是「找出异常样本」。

### 2. 无监督异常检测（按 `Target` 评估）—— 更合理

| 方法 | ROC-AUC | PR-AUC |
|---|---|---|
| Isolation Forest | 0.787 | 0.150 |
| LOF | **0.805** | 0.179 |
| **One-Class SVM** | 0.772 | **0.228** ✅ |
| 三模型集成 | — | 通常更高 |

### 关键结论

1. 预测性维护的无监督分析应优先采用**异常检测**思路，而不是多分类聚类。
2. 在极度不平衡数据上，**PR-AUC 比 ROC-AUC 更有参考价值**（ROC 会虚高）。
   - PR-AUC 随机基线 ≈ 正类占比 ≈ 0.034，所以 0.15~0.23 已明显好于随机。
3. 三个检测器中 **One-Class SVM 的 PR-AUC 最高（0.228）**，最值得优先采用。
4. 把多个检测器的分数 min-max 归一化后**取平均（集成）**，通常比单个模型更稳定。

### 注意事项

- 异常检测模型输出的 `decision_function` / `score_samples` **越低越异常**，取负号才是「异常分数」。
- `contamination` 应设为约等于真实故障比例（3.4%）。
- 换用 LOF 时 `n_neighbors` 很敏感，建议在 10~50 之间试。
- 可视化时建议用**连续异常分数**着色（而不是二值标签），信息更丰富。

---

## 环境说明

- 使用的 Conda 环境：`ml-industrial`（Python 3.11）
- 安装包时务必用 **`python -m pip install ...`**，不要直接用裸 `pip`：
  - 裸 `pip` 可能指向 `~/.local/bin/pip`（系统 Python 3.10），导致包装到错误位置。
- 若 import 时报 `libstdc++.so.6: version 'CXXABI_1.3.15' not found`：
  - 在运行前先执行 `export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$LD_LIBRARY_PATH"`，让 conda 环境自带的 libstdc++ 优先加载。

---

## 常见问题

1. **`No module named 'pytorch_lightning'` / `'anomalib'`**：包没装进当前环境，用 `python -m pip install -e .` 装到 `ml-industrial`。
2. **`'float' object has no attribute 'round'`**：sklearn 的 `roc_auc_score`、`average_precision_score`、`f1_score` 返回 Python `float`，没有 `.round()` 方法。应使用 `round(x, 3)` 或 `f"{x:.3f}"`。
3. **`predict_proba is not available when probability=False`**：SVC 需设置 `probability=True`，或改用 `decision_function` 的分数扫阈值。
