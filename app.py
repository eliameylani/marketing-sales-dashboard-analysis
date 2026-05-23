import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Marketing Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.metric-card {
    background-color: #1F2937;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

.metric-title {
    font-size: 18px;
    color: #9CA3AF;
}

.metric-value {
    font-size: 32px;
    font-weight: bold;
    color: white;
}

.section-title {
    font-size: 40px;
    font-weight: bold;
    color: white;
}

.sub-text {
    color: #9CA3AF;
    font-size: 18px;
}

.insight-box {
    background-color: #1F2937;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #6B7280;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📊 Navigation")

menu = st.sidebar.radio(
    "Select Menu",
    [
        "Dashboard Overview",
        "Business Insights",
        "Power BI Dashboard",
        "About Project"
    ]
)

# HOME
if menu == "Dashboard Overview":

    st.markdown("""
    <div class="section-title">
        Marketing Sales Dashboard Analysis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sub-text">
        Quick Commerce Analytics, Customer Insights & Fraud Detection System
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">💰 Total Revenue</div>
            <div class="metric-value">Rp4.7B</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">🧾 Transactions</div>
            <div class="metric-value">107K</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">👥 Total Users</div>
            <div class="metric-value">15K</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">📈 Average Order Value</div>
            <div class="metric-value">Rp44K</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.subheader("📌 Project Overview")

    st.write("""
    This project focuses on analyzing Quick Commerce sales performance using
    Power BI dashboards combined with descriptive statistical analysis and
    Benford’s Law anomaly detection.

    The dashboard is designed to help Marketing & Sales Managers monitor
    revenue growth, customer behavior, transaction activities, and unusual
    transaction patterns for strategic business decision-making.
    """)

# BUSINESS INSIGHTS
elif menu == "Business Insights":

    st.markdown("""
    <div class="section-title">
        Business Insights
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="insight-box">
            <h3>💳 Payment Analysis</h3>
            <p>
            QRIS and E-Wallet are the most dominant payment methods,
            indicating strong adoption of digital payment systems.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="insight-box">
            <h3>🛒 Product Performance</h3>
            <p>
            Several product categories contribute significantly
            to overall sales revenue and transaction volume.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="insight-box">
            <h3>⏰ Transaction Activity</h3>
            <p>
            Most customer transactions occur during morning
            to afternoon periods.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="insight-box">
            <h3>🔍 Fraud Detection</h3>
            <p>
            Benford’s Law analysis indicates unusual digit
            distributions that may suggest transaction anomalies.
            </p>
        </div>
        """, unsafe_allow_html=True)

# POWER BI
elif menu == "Power BI Dashboard":

    st.markdown("""
    <div class="section-title">
        Interactive Power BI Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    dashboard_url = "https://app.powerbi.com/groups/me/reports/584c6cbd-f667-4d90-aad3-1bbe1b7e7e72/648d4ec2ad001c0ee10d?experience=power-bi"

    st.link_button(
        "🚀 Open Power BI Dashboard",
        dashboard_url
    )

    st.info("Click the button above to access the interactive dashboard.")

# ABOUT
elif menu == "About Project":

    st.markdown("""
    <div class="section-title">
        About Project
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    ### 👩‍💻 Team Members

    - Elia Meylani Simanjuntak
    - Mutiara Dian Pitaloka
    - Oktavia Nurwinda
    - Farahanum Afifah
    """)

    st.write("""
    ### ⚙️ Technologies Used

    - Power BI
    - Python
    - Streamlit
    - Jupyter Notebook
    - Excel
    """)

# FOOTER
st.markdown("""
<div class="footer">
    © 2025 Marketing Sales Dashboard Analysis • Built with Streamlit
</div>
""", unsafe_allow_html=True)
