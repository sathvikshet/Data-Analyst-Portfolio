
---

# 📊 Product, Retention & Churn Analytics using SQL

## 🔹 Project Overview

This project focuses on **product usage, user engagement, retention, churn, and feature adoption** using SQL.

The goal is to demonstrate how SQL can be used to:

* Understand **how users engage with a product**
* Identify **where users drop off**
* Detect **early churn signals**
* Measure **feature adoption and retention impact**

This mirrors real-world **Product Analytics / Growth Analytics** work commonly done in SaaS companies.

---

## 🔹 Business Problems Solved

This project answers key product and growth questions such as:

* How active are users on a daily, weekly, and monthly basis?
* How sticky is the product (DAU / MAU)?
* How well do users retain over time after signup?
* Where do users drop off in the conversion funnel?
* Which users are churned based on inactivity or subscription end?
* What is the overall churn rate?
* Which product features drive higher retention?

---

## 🔹 Project Structure

```
📦 Product-Retention-Churn-Analytics-SQL/
│
├── activity_metrics.sql
├── cohort_analysis.sql
├── funnel_analysis.sql
├── churn_detection.sql
├── feature_adoption.sql
│
├── final_views.sql
├── insights_for_founders.md
├── data_model_assumptions.md
└── README.md
```

---

## 🔹 SQL Files Explained

### 1️⃣ `activity_metrics.sql`

Focuses on **user engagement metrics**:

* Daily Active Users (DAU)
* Weekly Active Users (WAU)
* Monthly Active Users (MAU)
* DAU / MAU ratio (product stickiness)

Used to measure overall product usage and engagement health.

---

### 2️⃣ `cohort_analysis.sql`

Focuses on **user retention over time**:

* Signup-based cohorts
* Monthly retention tracking
* Retention percentage by cohort age

Used to understand how long users stay active after joining.

---

### 3️⃣ `funnel_analysis.sql`

Focuses on **conversion flow analysis**:

* Signup → Activation → Subscription → Payment
* Conversion rates between steps
* Drop-off counts at each stage

Used to identify friction points in the user journey.

---

### 4️⃣ `churn_detection.sql`

Focuses on **churn identification and churn rate**:

* Activity-based churn (30-day inactivity)
* Subscription-based churn
* Combined churn logic
* Overall churn rate calculation

Used to monitor product health and retention risk.

---

### 5️⃣ `feature_adoption.sql`

Focuses on **feature usage and retention impact**:

* Feature adoption counts
* Feature adoption percentage
* Comparison of feature usage between retained and churned users
* Retention ratio per feature

Used to identify features that drive long-term user retention.

---

## 🔹 SQL Concepts Used

* Common Table Expressions (CTEs)
* Window Functions
* Funnel analysis using filtered aggregations
* Cohort analysis with time offsets
* Retention and churn calculations
* Product engagement metrics (DAU / MAU)
* Business-driven SQL structuring

---

## 🔹 Assumptions

* Each row in `events` represents a user interaction
* `event_time` captures when activity occurred
* Users inactive for 30+ days are considered churned
* Signup date represents the start of a user lifecycle
* Feature usage is inferred from event names

Detailed assumptions and table structure are documented in
👉 **`data_model_assumptions.md`**

---

## 🔹 Target Roles

This project is designed for:

• Data Analyst

• Product Analyst

• Growth / Business Analyst

• SaaS and product analytics teams

The emphasis is on **business understanding, clarity, and decision support**, not just SQL complexity.

---

## 🔹 Author

**Sathvik**
Aspiring Product / Data Analyst specializing in product analytics, SQL-based analysis, and data-driven decision making.

---


