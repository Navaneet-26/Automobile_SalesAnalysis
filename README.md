# 🚗 Automobile Sales Analytics Dashboard

🔗 **Live Demo:** https://automobile-salesanalysis.onrender.com/

An interactive dashboard built using **Python, Dash, and Plotly** to analyze automobile sales trends across recession and non-recession periods.

---

## 📚 Table of Contents

- [📌 Problem Statement](#-problem-statement)
- [❓ Key Business Questions](#-key-business-questions)
- [📊 Project Overview](#-project-overview)
- [🖼️ Dashboard Preview](#️-dashboard-preview)
- [⚙️ Tech Stack](#️-tech-stack)
- [✨ Key Features](#-key-features)
- [🔍 Key Insights & Findings](#-key-insights--findings)
- [💡 Business Recommendations](#-business-recommendations)
- [🚀 How to Run Locally](#-how-to-run-locally)
- [🌐 Deployment](#-deployment)
- [📈 Outcome](#-outcome)
- [👨‍💻 Author](#-author)

---

## 📌 Problem Statement

Automobile companies often struggle to understand how external economic factors influence sales performance. Without proper analysis, businesses may:

- Fail to anticipate sales drops during economic downturns  
- Misallocate advertising budgets  
- Miss seasonal demand opportunities  
- Lack clarity on customer affordability and demand patterns  

This project uses macroeconomic data to generate actionable insights for improving decision-making and sales strategy.

---

## ❓ Key Business Questions

- How do recession periods impact automobile sales across segments?  
- Which factors (GDP, unemployment, consumer confidence) most influence sales?  
- Is there a relationship between advertising spend and sales performance?  
- How does seasonality affect automobile demand?  
- Which regions perform better during economic downturns?  

---

## 📊 Project Overview

This project analyzes how macroeconomic factors like **GDP, unemployment rate, consumer confidence, and seasonality** impact automobile sales.

Users can dynamically switch between:

- 📈 Yearly Statistics  
- 📉 Recession Period Analysis  

using interactive dropdowns powered by Dash callbacks.

---

## 🖼️ Dashboard Preview

### 1. Yearly Statistics
<img width="1760" height="1388" alt="automobile-salesanalysis onrender com_ (1)" src="https://github.com/user-attachments/assets/e2e40e38-c3c0-49c5-ac8f-c90619c67604" />

### 2. Recession period
<img width="1760" height="1388" alt="automobile-salesanalysis onrender com_" src="https://github.com/user-attachments/assets/dcef6a5e-2a78-40b8-af78-598237dbf2ff" />

### 3. Sales Regional wise during recession
![Dashboard Preview](image.png)

---

## ⚙️ Tech Stack

- Python  
- Dash  
- Plotly  
- Pandas  
- Folium  

---

## ✨ Key Features

- Interactive dropdown filters  
- Dynamic graph updates (Dash callbacks)  
- Recession vs Non-recession comparison  
- Multiple visualizations (line, bar, pie charts)  
- Live deployed dashboard  

---

## 🔍 Key Insights & Findings

### 📌 1. Sales vs Advertising
Automobile sales are more volatile than advertising during non-recession periods, showing strong dependence on external economic conditions.

---

### 📉 2. Recession Impact
There is a **significant decline in automobile sales during recession periods**.  
Executive and sports cars are the most affected segments.

---

### 📊 3. GDP Behavior
GDP is lower and more volatile during recessions, reflecting economic instability.  
Non-recession periods show relatively stable growth.

---

### 📅 4. Seasonality
Sales peak in **April and December**, indicating strong seasonal demand patterns.

---

### 💰 5. Consumer Confidence & Pricing
Higher consumer confidence increases sales, while higher vehicle prices reduce demand.  
Affordability becomes critical during downturns.

---

### 📢 6. Advertising Strategy
Companies increase advertising spend during non-recession periods to maximize growth opportunities.

---

### 🎯 7. Smart Marketing During Recession
Companies shift focus toward **affordable vehicles**, targeting cost-conscious customers.

---

### 📉 8. Unemployment vs Sales
Sales decline as unemployment rises, with noticeable drops beyond 3%.  
Entry-level vehicles are more sensitive to economic changes.

---

### 🌎 9. Regional Sales Distribution
Sales vary across regions during recession, highlighting geographic demand differences using Folium maps.

---

## 💡 Business Recommendations

- 🎯 Focus on **affordable vehicles during recession**  
- 📢 Optimize **advertising spend during growth periods**  
- 📉 Track **GDP & unemployment** for forecasting  
- 📅 Leverage **seasonal peaks (April & December)**  
- 🌎 Use **regional insights** for targeted marketing  

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## 🌐 Deployment

This project is deployed on Render for public access.

## 📈 Outcome

This project demonstrates:

- Identifying key drivers of automobile sales
- Improving marketing and pricing strategies
- Enabling data-driven decision-making
- Building and deploying interactive dashboards
  
## 👨‍💻 Author

Navaneet SV

