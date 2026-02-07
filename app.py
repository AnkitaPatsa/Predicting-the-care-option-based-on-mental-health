{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d3bae6d0-19ee-4c3c-bdef-ec1d14d0e076",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in ./anaconda3/lib/python3.12/site-packages (1.54.0)\n",
      "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: blinker<2,>=1.5.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<7,>=5.5 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (6.2.6)\n",
      "Requirement already satisfied: click<9,>=7.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (3.1.46)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging>=20 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (2.2.3)\n",
      "Requirement already satisfied: pillow<13,>=7.1.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: protobuf<7,>=3.20 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (23.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (9.1.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.10.0 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in ./anaconda3/lib/python3.12/site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in ./anaconda3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in ./anaconda3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: narwhals>=1.27.1 in ./anaconda3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.16.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in ./anaconda3/lib/python3.12/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in ./anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in ./anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in ./anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in ./anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in ./anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in ./anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2024.12.14)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in ./anaconda3/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in ./anaconda3/lib/python3.12/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in ./anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in ./anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in ./anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: six>=1.5 in ./anaconda3/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de0c7353-5118-43ef-9191-497f9fa59751",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4d488f94-0da6-4f5a-96c6-02d9921da882",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-07 00:06:20.017 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.214 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/cloud/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-02-07 00:06:20.215 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.216 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.219 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.219 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.220 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.221 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.221 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.222 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.223 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.223 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.224 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.225 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.226 Session state does not function when running a script without `streamlit run`\n",
      "2026-02-07 00:06:20.227 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.227 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-07 00:06:20.228 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.title(\"Mental Health Care Options Classifications\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Upload your data (CSV)\", type=\"csv\")\n",
    "\n",
    "model_name = st.selectbox(\n",
    "    \"Select Model\",\n",
    "    [\"Logistic Regression\", \"Decision Tree\", \"KNN\",\n",
    "     \"Naive Bayes\", \"Random Forest\", \"XGBoost\"]\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b99068b8-6321-456d-af3e-61524aabdf21",
   "metadata": {},
   "outputs": [],
   "source": [
    "if uploaded_file:\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "    st.write(data.head())\n",
    "\n",
    "    model = joblib.load(f\"model/{model_name}.pkl\")\n",
    "    predictions = model.predict(data)\n",
    "\n",
    "    st.write(\"Predictions:\", predictions)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
