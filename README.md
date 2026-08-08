# Loan_Prediction_app
🤖 Interactive Loan Prediction Web App built with Python, Streamlit, and Machine Learning. Uses the KNN classification algorithm and StandardScaler to predict loan approval based on income, credit score, loan amount, dependents, and education, with an interactive Light/Dark theme UI.


## ▶️ How to Run the App

### 1. Clone the Repository


git clone https://github.com/Namanfalke/Loan_Prediction_app/tree/main


### 2. Open the Project Folder

cd KNN-Loan-Prediction


### 3. Create a Virtual Environment


python -m venv venv


### 4. Activate the Virtual Environment

**Windows:**


venv\Scripts\activate


### 5. Install Required Libraries


pip install -r requirements.txt


### 6. Run the Streamlit Application


streamlit run app.py


### 7. Open in Browser

After running the command, Streamlit will provide a local URL such as:


http://localhost:8501


Open this URL in your browser to use the application.

### 📁 Project Structure

KNN-Loan-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
└── saved model/
    ├── KNN_model.pkl
    └── StandardScaler.pkl

> **Note:** Make sure the `saved model` folder and both `.pkl` files are present in the repository. The application needs them to load the trained KNN model and StandardScaler.
