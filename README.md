# Local Outlier Factor (LOF)

## Overview
Local Outlier Factor (LOF) is an unsupervised anomaly detection algorithm that identifies outliers by comparing the local density of each data point with the density of its nearest neighbors. Points with significantly lower local density are considered anomalies.

## Features
- Unsupervised learning
- Density-based anomaly detection
- Detects local outliers
- Suitable for fraud detection, network security, sensor monitoring, and manufacturing

## Dataset
- Timestamp
- Value
- Ground truth anomaly labels (for evaluation)

## Workflow
1. Load the dataset
2. Visualize the data
3. Train the LOF model
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
LOF detects anomalies by comparing the density of a data point with the density of its neighboring points. Data points with much lower local density are identified as anomalies.
