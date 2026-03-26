
---

# 🧪 Experimentation & Business Impact Analytics using SQL

## 🔹 Project Overview

This project focuses on **A/B experimentation analysis** to measure the **true business impact** of product changes using SQL.

The goal is to demonstrate how SQL can be used to:

* Validate experiment setup
* Measure conversion impact
* Quantify revenue uplift
* Compare retention outcomes
* Make **data-driven rollout decisions**

This mirrors real-world **Product, Growth, and Experimentation Analytics** work in SaaS companies.

---

## 🔹 Business Problems Solved

This project answers critical experimentation questions such as:

* Is the experiment set up correctly (no bias / SRM)?
* Are users evenly distributed across variants?
* Which variant converts better?
* Does the winning variant generate more revenue?
* Is the revenue uplift meaningful per user (ARPU)?
* Does the experiment improve long-term retention?
* Is the impact short-term or sustainable?

---

## 🔹 Project Structure

```
📦 Experimentation-Business-Impact-Analytics-SQL/
│
├── experiment_validation.sql
├── conversion_analysis.sql
├── revenue_impact.sql
├── retention_comparision.sql
│
├── final_views.sql
├── insights_for_founders.md
├── data_model_assumptions.md
└── README.md
```

---

## 🔹 SQL Files Explained

### 1️⃣ `experiment_validation.sql`

Focuses on **experiment hygiene**:

* User assignment validation
* Variant distribution checks
* Sample Ratio Mismatch (SRM) detection

Used to ensure experiment results are **trustworthy** before analysis.

---

### 2️⃣ `conversion_analysis.sql`

Focuses on **conversion performance**:

* Converted users per variant
* Conversion rate calculation
* Absolute and relative conversion uplift

Used to identify which variant performs better in driving conversions.

---

### 3️⃣ `revenue_impact.sql`

Focuses on **monetary impact**:

* Total revenue per variant
* ARPU (Average Revenue Per User)
* Revenue uplift between variants

Used to evaluate whether the experiment actually **makes more money**.

---

### 4️⃣ `retention_comparision.sql`

Focuses on **long-term impact**:

* Retained users per variant
* Retention rate comparison
* Retention uplift analysis

Used to ensure the winning variant drives **sustainable growth**, not just short-term gains.

---

## 🔹 SQL Concepts Used

* Common Table Expressions (CTEs)
* Experiment validation & SRM checks
* Funnel-style conversion analysis
* Revenue attribution
* ARPU calculations
* Retention metrics
* Absolute & relative lift calculations
* Business-driven SQL structuring

---

## 🔹 Assumptions

* Each user belongs to only one experiment variant
* Successful payment = conversion
* Revenue includes only successful payments
* User is retained if active in the last 30 days
* Variants A and B represent control and treatment

Detailed assumptions and table structure are documented in
👉 **`data_model_assumptions.md`**

---

## 🔹 Target Roles

This project is designed for:

• Data Analyst  

• Product Analyst

• Growth Analyst

• Experimentation / A/B Testing Analyst 

• Startup and SaaS analytics teams

The emphasis is on **business impact**, not just statistical metrics.

---

## 🔹 Author

**Sathvik**
Aspiring Product / Growth Data Analyst specializing in experimentation analytics, SQL analysis, and data-driven decision making.

---

