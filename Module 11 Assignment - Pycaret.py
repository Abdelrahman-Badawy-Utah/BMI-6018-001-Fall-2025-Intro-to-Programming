# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 14:40:20 2025

@author: El-Wattaneya
"""

# ============================================================
# Library Name: PyCaret
# Source: https://pycaret.org/
#
# PyCaret is an open-source, low-code machine learning library
# used to automate the complete machine learning pipeline.
# It performs:
# - Data preprocessing
# - Feature encoding
# - Missing value handling
# - Model training
# - Model comparison
# - Model evaluation
#
# In this assignment, PyCaret is applied Breast Cancer Recurrence Dataset 
#to predict whether a patient will experience recurrence of cancer.
# ============================================================


# ============================================================
# Advantages of PyCaret:
#
# 1. Fully automated preprocessing and encoding
# 2. Excellent support for categorical medical data
# 3. Minimal coding required
# 4. Automatic comparison of multiple ML models
# 5. Built-in evaluation and visualization tools
#
# Limitations of PyCaret:
#
# 1. Less transparency of internal ML steps
# 2. Requires more computing resources
# 3. Limited customization compared to manual ML coding
# ============================================================


# ============================================================
# STEP 1: Installing the Library
# ============================================================
pip install pycaret 

# ============================================================
# STEP 2: Importing Required Libraries
# ============================================================
import pandas as pd
from pycaret.classification import setup, compare_models, evaluate_model, predict_model

# ============================================================
# STEP 3: Assigning Column Names Based on Dataset Description
# ============================================================
column_names = [
    "Class",          # Target
    "age",
    "menopause",
    "tumor-size",
    "inv-nodes",
    "node-caps",
    "deg-malig",
    "breast",
    "breast-quad",
    "irradiat"
]
# ============================================================
# STEP 4: Loading the Dataset Using Pandas
# ============================================================
df = pd.read_csv(r"C:\Users\El-Wattaneya\Desktop\New folder (2)\breast-cancer.data", header=None, names=column_names)

# ============================================================
# STEP 5: Displaying Dataset Information
# ============================================================
print(df.head())
print(df.info())

# ============================================================
# STEP 6: Initializing PyCaret Setup
# ============================================================
clf = setup(
    data=df,
    target="Class",
    session_id=42,
    verbose=False
)
# ============================================================
# STEP 7: Automatically Train & Compare ML Models
# ============================================================
best_model = compare_models()

# ============================================================
# STEP 8: Evaluating the Best Model
# ============================================================
evaluate_model(best_model)

# To know the exact ML model being used
model_name = type(best_model).__name__
print("Best Machine Learning Model Used:", model_name)

# ============================================================
# STEP 9: Generating Predictions
# ============================================================
predictions = predict_model(best_model)
print(predictions.head())

# ============================================================
# STEP 10: Predicting Breast Cancer Recurrence for a New Patient
# ============================================================

# Create a new patient with the same feature names
new_patient = pd.DataFrame({
    "age": ["50-59"],
    "menopause": ["ge40"],
    "tumor-size": ["20-24"],
    "inv-nodes": ["0-2"],
    "node-caps": ["no"],
    "deg-malig": [2],
    "breast": ["right"],
    "breast-quad": ["right-up"],
    "irradiat": ["no"]
})

# Use the trained model to make a prediction
new_prediction = predict_model(best_model, data=new_patient)

print("\nNew Patient Prediction:")
print(new_prediction)

# ============================================================
# STEP 11: Model Visualizations
# to understand how well the model performs
# ============================================================
# Importing the plot model
from pycaret.classification import plot_model

# 1. Confusion Matrix
# Shows correct vs incorrect predictions for each class
plot_model(best_model, plot='confusion_matrix')

# 2. ROC Curve
# Shows how well the model separates the two classes
plot_model(best_model, plot='auc')

# 3. Feature Importance
# Shows which clinical features are most important for prediction
plot_model(best_model, plot='feature')

# 4. Precision-Recall Curve
# Useful when dealing with medical classification problems
plot_model(best_model, plot='pr')

# 5. Classification Report Visualization
plot_model(best_model, plot='class_report')



