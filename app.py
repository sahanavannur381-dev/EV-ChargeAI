
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------

st.set_page_config(
    page_title="EV ChargeAI",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------------
# DARK THEME DESIGN
# -----------------------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0B1220, #111C30);
    color: #F4F7FF;
}

[data-testid="stSidebar"] {
    background: #101827;
    border-right: 1px solid #26364D;
}

h1, h2, h3 {
    color: #45D6E8 !important;
}

p, label {
    color: #E2EAF5;
}

[data-testid="stMetric"] {
    background: #17263A;
    border: 1px solid #29445D;
    padding: 18px;
    border-radius: 14px;
}

.stButton > button {
    background: linear-gradient(90deg, #08B9CE, #7560E8);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #168FA7;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# APPLICATION HEADER
# -----------------------------------

st.title("⚡ EV ChargeAI")
st.subheader("AI-Driven EV Charging Infrastructure Decision Support")

st.write(
    "An interactive research prototype for exploring "
    "electric vehicle charging demand and infrastructure planning."
)

# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------

st.sidebar.title("⚡ EV ChargeAI")
st.sidebar.write("Application Navigation")

page = st.sidebar.radio(
    "Choose a page",
    ["Dashboard", "Demand Analysis", "Recommendations"]
)

# ===================================
# PAGE 1: DASHBOARD
# ===================================

if page == "Dashboard":

    st.header("EV Charging Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Survey Responses", "200")
    col2.metric("EV Owners", "115")
    col3.metric("Demand for More Stations", "72%")

    st.divider()

    st.subheader("Demand for Additional Charging Stations")

    data = pd.DataFrame({
        "Response": ["Yes", "No", "Maybe"],
        "People": [144, 30, 26]
    })

    fig = px.bar(
        data,
        x="Response",
        y="People",
        text="People",
        title="Survey Responses on Charging Station Demand"
    )

    fig.update_layout(
        paper_bgcolor="#17263A",
        plot_bgcolor="#17263A",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "72% of respondents indicated a need for more nearby "
        "EV charging stations."
    )

# ===================================
# PAGE 2: DEMAND ANALYSIS
# ===================================

elif page == "Demand Analysis":

    st.header("Interactive Charging Demand Analysis")

    st.write(
        "Enter the details below to explore an illustrative "
        "charging demand estimate."
    )

    location = st.selectbox(
        "Select Location Type",
        ["Residential", "Commercial", "Highway", "Industrial"]
    )

    ev_count = st.number_input(
        "Enter Estimated Number of EVs",
        min_value=1,
        max_value=10000,
        value=100
    )

    frequency = st.selectbox(
        "Select Charging Frequency",
        ["Low", "Medium", "High"]
    )

    if st.button("Calculate Estimated Demand"):

        multipliers = {
            "Low": 0.2,
            "Medium": 0.5,
            "High": 0.8
        }

        estimated_sessions = int(
            ev_count * multipliers[frequency]
        )

        st.subheader("Demand Estimation Result")

        st.metric(
            "Estimated Charging Sessions",
            estimated_sessions
        )

        st.write("Selected Location:", location)
        st.write("Selected Charging Frequency:", frequency)

        if estimated_sessions >= 60:
            st.success(
                "High estimated demand. Consider evaluating "
                "additional charging capacity."
            )

        elif estimated_sessions >= 30:
            st.info(
                "Moderate estimated demand. Monitor usage "
                "and plan capacity accordingly."
            )

        else:
            st.warning(
                "Low estimated demand. Continue monitoring "
                "before expanding infrastructure."
            )

    st.caption(
        "Note: This is an illustrative rule-based calculation, "
        "not a trained or validated AI prediction model."
    )

# ===================================
# PAGE 3: RECOMMENDATIONS
# ===================================

elif page == "Recommendations":

    st.header("Infrastructure Recommendations")

    st.write(
        "Select the conditions of a location to generate "
        "a suggested infrastructure action."
    )

    location = st.selectbox(
        "Select Location",
        ["Residential", "Commercial", "Highway", "Industrial"]
    )

    demand = st.selectbox(
        "Select Demand Level",
        ["Low", "Medium", "High"]
    )

    accessibility = st.selectbox(
        "Select Accessibility",
        ["Good", "Average", "Poor"]
    )

    waiting = st.selectbox(
        "Select Waiting Time",
        ["Short", "Moderate", "Long"]
    )

    if st.button("Generate Recommendation"):

        st.subheader("Recommended Action")

        if demand == "High" and accessibility == "Poor":

            st.success(
                "Prioritise installing additional charging stations "
                "in this location."
            )

        elif waiting == "Long":

            st.info(
                "Consider increasing charging capacity to reduce "
                "waiting time."
            )

        elif demand == "Medium":

            st.info(
                "Monitor charging demand and plan gradual "
                "infrastructure expansion."
            )

        else:

            st.success(
                "Existing infrastructure may be sufficient. "
                "Continue monitoring demand."
            )

        st.write("Selected Location:", location)
        st.write("Demand Level:", demand)
        st.write("Accessibility:", accessibility)
        st.write("Waiting Time:", waiting)

    st.caption(
        "Note: Recommendations are generated using predefined "
        "decision rules for prototype demonstration."
    )

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "EV ChargeAI | MBA Research Prototype | "
    "Decision Support for EV Charging Infrastructure"
)
