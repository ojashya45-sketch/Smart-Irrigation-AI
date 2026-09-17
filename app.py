
import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Smart Irrigation AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

    .stApp {
        background-color: #eef5ee;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1 {
        color: #1b5e20;
    }

    h2, h3 {
        color: #1b5e20;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .result {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        background-color: white;
        border: 1px solid #cfdccf;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        color: #536458;
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

    st.title("🌱 Smart Irrigation")

    st.divider()

    st.subheader("📌 About")

    st.write(
        "This application uses Machine Learning to predict "
        "the irrigation requirement of a crop using soil, "
        "weather, crop and previous irrigation data."
    )

    st.divider()

    st.subheader("🤖 Machine Learning")

    st.write("Random Forest + SMOTE")

    st.divider()

    st.subheader("💧 Prediction Classes")

    st.write("🟢 Low")
    st.write("🟡 Medium")
    st.write("🔴 High")

    st.divider()

    st.caption("Smart Agriculture • ML Project")

# =========================================================
# HEADER
# =========================================================

st.title("🌱 Smart Irrigation AI")

st.markdown(
    "<div class='subtitle'>"
    "AI-Based Irrigation Requirement Prediction System"
    "</div>",
    unsafe_allow_html=True
)

st.info(
    "💡 Enter the current field and crop conditions. "
    "The machine learning model will predict whether "
    "the irrigation requirement is Low, Medium, or High."
)

# =========================================================
# FIELD CONDITIONS
# =========================================================

st.header("📊 Field & Environmental Conditions")

col1, col2, col3 = st.columns(3)

with col1:

    soil_moisture = st.number_input(
        "💧 Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=25.0,
        step=1.0
    )

with col2:

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=-10.0,
        max_value=60.0,
        value=32.0,
        step=1.0
    )

with col3:

    humidity = st.number_input(
        "💨 Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=55.0,
        step=1.0
    )

col4, col5 = st.columns(2)

with col4:

    rainfall = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=2.0,
        step=1.0
    )

with col5:

    previous_irrigation = st.number_input(
        "🚿 Previous Irrigation (mm)",
        min_value=0.0,
        max_value=500.0,
        value=10.0,
        step=1.0
    )

# =========================================================
# CROP INFORMATION
# =========================================================

st.header("🌾 Crop Information")

crop_col1, crop_col2, crop_col3 = st.columns(3)

with crop_col1:

    crop_type = st.selectbox(
        "🌾 Crop Type",
        [
            "Wheat",
            "Rice",
            "Maize"
        ]
    )

with crop_col2:

    growth_stage = st.selectbox(
        "🌱 Crop Growth Stage",
        [
            "Sowing",
            "Vegetative",
            "Flowering",
            "Harvest"
        ]
    )

with crop_col3:

    season = st.selectbox(
        "☀️ Season",
        [
            "Kharif",
            "Rabi",
            "Zaid"
        ]
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

    # Preprocess

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
            "for the given conditions."
        )

    elif prediction_label == "Medium":

        st.warning(
            "🟡 MEDIUM Irrigation Requirement"
        )

        st.write(
            "The model predicts a medium irrigation requirement "
            "for the given conditions."
        )

    else:

        st.success(
            "🟢 LOW Irrigation Requirement"
        )

        st.write(
            "The model predicts a low irrigation requirement "
            "for the given conditions."
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
)