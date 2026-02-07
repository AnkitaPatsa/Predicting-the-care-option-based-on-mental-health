# Predicting-the-care-option-based-on-mental-health
# Problem Statement - 
The given dataset is a mental-health-related survey containing multiple categorical attributes such as work environment, stress factors, mood indicators, and personal habits. The target variable chosen for this task is CareOptions, a multi-class label describing what type of mental-health care options an individual prefers.
# Dataset Description -
Dataset Name: Mental Health dataset

Source: https://www.kaggle.com/datasets/alamshihab075/mental-health-dataset?select=Mental+Health+dataset1.csv

Target Variable: CareOptions (Multi-class) 

Features: The dataset contains 16 categorical attributes like Gender, Country, Occupation, Treatment, Family history and many more. Number of samples: 261328 

Number of features: 16

Problem type: Multi-class classification

# Models Used -
| ML Model            | Accuracy | AUC      | Precision | Recall   | Macro-F1 | MCC      |
| ------------------- | -------- | -------- | --------- | -------- | -------- | -------- |
| Logistic Regression | 0.517487 | 0.701264 | 0.520905  | 0.523226 | 0.512503 | 0.285439 |
| Decision Tree       | 0.567214 | 0.756134 | 0.581855  | 0.580963 | 0.563858 | 0.369511 |
| KNN                 | 0.476313 | 0.653783 | 0.463783  | 0.450437 | 0.450961 | 0.185843 |
| Naive Bayes         | 0.296904 | 0.653832 | 0.547721  | 0.366090 | 0.210054 | 0.093074 |
| Random Forest       | 0.579784 | 0.775206 | 0.594611  | 0.594746 | 0.577720 | 0.388198 |
| XGBoost             | 0.606283 | 0.793894 | 0.620544  | 0.578285 | 0.576373 | 0.392964 |

Model	Observation -

Logistic Regression: Simple baseline, fast but limited by linearity

Decision Tree:	Overfits, sensitive to data splits

KNN:	Sensitive to high dimensionality

Naive Bayes:	Fast but independence assumption limits accuracy

Random Forest:	Strong performance, robust to overfitting

XGBoost:	Best overall performance with highest macro-F1

Best Model: XGBoost achieved the best overall performance with the highest macro-F1 score and ROC-AUC.
