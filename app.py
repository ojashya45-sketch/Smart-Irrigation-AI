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

st.markdown("""
<style>

/* =========================
   MAIN PAGE
   ========================= */

.stApp {
    background: #eef5ee;
    color: #1f2933;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* =========================
   HEADER
   ========================= */

.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #1b5e20;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 19px;
    color: #455a46;
    margin-bottom: 30px;
}

/* =========================
   CARDS
   ========================= */

.section-card {
    background: #ffffff;
    padding: 24px;
    border-radius: 18px;
    margin-bottom: 18px;
    border: 1px solid #cfdccf;
    box-shadow: 0 4px 12px rgba(0,0,0,0.07);
}

.section-title {
    font-size: 23px;
    font-weight: 750;
    color: #1b5e20;
    margin-bottom: 10px;
}

/* =========================
   NORMAL TEXT
   ========================= */

p {
    color: #26352a;
}

label {
    color: #26352a !important;
    font-weight: 600 !important;
}

/* =========================
   INPUT BOXES
   ========================= */

div[data-baseweb="input"] {
    background-color: #ffffff;
    border-radius: 10px;
}

div[data-baseweb="input"] input {
    color: #1f2933 !important;
    background-color: #ffffff !important;
}

div[data-baseweb="select"] {
    background-color: #ffffff;
    border-radius: 10px;
}

div[data-baseweb="select"] * {
    color: #1f2933 !important;
}

/* =========================
   BUTTON
   ========================= */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
    background-color: #2e7d32;
    color: white;
    border: none;
}

.stButton > button:hover {
    background-color: #1b5e20;
    color: white;
}

/* =========================
   PREDICTION CARD
   ========================= */

.prediction-box {
    background: #ffffff;
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    margin-top: 25px;
    border: 2px solid #b7cdb7;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.prediction-label {
    font-size: 18px;
    color: #536458;
    margin-bottom: 8px;
}

.prediction-value {
    font-size: 42px;
    font-weight: 800;
    color: #1b5e20;
}

.prediction-description {
    font-size: 17px;
    color: #536458;
}

/* =========================
   INFORMATION CARDS
   ========================= */

.info-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #cfdccf;
    text-align: center;
    margin-top: 10px;
}

.info-number {
    font-size: 27px;
    font-weight: 750;
    color: #1b5e20;
}

.info-label {
    color: #536458;
    font-size: 14px;
}

/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background-color: #173b1a;
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] hr {
    border-color: #5d8060;
}

/* =========================
   EXPANDER
   ========================= */

div[data-testid="stExpander"] {
    background-color: #ffffff;
    border: 1px solid #cfdccf;
    border-radius: 12px;
}

div[data-testid="stExpander"] * {
    color: #26352a;
}

/* =========================
   DATAFRAME
   ========================= */

div[data-testid="stDataFrame"] {
    background-color: white;
}

/* =========================
   FOOTER
   ========================= */

.footer {
    text-align: center;
    color: #536458;
    font-size: 14px;
    margin-top: 45px;
    padding-top: 20px;
    border-top: 1px solid #c8d5c8;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌱 Smart Irrigation")

    st.markdown("---")

    st.markdown("### 📌 About")

    st.write(
        "This application uses Machine Learning to "
        "predict the irrigation requirement of a crop "
        "using soil, weather, crop and previous irrigation data."
    )

    st.markdown("---")

    st.markdown("### 🤖 Machine Learning Model")

    st.write("Random Forest + SMOTE")

    st.markdown("---")

    st.markdown("### 💧 Prediction Classes")

    st.write("🟢 Low")
    st.write("🟡 Medium")
    st.write("🔴 High")

    st.markdown("---")

    st.caption("Smart Agriculture • ML Project")

# =========================================================
# HEADER
# =========================================================

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

# =========================================================
# INTRODUCTION
# =========================================================

st.markdown("""
<div class="section-card">

<div class="section-title">💡 Irrigation Decision Support</div>

<p>
Enter the current field and crop conditions below.
The machine learning model will predict the expected
irrigation requirement as <b>Low</b>, <b>Medium</b>, or <b>High</b>.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# FIELD CONDITIONS
# =========================================================

st.markdown("""
<div class="section-card">
<div class="section-title">📊 Field & Environmental Conditions</div>
</div>
""", unsafe_allow_html=True)

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

st.markdown("""
<div class="section-card">
<div class="section-title">🌾 Crop Information</div>
</div>
""", unsafe_allow_html=True)

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

# =========================================================
# BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

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

# =========================================================
# RESET
# =========================================================

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

    # Transform input
    input_encoded = preprocessor.transform(input_data)

    # Prediction
    prediction = model.predict(input_encoded)

    prediction_label = label_encoder.inverse_transform(
        prediction
    )[0]

    # =====================================================
    # RESULT
    # =====================================================

    if prediction_label == "High":

        result_color = "#b71c1c"
        result_icon = "🔴"
        description = (
            "The model predicts a high irrigation requirement."
        )

    elif prediction_label == "Medium":

        result_color = "#8a6d00"
        result_icon = "🟡"
        description = (
            "The model predicts a medium irrigation requirement."
        )

    else:

        result_color = "#1b5e20"
        result_icon = "🟢"
        description = (
            "The model predicts a low irrigation requirement."
        )

    st.markdown(
        f"""
        <div class="prediction-box">

            <div class="prediction-label">
                Predicted Irrigation Requirement
            </div>

            <div class="prediction-value"
                 style="color:{result_color};">

                {result_icon} {prediction_label.upper()}

            </div>

            <div class="prediction-description">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📋 Field Summary")

    summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

    with summary_col1:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-number">
                    {soil_moisture:.0f}%
                </div>
                <div class="info-label">
                    Soil Moisture
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with summary_col2:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-number">
                    {temperature:.0f}°C
                </div>
                <div class="info-label">
                    Temperature
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with summary_col3:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-number">
                    {rainfall:.0f} mm
                </div>
                <div class="info-label">
                    Rainfall
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with summary_col4:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-number">
                    {humidity:.0f}%
                </div>
                <div class="info-label">
                    Humidity
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # MODEL CONFIDENCE
    # =====================================================

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(input_encoded)[0]

        confidence = max(probabilities) * 100

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("🤖 Model Confidence")

        st.progress(
            min(int(confidence), 100)
        )

        st.write(
            f"Estimated model confidence: **{confidence:.1f}%**"
        )

        st.caption(
            "This is the model's probability estimate and "
            "should not be interpreted as a guarantee."
        )

    # =====================================================
    # INPUT DETAILS
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

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