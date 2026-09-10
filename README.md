# 🏠 House Price Prediction using Machine Learning

A machine learning project that predicts house prices using **Linear Regression** based on various property features such as area, number of bedrooms, bathrooms, floors, year built, location, condition, and garage availability.

## 📌 Project Overview

House price prediction is a common machine learning problem where historical housing data is used to identify relationships between property characteristics and their prices.

In this project, a **Linear Regression** model is trained to predict house prices using multiple features from a housing dataset.

The project demonstrates the complete basic machine learning workflow:

- Loading and exploring a dataset
- Checking dataset dimensions and information
- Detecting duplicate records
- Encoding categorical variables
- Performing correlation analysis
- Splitting data into training and testing sets
- Training a Linear Regression model
- Making predictions
- Evaluating model performance

---

## 📊 Dataset

The project uses the **House Price Prediction Dataset**, which contains information about different properties and their corresponding prices.

### Features Used

| Feature | Description |
|---|---|
| Area | Area of the house |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Floors | Number of floors |
| YearBuilt | Year in which the house was built |
| Location | Location of the property |
| Condition | Condition of the property |
| Garage | Garage availability/information |
| Price | Target house price |

The categorical features such as `Location`, `Condition`, and `Garage` are converted into numerical values using **Label Encoding**.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Linear Regression**
- **Git & GitHub**

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Exploration
   ↓
Duplicate Checking
   ↓
Categorical Encoding
   ↓
Correlation Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Linear Regression Model
   ↓
Prediction
   ↓
Model Evaluation
