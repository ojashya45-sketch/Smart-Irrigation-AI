
import streamlit as st
import pandas as pd
import joblib

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Irrigation AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

    /* FIX: Main page text and widget labels */
    [data-testid="stMain"] {
        color: #1f2937 !important;
    }

    [data-testid="stMain"] [data-testid="stWidgetLabel"],
    [data-testid="stMain"] [data-testid="stWidgetLabel"] *,
    [data-testid="stMain"] label,
    [data-testid="stMain"] .stMarkdown,
    [data-testid="stMain"] .stMarkdown p,
    [data-testid="stMain"] .stCaption,
    [data-testid="stMain"] [data-testid="stCaptionContainer"],
    [data-testid="stMain"] [data-testid="stCaptionContainer"] * {
        color: #1f2937 !important;
    }

    /* Number input fields */
    [data-testid="stMain"] [data-testid="stNumberInput"] input {
        color: #ffffff !important;
        background-color: #262730 !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    /* Number input buttons */
    [data-testid="stMain"] [data-testid="stNumberInput"] button {
        color: #ffffff !important;
    }

    /* Dropdown selected values */
    [data-testid="stMain"] [data-baseweb="select"] {
        color: #1f2937 !important;
    }

    [data-testid="stMain"] [data-baseweb="select"] input {
        color: #1f2937 !important;
        -webkit-text-fill-color: #1f2937 !important;
    }

    /* Dropdown menu and options */
    [data-testid="stMain"] [role="listbox"],
    [data-testid="stMain"] [role="option"] {
        color: #1f2937 !important;
        background-color: #ffffff !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #103f1b;
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        min-height: 50px;
        font-size: 18px;
        font-weight: 700;
        background-color: #176b2c;
        color: #ffffff !important;
        border: none;
    }

    .stButton > button:hover {
        background-color: #0f5120;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. LOAD MACHINE LEARNING COMPONENTS
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

except FileNotFoundError:
    st.error("❌ Required ML model file was not found.")

    st.info(
        "Make sure these files are present in the same folder "
        "as app.py:"
    )

    st.code("""
smote_random_forest.pkl
preprocessor.pkl
label_encoder.pkl
""")

    st.stop()

except Exception as e:
    st.error("❌ Error loading the machine learning model.")
    st.exception(e)
    st.stop()

# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("🌱 **Smart Irrigation**")

    st.divider()

    st.subheader("📌 About")

    st.write(
        "This application uses Machine Learning "
        "to predict the irrigation requirement of "
        "a crop using soil, weather, crop and "
        "previous irrigation data."
    )

    st.divider()

    st.subheader("🤖 Machine Learning")
    st.write("Random Forest + SMOTE")

    st.divider()

    st.subheader("💧 Prediction Classes")
    st.write("🟢 Low")
    st.write("🟡 Medium")
    st.write("🔴 High")

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
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 8. FIELD & ENVIRONMENTAL CONDITIONS
# ============================================================

st.markdown(
    '<div class="section-title">'
    '📊 Field & Environmental Conditions'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    soil_moisture = st.number_input(
        "💧 Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=25.0,
        step=0.5
    )

with col2:
    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=-10.0,
        max_value=60.0,
        value=32.0,
        step=0.5
    )

with col3:
    humidity = st.number_input(
        "💨 Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=55.0,
        step=0.5
    )

col4, col5 = st.columns(2)

with col4:
    rainfall = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=0.0,
        value=2.0,
        step=0.5
    )

with col5:
    previous_irrigation = st.number_input(
        "🚿 Previous Irrigation (mm)",
        min_value=0.0,
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

with crop_col1:
    crop_type = st.selectbox(
        "🌾 Crop Type",
        ["Wheat", "Rice", "Maize"]
    )

with crop_col2:
    growth_stage = st.selectbox(
        "🌱 Crop Growth Stage",
        ["Sowing", "Vegetative", "Flowering", "Harvest"]
    )

with crop_col3:
    season = st.selectbox(
        "☀️ Season",
        ["Kharif", "Rabi", "Zaid"]
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
        # Create input DataFrame
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

        # Preprocess input
        input_encoded = preprocessor.transform(input_data)

        # Machine learning prediction
        prediction = model.predict(input_encoded)

        # Convert encoded prediction to label
        prediction_label = label_encoder.inverse_transform(
            prediction
        )[0]

        # Display prediction heading
        st.markdown(
            '<div class="section-title">'
            '🎯 Prediction Result'
            '</div>',
            unsafe_allow_html=True
        )

        if prediction_label == "High":
            st.error("🔴 HIGH Irrigation Requirement")

            st.write(
                "The model predicts that the crop may "
                "require a high amount of irrigation."
            )

        elif prediction_label == "Medium":
            st.warning("🟡 MEDIUM Irrigation Requirement")

            st.write(
                "The model predicts that the crop may "
                "require a moderate amount of irrigation."
            )

        elif prediction_label == "Low":
            st.success("🟢 LOW Irrigation Requirement")

            st.write(
                "The model predicts that the crop may "
                "require a low amount of irrigation."
            )

        else:
            st.info(
                f"💧 Predicted Irrigation Requirement: "
                f"{prediction_label}"
            )

        # Show entered values
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
        st.error("❌ Prediction could not be completed.")

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
)