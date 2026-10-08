<<<<<<< HEAD
=======

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
import streamlit as st
import pandas as pd
import joblib

<<<<<<< HEAD

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================
=======
# =========================================================
# PAGE CONFIG
# =========================================================
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b

st.set_page_config(
    page_title="Smart Irrigation AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

<<<<<<< HEAD

# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f4f8f3;
    }

    /* Main title */
    .main-title {
        font-size: 46px;
        font-weight: 800;
        color: #176b2c;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #48624d;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 30px;
        font-weight: 700;
        color: #176b2c;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Information box */
    .info-box {
        background-color: white;
        border: 1px solid #d7e5d8;
        border-radius: 15px;
        padding: 22px;
        margin-bottom: 25px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }

    .info-title {
        font-size: 23px;
        font-weight: 700;
        color: #176b2c;
    }

    .info-text {
        font-size: 17px;
        color: #405246;
        line-height: 1.6;
    }

    /* Prediction result */
    .result-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
    }

    .result-title {
        font-size: 32px;
        font-weight: 800;
    }

    .result-description {
        font-size: 18px;
        margin-top: 8px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #103f1b;
=======
# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    model = joblib.load("smote_random_forest.pkl")
    preprocessor = joblib.load("preprocessor.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
    return model, preprocessor, label_encoder


model, preprocessor, label_encoder = load_model()

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */
    .stApp {
        background-color: #eef5ee;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* HEADINGS */
    h1 {
        color: #1b5e20 !important;
        font-weight: 800 !important;
    }

    h2, h3 {
        color: #1b5e20 !important;
    }

    /* NORMAL TEXT */
    p {
        color: #26352a;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #173b1a;
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

<<<<<<< HEAD
    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-size: 18px;
        font-weight: 700;
        background-color: #176b2c;
        color: white;
=======
    section[data-testid="stSidebar"] hr {
        border-color: #5d8060;
    }

    /* INPUT LABELS */
    label {
        color: #26352a !important;
        font-weight: 600 !important;
    }

    /* INPUT BOXES */
    div[data-baseweb="input"] {
        background-color: white;
        border-radius: 10px;
    }

    div[data-baseweb="input"] input {
        color: #1f2933 !important;
        background-color: white !important;
    }

    /* SELECT BOX */
    div[data-baseweb="select"] {
        background-color: white;
        border-radius: 10px;
    }

    div[data-baseweb="select"] * {
        color: #1f2933 !important;
    }

    /* BUTTON */
    .stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 700;
        background-color: #2e7d32;
        color: white !important;
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
        border: none;
    }

    .stButton > button:hover {
<<<<<<< HEAD
        background-color: #0f5120;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. LOAD ML COMPONENTS
# ============================================================

@st.cache_resource
def load_models():

    model = joblib.load("smote_random_forest.pkl")
    preprocessor = joblib.load("preprocessor.pkl")
    label_encoder = joblib.load("label_encoder.pkl")

    return model, preprocessor, label_encoder


# ============================================================
# 4. LOAD MODEL WITH ERROR HANDLING
# ============================================================

try:

    model, preprocessor, label_encoder = load_models()

except FileNotFoundError as e:

    st.error(
        "❌ Required ML model file was not found."
    )

    st.info(
        "Make sure these files are present in the same folder as app.py:"
    )

    st.code(
        """
smote_random_forest.pkl
preprocessor.pkl
label_encoder.pkl
        """
    )

    st.stop()

except Exception as e:

    st.error("❌ Error loading the machine learning model.")

    st.exception(e)

    st.stop()


# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "🌱 **Smart Irrigation**"
    )

    st.divider()

    st.subheader("📌 About")

    st.write(
        "This application uses Machine Learning "
        "to predict the irrigation requirement of "
        "a crop using soil, weather, crop and "
        "previous irrigation data."
=======
        background-color: #1b5e20;
        color: white !important;
    }

    /* INFO BOX */
    .intro-box {
        background-color: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #cfdccf;
        margin-bottom: 20px;
    }

    .intro-title {
        color: #1b5e20;
        font-size: 22px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    /* FOOTER */
    .footer {
        text-align: center;
        color: #536458;
        font-size: 14px;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #c8d5c8;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌱 Smart Irrigation")

    st.divider()

    st.markdown("### 📌 About")

    st.write(
        "This application uses Machine Learning to predict "
        "the irrigation requirement of a crop using soil, "
        "weather, crop and previous irrigation data."
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
    )

    st.divider()

<<<<<<< HEAD
    st.subheader("🤖 Machine Learning")
=======
    st.markdown("### 🤖 Machine Learning")
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b

    st.write("Random Forest + SMOTE")

    st.divider()

<<<<<<< HEAD
    st.subheader("💧 Prediction Classes")
=======
    st.markdown("### 💧 Prediction Classes")
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b

    st.write("🟢 Low")
    st.write("🟡 Medium")
    st.write("🔴 High")

<<<<<<< HEAD

# ============================================================
# 6. APPLICATION HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌱 Smart Irrigation AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Based Irrigation Requirement Prediction System'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 7. INFORMATION SECTION
# ============================================================

st.markdown(
    """
    <div class="info-box">
        <div class="info-title">
            💡 Irrigation Decision Support
        </div>
        <div class="info-text">
            Enter the current field and crop conditions below.
            The machine learning model will predict the expected
            irrigation requirement as Low, Medium, or High.
        </div>
=======
    st.divider()

    st.caption("Smart Agriculture • ML Project")

# =========================================================
# HEADER
# =========================================================

st.title("🌱 Smart Irrigation AI")

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:19px;
        color:#455a46;
        margin-bottom:25px;
    ">
    AI-Based Irrigation Requirement Prediction System
    </p>
    """,
    unsafe_allow_html=True
)

# =========================================================
# INTRODUCTION
# =========================================================

st.markdown(
    """
    <div class="intro-box">
        <div class="intro-title">
            💡 Irrigation Decision Support
        </div>

        <p>
        Enter the current field and crop conditions below.
        The machine learning model will predict the expected
        irrigation requirement as <b>Low</b>, <b>Medium</b>,
        or <b>High</b>.
        </p>
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
    </div>
    """,
    unsafe_allow_html=True
)

<<<<<<< HEAD

# ============================================================
# 8. FIELD & ENVIRONMENTAL CONDITIONS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Field & Environmental Conditions</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


=======
# =========================================================
# FIELD CONDITIONS
# =========================================================

st.header("📊 Field & Environmental Conditions")

col1, col2, col3 = st.columns(3)

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with col1:

    soil_moisture = st.number_input(
        "💧 Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=25.0,
<<<<<<< HEAD
        step=0.5
    )


=======
        step=1.0
    )

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with col2:

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=-10.0,
        max_value=60.0,
        value=32.0,
<<<<<<< HEAD
        step=0.5
    )


=======
        step=1.0
    )

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with col3:

    humidity = st.number_input(
        "💨 Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=55.0,
<<<<<<< HEAD
        step=0.5
    )


col4, col5 = st.columns(2)


=======
        step=1.0
    )

col4, col5 = st.columns(2)

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with col4:

    rainfall = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=0.0,
<<<<<<< HEAD
        value=2.0,
        step=0.5
    )


=======
        max_value=500.0,
        value=2.0,
        step=1.0
    )

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with col5:

    previous_irrigation = st.number_input(
        "🚿 Previous Irrigation (mm)",
        min_value=0.0,
<<<<<<< HEAD
        value=10.0,
        step=0.5
    )


# ============================================================
# 9. CROP INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🌾 Crop Information</div>',
    unsafe_allow_html=True
)

crop_col1, crop_col2, crop_col3 = st.columns(3)


=======
        max_value=500.0,
        value=10.0,
        step=1.0
    )

# =========================================================
# CROP INFORMATION
# =========================================================

st.header("🌾 Crop Information")

crop_col1, crop_col2, crop_col3 = st.columns(3)

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with crop_col1:

    crop_type = st.selectbox(
        "🌾 Crop Type",
<<<<<<< HEAD
        [
            "Wheat",
            "Rice",
            "Maize"
        ]
    )


=======
        ["Wheat", "Rice", "Maize"]
    )

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with crop_col2:

    growth_stage = st.selectbox(
        "🌱 Crop Growth Stage",
<<<<<<< HEAD
        [
            "Sowing",
            "Vegetative",
            "Flowering",
            "Harvest"
        ]
    )


=======
        ["Sowing", "Vegetative", "Flowering", "Harvest"]
    )

>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
with crop_col3:

    season = st.selectbox(
        "☀️ Season",
<<<<<<< HEAD
        [
            "Kharif",
            "Rabi",
            "Zaid"
        ]
    )


# ============================================================
# 10. PREDICTION BUTTON
# ============================================================

st.write("")

predict_button = st.button(
    "🔍 Predict Irrigation Requirement"
)


# ============================================================
# 11. PREDICTION
# ============================================================

if predict_button:

    try:

        # ----------------------------------------------------
        # Create input DataFrame
        # ----------------------------------------------------

        input_data = pd.DataFrame({

            "Soil_Moisture": [
                soil_moisture
            ],

            "Temperature_C": [
                temperature
            ],

            "Humidity": [
                humidity
            ],

            "Rainfall_mm": [
                rainfall
            ],

            "Crop_Type": [
                crop_type
            ],

            "Crop_Growth_Stage": [
                growth_stage
            ],

            "Season": [
                season
            ],

            "Previous_Irrigation_mm": [
                previous_irrigation
            ]

        })


        # ----------------------------------------------------
        # Preprocess input
        # ----------------------------------------------------

        input_encoded = preprocessor.transform(
            input_data
        )


        # ----------------------------------------------------
        # Machine Learning prediction
        # ----------------------------------------------------

        prediction = model.predict(
            input_encoded
        )


        # ----------------------------------------------------
        # Convert encoded prediction to label
        # ----------------------------------------------------

        prediction_label = label_encoder.inverse_transform(
            prediction
        )[0]


        # ----------------------------------------------------
        # Display prediction
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">🎯 Prediction Result</div>',
            unsafe_allow_html=True
        )


        if prediction_label == "High":

            st.error(
                "🔴 HIGH Irrigation Requirement"
            )

            st.write(
                "The model predicts that the crop may "
                "require a high amount of irrigation."
            )


        elif prediction_label == "Medium":

            st.warning(
                "🟡 MEDIUM Irrigation Requirement"
            )

            st.write(
                "The model predicts that the crop may "
                "require a moderate amount of irrigation."
            )


        elif prediction_label == "Low":

            st.success(
                "🟢 LOW Irrigation Requirement"
            )

            st.write(
                "The model predicts that the crop may "
                "require a low amount of irrigation."
            )


        else:

            st.info(
                f"💧 Predicted Irrigation Requirement: "
                f"{prediction_label}"
            )


        # ----------------------------------------------------
        # Show entered values
        # ----------------------------------------------------

        st.subheader("📋 Input Summary")

        display_data = pd.DataFrame({
            "Parameter": [
                "Soil Moisture",
                "Temperature",
                "Humidity",
                "Rainfall",
                "Previous Irrigation",
                "Crop Type",
                "Growth Stage",
                "Season"
            ],

            "Value": [
                f"{soil_moisture:.1f} %",
                f"{temperature:.1f} °C",
                f"{humidity:.1f} %",
                f"{rainfall:.1f} mm",
                f"{previous_irrigation:.1f} mm",
                crop_type,
                growth_stage,
                season
            ]
        })

        st.table(display_data)


    except Exception as e:

        st.error(
            "❌ Prediction could not be completed."
        )

        st.write(
            "Please check that the input column names and "
            "model preprocessing configuration match the "
            "training data."
        )

        st.exception(e)


# ============================================================
# 12. FOOTER
# ============================================================

st.divider()

st.caption(
    "🌱 Smart Irrigation AI • Machine Learning based "
    "Irrigation Requirement Prediction System"
=======
        ["Kharif", "Rabi", "Zaid"]
    )

# =========================================================
# BUTTONS
# =========================================================

st.write("")

predict_col, reset_col = st.columns([3, 1])

with predict_col:

    predict_button = st.button(
        "🔍 Predict Irrigation Requirement",
        use_container_width=True
    )

with reset_col:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )

if reset_button:
    st.rerun()

# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = pd.DataFrame({
        "Soil_Moisture": [soil_moisture],
        "Temperature_C": [temperature],
        "Humidity": [humidity],
        "Rainfall_mm": [rainfall],
        "Crop_Type": [crop_type],
        "Crop_Growth_Stage": [growth_stage],
        "Season": [season],
        "Previous_Irrigation_mm": [previous_irrigation]
    })

    # Preprocessing
    input_encoded = preprocessor.transform(input_data)

    # Prediction
    prediction = model.predict(input_encoded)

    prediction_label = label_encoder.inverse_transform(
        prediction
    )[0]

    # =====================================================
    # RESULT
    # =====================================================

    st.header("💧 Prediction Result")

    if prediction_label == "High":

        st.error(
            "🔴 HIGH Irrigation Requirement"
        )

        st.write(
            "The model predicts a high irrigation requirement "
            "for the given field conditions."
        )

    elif prediction_label == "Medium":

        st.warning(
            "🟡 MEDIUM Irrigation Requirement"
        )

        st.write(
            "The model predicts a medium irrigation requirement "
            "for the given field conditions."
        )

    else:

        st.success(
            "🟢 LOW Irrigation Requirement"
        )

        st.write(
            "The model predicts a low irrigation requirement "
            "for the given field conditions."
        )

    # =====================================================
    # FIELD SUMMARY
    # =====================================================

    st.header("📋 Field Summary")

    summary1, summary2, summary3, summary4 = st.columns(4)

    with summary1:
        st.metric(
            "Soil Moisture",
            f"{soil_moisture:.0f}%"
        )

    with summary2:
        st.metric(
            "Temperature",
            f"{temperature:.0f}°C"
        )

    with summary3:
        st.metric(
            "Rainfall",
            f"{rainfall:.0f} mm"
        )

    with summary4:
        st.metric(
            "Humidity",
            f"{humidity:.0f}%"
        )

    # =====================================================
    # MODEL CONFIDENCE
    # =====================================================

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            input_encoded
        )[0]

        confidence = max(probabilities) * 100

        st.header("🤖 Model Confidence")

        st.progress(
            min(int(confidence), 100)
        )

        st.write(
            f"Estimated model confidence: "
            f"**{confidence:.1f}%**"
        )

        st.caption(
            "This is the model's probability estimate and "
            "should not be interpreted as a guarantee."
        )

    # =====================================================
    # INPUT DETAILS
    # =====================================================

    with st.expander("🔎 View Input Details"):

        st.dataframe(
            input_data,
            use_container_width=True,
            hide_index=True
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    🌱 <b>Smart Irrigation AI</b><br><br>

    Machine Learning Based Agricultural Decision Support Prototype<br>

    Python • Scikit-learn • Streamlit

    </div>
    """,
    unsafe_allow_html=True
>>>>>>> 6acd8cc4fac5c71ce62a8f9830804117c23c634b
)