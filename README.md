# 🚀 Marketing Sales Dashboard Analysis  
### *Quick Commerce Analytics, Customer Insight & Fraud Detection System*

<div align="center">

![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-Analytics-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

# 📌 Project Overview

This project analyzes **Quick Commerce sales transactions** using an interactive **Power BI Dashboard** combined with **Descriptive Statistical Analysis** and **Benford’s Law**.

The dashboard is designed to help Marketing & Sales Managers:
- monitor sales performance,
- understand customer behavior,
- identify business opportunities,
- and detect unusual transaction patterns.

The analysis provides strategic insights through interactive visualizations and statistical approaches to support **data-driven decision making**.

---

# 🎯 Project Objectives

✅ Analyze overall sales performance  
✅ Monitor revenue growth trends  
✅ Identify top-performing product categories  
✅ Analyze customer purchasing behavior  
✅ Evaluate dominant payment methods  
✅ Discover peak transaction activity hours  
✅ Detect anomalies using Benford’s Law  
✅ Support strategic business decisions with analytics

---

# 🛒 Dataset Description

The dataset contains transaction data from a Quick Commerce platform.  
Each record represents a customer transaction and includes information related to users, products, payments, and transaction activities.

---

## 📂 Dataset Attributes

| Attribute | Description |
|---|---|
| `transaction_id` | Unique transaction identifier |
| `session_id` | Session activity identifier |
| `user_id` | Customer identifier |
| `age` | Customer age |
| `location` | Customer region/location |
| `segment` | Customer segmentation |
| `trx_timestamps` | Transaction timestamp |
| `payment_method` | Payment method used |
| `product_category` | Product category |
| `product_name` | Product purchased |
| `qty` | Quantity purchased |
| `amount` | Total transaction amount |
| `product_price` | Product unit price |
| `traffic` | Traffic acquisition source |
| `trx_hour` | Transaction hour |
| `time_of_day` | Morning/Afternoon/Night classification |

---

# 📊 Dashboard Features

## 🔹 Key Performance Indicators (KPI)

| KPI | Description |
|---|---|
| 💰 Total Revenue | Total revenue generated |
| 🧾 Total Transactions | Total completed transactions |
| 👥 Total Users | Total active users |
| 📈 Average Order Value | Average customer spending |
| 🔄 Conversion Rate | Transaction conversion performance |

---

## 🔹 Interactive Visualizations

✨ Revenue Trend by Year  
✨ Revenue by Product Category  
✨ Revenue by Payment Method  
✨ Product Performance Analysis  
✨ Transaction Distribution by Hour  
✨ Customer Segment Analysis  
✨ Session Activity Analysis  

---

# 🧠 Area of Analysis

## 1️⃣ Sales Performance Metrics
This section evaluates business performance using:
- Total Revenue
- Quantity Sold
- Average Order Value
- Revenue by Product Category
- Revenue by Payment Method
- Product Sales Performance

---

## 2️⃣ Customer & Traffic Metrics
This section focuses on customer behavior analysis:
- Total Users
- User Activity
- Traffic Sources
- Customer Segmentation
- Transaction Activity by Hour
- Session Distribution

---

# 📈 Descriptive Statistics Analysis

Statistical analysis was conducted to understand transaction value distribution and overall sales characteristics.

---

## 📌 Statistical Summary

| Metric | Value |
|---|---|
| Mean | Rp44,203.89 |
| Median | Rp40,000 |
| Mode | Rp40,000 |
| Standard Deviation | 19,976 |
| Minimum | Rp3,500 |
| Maximum | Rp156,000 |
| Total Transactions | 107,664 |
| Total Revenue | Rp4,759,167,500 |

---

## 📌 Key Findings

- Most transactions occur around Rp40,000
- Transaction values are moderately distributed
- Distribution is positively skewed (right-skewed)
- Some high-value transactions increase the overall mean
- No missing values were found in transaction data

---

# 🔍 Benford’s Law Analysis

Benford’s Law was applied to analyze the first-digit distribution of transaction values.

---

## 📌 Key Findings

| Digit | Observation |
|---|---|
| 1️⃣ | Much lower than expected |
| 3️⃣ & 4️⃣ | Significantly higher than expected |
| 2️⃣–6️⃣ | Above natural Benford distribution |

---

## 📌 Interpretation

The first-digit distribution does not fully follow the natural Benford pattern.  
This indicates:
- unusual concentration of transaction values,
- possible transaction anomalies,
- and potential fraud indicators.

Benford’s Law helps provide an additional analytical layer for anomaly detection within sales data.

---

# 💡 Business Insights

## 📌 Sales Insights
- Revenue shows stable growth over time
- Certain product categories dominate sales contribution
- Digital payment methods such as QRIS and e-wallet are highly preferred

---

## 📌 Customer Insights
- Customer activity is highest during morning to afternoon periods
- Returning users consistently contribute to sales
- Transaction behavior differs across segments and regions

---

## 📌 Strategic Recommendations
- Optimize marketing campaigns during peak transaction hours
- Focus promotions on high-performing product categories
- Expand digital payment incentives
- Conduct further investigation into unusual transaction patterns

---

# ⚙️ Technologies Used

<div align="center">

| Technology | Function |
|---|---|
| 🟡 Power BI | Dashboard Visualization |
| 🐍 Python | Data Analysis |
| 📓 Jupyter Notebook | Exploratory Data Analysis |
| 📊 Excel | Data Preparation |
| 📈 Statistical Methods | Descriptive & Benford Analysis |

</div>

---

# 🗂 Project Structure

```text
marketing-sales-dashboard-analysis/
│
├── notebooks/
│   └── analysis.ipynb
│
├── dashboard/
│   └── dashboard.pbix
│
├── data/
│
├── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔗 Dashboard Access

🚀 Click below to open the interactive dashboard:

[Power BI Dashboard](https://app.powerbi.com/groups/me/reports/584c6cbd-f667-4d90-aad3-1bbe1b7e7e72/648d4ec2ad001c0ee10d?experience=power-bi)

---

# 📷 Dashboard Preview

> Dashboard screenshots and visual previews will be added soon.

---

# 🚀 Future Development

✨ Sales Forecasting  
✨ Customer Segmentation using Machine Learning  
✨ Real-Time Data Integration  
✨ Fraud Detection Automation  
✨ Advanced Predictive Analytics  
✨ Interactive Business Intelligence Enhancements  

---

# 👩‍💻 Authors

<div align="center">

| Name | Role |
|---|---|
| **Elia Meylani Simanjuntak** | Data Analyst & Dashboard Developer |
| **Mutiara Dian Pitaloka** | Data Visualization & Analysis |
| **Oktavia Nurwinda** | Statistical Analysis |
| **Farahanum Afifah** | Business Insight & Documentation |

</div>

---

<div align="center">

## ⭐ Thank You for Visiting This Project ⭐

### *Data-Driven Decisions Start With Better Analytics*

</div>

# 🌐 Live Demo

🚀 Open Interactive Website:

[Click Here](https://marketing-sales-dashboard-analysis-3ymfhyqmegkzsrxatqt6lo.streamlit.app/)
