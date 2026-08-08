# import streamlit as st
# import pandas as pd
# import joblib

# knn=joblib.load(r"C:\Users\yashk\OneDrive\Desktop\Naman ML\Streamelit\P1\saved model\KNN_model.pkl")
# ss=joblib.load(r'C:\Users\yashk\OneDrive\Desktop\Naman ML\Streamelit\P1\saved model\StandardScaler.pkl')


# st.set_page_config(
#     page_title="KNN Prediction App",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("My first projct on streamlit")

# #Annual_Income	Credit_Score	Loan_Amount	Dependents	Education

# Annual_income = st.number_input("Enter ur annual salery",min_value=0)
# Credit_score = st.number_input("Enter ur credit score",min_value=0)
# Loan_amount = st.number_input("Enter ur loan amount",min_value=0)
# Dependents = st.number_input("Number od dependents",min_value=0,max_value=20)
# Education = st.number_input("Education for non_graduate == 1, graduate == 0",min_value=0,max_value=1)

# input_data=[Annual_income,Credit_score,Loan_amount,Dependents,Education]
# scalled_input=ss.transform([input_data])




# if st.button("Submit"):
#     # st.write(scalled_input)
#     prediction=knn.predict(scalled_input)
#     st.write(prediction)



#_______________________________________________________

import streamlit as st
import pandas as pd
import joblib



# ==========================================================
# LOAD MODEL AND SCALER
# ==========================================================

knn = joblib.load("KNN_model.pkl")

ss = joblib.load("StandardScaler.pkl")


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="KNN Loan Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# SESSION STATE FOR THEME
# ==========================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙️ Settings")

    # Theme switch
    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

    st.session_state.dark_mode = dark_mode

    st.divider()

    st.header("📌 About This App")

    st.write("""
    This application uses a **K-Nearest Neighbors (KNN)**
    machine learning model to predict loan outcomes.

    The input values are automatically standardized using
    the saved **StandardScaler** before making the prediction.
    """)

    st.divider()

    st.subheader("📊 Features Used")

    st.write("💰 Annual Income")
    st.write("💳 Credit Score")
    st.write("🏦 Loan Amount")
    st.write("👨‍👩‍👧 Dependents")
    st.write("🎓 Education")

    st.divider()

    st.subheader("⚙️ Model")

    st.write("Algorithm: **K-Nearest Neighbors**")
    st.write("Preprocessing: **StandardScaler**")

    st.divider()

    st.caption("Built with Python + Streamlit")


# ==========================================================
# DARK / LIGHT THEME COLORS
# ==========================================================

if st.session_state.dark_mode:

    background = "#0E1117"
    card_background = "#1E2430"
    text_color = "#FFFFFF"
    secondary_text = "#B8C0CC"
    border_color = "#303846"

else:

    background = "#F5F7FB"
    card_background = "#FFFFFF"
    text_color = "#1F2937"
    secondary_text = "#666666"
    border_color = "#E5E7EB"


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       MAIN APP
       ===================================================== */

    .stApp {{
        background-color: {background};
        color: {text_color};
    }}


    /* =====================================================
       MAIN TITLE
       ===================================================== */

    .main-title {{
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        color: {text_color};
        margin-bottom: 5px;
    }}


    /* =====================================================
       SUBTITLE
       ===================================================== */

    .subtitle {{
        text-align: center;
        color: {secondary_text};
        font-size: 18px;
        margin-bottom: 30px;
    }}


    /* =====================================================
       INPUT BOX
       ===================================================== */

    .input-box {{
        background-color: {card_background};
        padding: 25px;
        border-radius: 15px;
        border: 1px solid {border_color};
        box-shadow: 0px 4px 15px rgba(0,0,0,0.10);
        margin-bottom: 20px;
    }}


    /* =====================================================
       TEXT
       ===================================================== */

    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
    }}

    p, label {{
        color: {text_color};
    }}


    /* =====================================================
       INPUT FIELDS
       ===================================================== */

    div[data-baseweb="input"] {{
        background-color: {card_background};
    }}

    div[data-baseweb="select"] > div {{
        background-color: {card_background};
    }}


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {{
        text-align: center;
        color: {secondary_text};
        margin-top: 40px;
        font-size: 14px;
    }}


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {{
        background-color: {card_background};
    }}


    /* =====================================================
       BUTTON
       ===================================================== */

    div.stButton > button {{
        border-radius: 10px;
        height: 50px;
        font-size: 17px;
        font-weight: 600;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">🤖 KNN Loan Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict loan approval using a Machine Learning model'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown(
    '<div class="input-box">',
    unsafe_allow_html=True
)

st.subheader("📝 Applicant Details")

st.write("Enter the applicant information below.")


# ==========================================================
# ROW 1
# ==========================================================

col1, col2 = st.columns(2)


with col1:

    Annual_income = st.number_input(
        "💰 Annual Income",
        min_value=0.0,
        value=500000.0,
        step=10000.0,
        help="Enter annual income."
    )


with col2:

    Credit_score = st.number_input(
        "💳 Credit Score",
        min_value=0,
        max_value=900,
        value=700,
        step=1,
        help="Enter credit score."
    )


# ==========================================================
# ROW 2
# ==========================================================

col3, col4 = st.columns(2)


with col3:

    Loan_amount = st.number_input(
        "🏦 Loan Amount",
        min_value=0.0,
        value=200000.0,
        step=10000.0,
        help="Enter requested loan amount."
    )


with col4:

    Dependents = st.number_input(
        "👨‍👩‍👧 Number of Dependents",
        min_value=0,
        max_value=20,
        value=0,
        step=1,
        help="Enter number of dependents."
    )


# ==========================================================
# ROW 3
# ==========================================================

col5, col6 = st.columns(2)


with col5:

    Education = st.selectbox(
        "🎓 Education",
        options=[0, 1],
        format_func=lambda x:
            "Graduate" if x == 0 else "Non-Graduate"
    )


with col6:

    st.info("""
    **Education Encoding**

    🎓 Graduate → `0`

    🎓 Non-Graduate → `1`
    """)


st.markdown("</div>", unsafe_allow_html=True)


# ==========================================================
# CREATE INPUT DATA
# ==========================================================

input_data = [
    Annual_income,
    Credit_score,
    Loan_amount,
    Dependents,
    Education
]


# ==========================================================
# CREATE DATAFRAME
# ==========================================================
# IMPORTANT:
# These names MUST match the names used when the scaler
# was trained.

input_df = pd.DataFrame(
    [input_data],
    columns=[
        "Annual_Income",
        "Credit_Score",
        "Loan_Amount",
        "Dependents",
        "Labelled_Education"
    ]
)


# ==========================================================
# PREDICT BUTTON
# ==========================================================

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])


with col2:

    predict_button = st.button(
        "🔮 Predict Loan",
        use_container_width=True,
        type="primary"
    )


# ==========================================================
# PREDICTION
# ==========================================================

if predict_button:

    try:

        # --------------------------------------------------
        # STANDARD SCALING
        # --------------------------------------------------

        scaled_input = ss.transform(input_df)


        # --------------------------------------------------
        # KNN PREDICTION
        # --------------------------------------------------

        prediction = knn.predict(scaled_input)

        result = prediction[0]


        # --------------------------------------------------
        # RESULT
        # --------------------------------------------------

        st.divider()

        st.subheader("🎯 Prediction Result")


        # Assuming:
        # 1 = Approved
        # 0 = Not Approved

        if result == 1:

            st.success(
                "🎉 Loan Prediction: APPROVED"
            )

            st.balloons()


        elif result == 0:

            st.error(
                "❌ Loan Prediction: NOT APPROVED"
            )


        else:

            st.info(
                f"🤖 Model Prediction: {result}"
            )


        # --------------------------------------------------
        # VIEW INPUT DATA
        # --------------------------------------------------

        with st.expander("🔍 View Input Data"):

            st.write("### Original Input")

            st.dataframe(
                input_df,
                use_container_width=True
            )


        # --------------------------------------------------
        # VIEW SCALED DATA
        # --------------------------------------------------

        with st.expander("📊 View Standard Scaled Data"):

            scaled_df = pd.DataFrame(
                scaled_input,
                columns=input_df.columns
            )

            st.dataframe(
                scaled_df,
                use_container_width=True
            )


        # --------------------------------------------------
        # VIEW MODEL OUTPUT
        # --------------------------------------------------

        with st.expander("🤖 View Model Output"):

            st.write("Raw prediction:", prediction)

            st.write("Prediction value:", result)


    except Exception as e:

        st.error(
            f"❌ Prediction Error: {e}"
        )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">
        🤖 KNN Machine Learning Project
        | Built using Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
