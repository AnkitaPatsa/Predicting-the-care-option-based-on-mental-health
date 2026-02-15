# Predicting-the-care-option-based-on-mental-health
# Problem Statement - 
The given dataset is a mental-health-related survey containing multiple categorical attributes such as work environment, stress factors, mood indicators, and personal habits. The target variable chosen for this task is CareOptions, a multi-class label describing what type of mental-health care options an individual prefers.
# Dataset Description -
Dataset Name: Mental Health dataset

Source: https://www.kaggle.com/datasets/alamshihab075/mental-health-dataset?select=Mental+Health+dataset1.csv

Target Variable: CareOptions (Multi-class) 

Features: The dataset contains 16 categorical attributes like Gender, Country, Occupation, Treatment, Family history and many more. 

Number of samples: 261328 

Number of features: 16

Problem type: Multi-class classification

# Models Used -
| ML Model            | Accuracy | AUC      | Precision | Recall   | Macro-F1 | MCC      |
| ------------------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Logistic Regression | 0.4435   | 0.6475   | 0.4844    | 0.3882   | 0.338    | 0.1261   |
| Decision Tree       | 0.5303   | 0.6573   | 0.5328    | 0.5113   | 0.4972   | 0.285    |
| KNN                 | 0.4675   | 0.6322   | 0.4665    | 0.4337   | 0.4248   | 0.1701   |
| Naive Bayes         | 0.3013   | 0.6353   | 0.5563    | 0.3657   | 0.2124   | 0.093    |
| Random Forest       | 0.5445   | 0.722    | 0.5482    | 0.5231   | 0.5157   | 0.302    |
| XGBoost             | 0.5133   | 0.7208   | 0.5986    | 0.4637   | 0.4419   | 0.2491   |

Model	Observation -

Logistic Regression: Simple baseline, fast but limited by linearity, likely underfitting

Decision Tree:	Good interpretability, but overfits, sensitive to data splits

KNN:	Sensitive to high dimensionality, not preferred for large datasets like this one since it is taking huge time to predict

Naive Bayes:	Fast but independent assumption limits accuracy, high precision but very low recall leads to biased predictions

Random Forest:	Best overall performance, robust to overfitting, stable, good Precision–Recall balance, highest MCC and F1 score

XGBoost:	Strong performance, good class discrimination

Best Model: Random Forest achieved the best overall performance with the highest macro-F1 score.
