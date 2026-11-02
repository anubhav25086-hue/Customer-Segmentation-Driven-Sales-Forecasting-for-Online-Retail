# Customer Segmentation-Driven Sales Forecasting for Online Retail

**Can customer segmentation improve sales forecasting accuracy compared to a traditional global forecasting model?**

A Machine Learning project exploring customer behavior, unsupervised learning, and time-series forecasting to build more granular and accurate retail demand predictions.

---

## Project Overview

Traditional retail forecasting often treats all customers as a single homogeneous group. However, customers differ significantly in purchasing frequency, spending patterns, and seasonal behavior.

This project investigates whether **customer segmentation can improve next-month sales forecasting accuracy**.

We first segment customers based on their purchasing behavior using RFM (Recency, Frequency, Monetary) features. We then build forecasting models for individual customer segments and compare their performance against a global forecasting model that considers all customers together.

The ultimate goal is to understand whether customer-aware forecasting can provide better insights for inventory planning, demand estimation, and targeted marketing.

## Research Question

> Does segment-aware forecasting reduce prediction error relative to a single global model for next-month revenue?

## Project Objectives

- Identify meaningful customer segments using purchasing behavior.
- Apply unsupervised learning techniques to discover customer groups.
- Build monthly revenue forecasting models for each segment.
- Incorporate historical revenue and seasonal patterns.
- Compare segment-aware forecasting against global forecasting.
- Evaluate whether segmentation provides a measurable improvement in predictive performance.

## Dataset

**UCI Online Retail Dataset**

Source: [UCI Machine Learning Repository – Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)

The dataset contains transactions from a UK-based online retailer.

| Property | Description |
|---|---|
| Time period | December 2010 – December 2011 |
| Records | Approximately 540,000 |
| Products | Approximately 4,000 |
| Customers | Approximately 4,372 |
| Geography | Primarily United Kingdom |
| Type | Transactional retail data |

### Important Features

| Feature | Description |
|---|---|
| InvoiceNo | Transaction identifier |
| StockCode | Product identifier |
| Quantity | Number of units purchased |
| InvoiceDate | Transaction date and time |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Customer's country |

## Methodology

The project follows a two-stage machine learning pipeline.

### 1. Data Cleaning and Preprocessing

Before building the models, we prepare the transactional dataset.

Key preprocessing steps include:

- Handling missing CustomerID values.
- Identifying cancellations and returns using invoice codes and negative quantities.
- Excluding cancellations from the initial forecasting analysis.
- Parsing InvoiceDate into a proper datetime format.
- Engineering revenue using:

\[
Revenue = Quantity \times UnitPrice
\]

- Aggregating transaction-level data into customer-level and monthly records.

### 2. Customer Segmentation

We use RFM analysis to represent customer purchasing behavior.

**RFM Features:**

| Feature | Meaning |
|---|---|
| Recency | How recently a customer made a purchase |
| Frequency | How frequently a customer purchases |
| Monetary | How much a customer spends |

**Algorithms:**

- K-Means Clustering – Primary segmentation approach.
- Gaussian Mixture Models (GMM) – Comparison approach.

The objective is to discover meaningful behavioral segments rather than treating every customer identically.

### 3. Monthly Revenue Forecasting

After segmentation, we construct monthly revenue time series for each customer segment.

The forecasting task is formulated as a supervised regression problem.

**Target variable:** Next-month segment revenue.

**Predictor features:**
- Lagged monthly revenue.
- Historical sales patterns.
- Month-of-year.
- Seasonal indicators.
- Holiday indicators, where available.

**Models:**

| Model | Role |
|---|---|
| Linear Regression | Baseline |
| Ridge Regression | Regularized baseline |
| Gradient Boosted Trees | Main forecasting model |

We also construct a global forecasting model using aggregated revenue from all customers.

### 4. Model Comparison

We compare two approaches:

**Approach A – Global Forecasting**

All customers are treated as one group, and a single model predicts total next-month revenue.

**Approach B – Segment-Aware Forecasting**

Customers are divided into behavioral segments, and individual forecasting models predict the revenue of each segment.

The segment-level predictions can then be aggregated to obtain the overall revenue forecast.

## Evaluation Metrics

### Forecasting Metrics

| Metric | Purpose |
|---|---|
| MAE | Measures average absolute prediction error |
| RMSE | Penalizes larger forecasting errors |
| MAPE | Measures percentage-based forecasting error |

### Segmentation Metric

**Silhouette Score**

Used to evaluate the quality and separation of the discovered customer clusters.

### Validation Strategy

- Time-based train/test split.
- Training on 2010 data.
- Testing on the final months of 2011.
- Rolling-origin cross-validation, if time permits.

The final test period will be kept separate from model selection to avoid data leakage.

## Current Implementation Progress

The customer-month forecasting panel has been constructed.

| Property | Current Value |
|---|---:|
| Panel observations | 32,544 |
| Columns | 4 |
| Features | CustomerID, Segment, Month, Revenue |
| Validation checks | Passed |

The initial panel construction and validation checks have been completed. Forecasting model development and comparative evaluation are the next major stages.

## Project Workflow

```text
Raw Online Retail Dataset
          |
          v
   Data Cleaning
          |
          v
  Feature Engineering
          |
          v
    RFM Analysis
          |
          v
 Customer Segmentation
      /       \
     v         v
   K-Means    GMM
      \       /
       v     v
  Segment-wise Monthly
    Revenue Panel
          |
          v
  Forecasting Models
          |
     +----+-----+
     |          |
     v          v
 Segment-wise   Global
 Forecasting   Forecasting
     |          |
     +----+-----+
          |
          v
   Performance Comparison
          |
          v
   Research Conclusions
```

## Expected Challenges

- Missing customer identifiers.
- Uneven customer distribution across segments.
- Selecting a defensible number of clusters.
- Limited seasonal information due to less than two years of data.
- Avoiding data leakage during time-based validation.
- Comparing global and segment-level forecasts fairly.

## Research Contribution

This project does not propose a completely new machine learning algorithm.

Instead, it investigates the practical value of combining two established ideas:

1. Behavioral customer segmentation.
2. Supervised monthly sales forecasting.

The central investigation is whether customer-level behavioral differences contain useful information that improves aggregate forecasting performance.

We also aim to investigate which customer segments contribute most to future revenue and whether some segments are more predictable than others.

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook / Google Colab
- **Version Control:** Git & GitHub

## Team Members

| Member | Responsibility |
|---|---|
| Yug Bansal | Data Cleaning & EDA |
| Vivaan | Customer Segmentation & Validation |
| Anubhav Kumar Singh | Forecasting Models |
| Vedant Kaim | Evaluation, Ablation & Report Writing |

**Institution:** Indraprastha Institute of Information Technology Delhi (IIIT Delhi)

**Course:** AI201 – Introduction to Machine Learning

**Semester:** Monsoon 2026

## Future Scope

Potential extensions of this project include:

- Investigating different clustering strategies and feature combinations.
- Studying segment-specific seasonal behavior.
- Performing ablation studies to understand the contribution of segmentation.
- Exploring whether certain customer segments are more predictable than others.
- Evaluating the robustness of the approach on other retail datasets.
- Investigating the impact of segmentation on inventory and marketing decisions.

## Project Status

**Under Development**

This repository documents the development of our AI201 machine learning project, from transactional data preprocessing to customer segmentation and comparative forecasting experiments.

---

*Built as part of AI201 – Introduction to Machine Learning at IIIT Delhi.*
