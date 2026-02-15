
import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    confusion_matrix,
    classification_report
)

st.title("Mental Health Care Options")

@st.cache_data
def load_sample_data():
    return pd.read_csv("data/Mental Health Dataset.csv") 

sample_df = load_sample_data()

st.subheader("Download Sample Dataset")

csv_sample = sample_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sample Dataset",
    data=csv_sample,
    file_name="Mental Health Dataset.csv",
    mime="text/csv"
)

uploaded_file = st.file_uploader("Upload data for predictions (CSV)", type="csv")

model_name = st.selectbox(
    "Select Model",
    ["Logistic Regression", "Decision Tree", "KNN",
     "Naive Bayes", "Random Forest", "XGBoost"]
)

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    model = joblib.load(f"model/{model_name}.pkl")
    label_encoder = joblib.load("model/label_encoder.pkl")
    if "CareOptions" in data.columns:
        X_test = data.drop("CareOptions", axis=1)
        y_true = label_encoder.transform(data["CareOptions"])
    else:
        X_test = data
        y_true = None
        
    predictions = model.predict(X_test)
    inverse_encoded_predictions = label_encoder.inverse_transform(predictions)

    data["CareOptions"] = inverse_encoded_predictions

    st.subheader("Predictions")
    st.dataframe(data)

    if y_true is not None:
        st.subheader("Evaluation Metrics")
        accuracy = accuracy_score(y_true, predictions)
        if len(np.unique(y_true)) == 2:
            y_prob = model.predict_proba(X_test)[:, 1]
            auc = roc_auc_score(y_true, y_prob)
        else:
            y_prob = model.predict_proba(X_test)
            auc = roc_auc_score(y_true, y_prob, multi_class="ovr")

        precision = precision_score(y_true, predictions, average="macro")
        recall = recall_score(y_true, predictions, average="macro")
        f1 = f1_score(y_true, predictions, average="macro")
        matcorcoeff = matthews_corrcoef(y_true, predictions)

        st.write("Accuracy:", round(accuracy, 4))
        st.write("AUC:", round(auc, 4))
        st.write("Precision:", round(precision, 4))
        st.write("Recall:", round(recall, 4))
        st.write("F1 Score:", round(f1, 4))
        st.write("MCC Score:", round(matcorcoeff, 4))

        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_true, predictions)
        st.write(cm)

        st.subheader("Classification Report")
        st.text(classification_report(y_true, predictions))
