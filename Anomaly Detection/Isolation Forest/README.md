# Isolation Forest

## Overview
Isolation Forest is an unsupervised anomaly detection algorithm that identifies anomalies by isolating data points through random partitioning. Anomalies are easier to isolate because they are rare and significantly different from normal observations.

## Features
- Unsupervised learning
- Tree-based anomaly detection
- Efficient on large datasets
- Suitable for fraud detection, network security, sensor monitoring, and industrial fault detection

## Dataset
- Timestamp
- Value
- Ground truth anomaly labels (for evaluation)

## Workflow
1. Load the dataset
2. Visualize the data
3. Train the Isolation Forest model
4. Predict anomalies
5. Visualize detected anomalies
6. Evaluate using a Confusion Matrix

## Libraries Used
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Output
- **1** → Normal
- **-1** → Anomaly

## Conclusion
Isolation Forest detects anomalies by randomly partitioning the data. Points that are isolated with fewer splits are identified as anomalies, making the algorithm fast and effective for large datasets.
