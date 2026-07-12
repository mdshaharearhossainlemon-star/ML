
P-Growth for Frequent Pattern Mining
Overview

This project implements the FP-Growth (Frequent Pattern Growth) algorithm to discover frequent itemsets and generate association rules from a market basket dataset. Unlike Apriori, FP-Growth avoids candidate generation by using an FP-Tree, making it faster and more memory-efficient for large datasets.

Dataset
Dataset: store_data.csv
Transactions: 7,501
Attributes: 20 items per transaction
Libraries Used
Pandas
Matplotlib
mlxtend
Workflow
Load the transaction dataset.
Convert transactions into one-hot encoded format using TransactionEncoder.
Apply the FP-Growth algorithm to mine frequent itemsets.
Generate association rules based on confidence.
Visualize the discovered patterns.
Parameters
Parameter	Value
Minimum Support	0.003
Metric	Confidence
Minimum Confidence	0.4
Results
Discovered frequent itemsets using FP-Growth.
Generated association rules with confidence and lift.
Visualized the most frequent itemsets and rule relationships.
Visualizations
Top 10 Frequent Itemsets (Bar Chart)
Support Distribution
Confidence vs Lift Scatter Plot
