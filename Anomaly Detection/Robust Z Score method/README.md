
# Robust Z-Score for Anomaly Detection

This project demonstrates anomaly detection using the **Robust Z-Score** method on the EC2 CPU Utilization dataset. Unlike the standard Z-Score, the Robust Z-Score uses the **Median** and **Median Absolute Deviation (MAD)**, making it more resistant to outliers and suitable for skewed data.

## Objectives

- Load and explore the CPU utilization dataset.
- Visualize normal observations and anomalies.
- Calculate the Median and MAD.
- Compute the Robust Z-Score for each observation.
- Detect anomalies using a predefined threshold.
- Evaluate the detection performance with a Confusion Matrix.

## Dataset

- **Dataset:** EC2 CPU Utilization
- **Features:**
  - `timestamp`
  - `value` (CPU utilization)

Ground-truth anomaly timestamps are manually labeled for evaluation.

## Workflow

1. Import required libraries.
2. Load the dataset.
3. Convert timestamps to datetime format.
4. Create ground-truth anomaly labels.
5. Visualize the dataset.
6. Calculate the Median and MAD.
7. Compute the Robust Z-Score.
8. Detect anomalies using a threshold of **±3.5**.
9. Visualize detected anomalies.
10. Evaluate the model using a Confusion Matrix.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Scikit-learn

## Results

The Robust Z-Score successfully identifies observations that significantly deviate from the median while remaining robust against extreme values. The Confusion Matrix provides a simple evaluation of the detection performance against the known anomaly labels.

## Key Concepts

- Anomaly Detection
- Robust Statistics
- Median
- Median Absolute Deviation (MAD)
- Robust Z-Score
- Exploratory Data Analysis (EDA)
- Confusion Matrix

## Future Work

- Isolation Forest
- Local Outlier Factor (LOF)
- One-Class SVM
- DBSCAN for Outlier Detection

---
**Author:** Md Shaharear Hossain Lemon
