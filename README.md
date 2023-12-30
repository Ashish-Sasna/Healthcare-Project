# Pharmaceutical Persistency Prediction

## Project Overview

This project aims to tackle a critical challenge faced by pharmaceutical companies regarding the persistency of drugs as per physician prescriptions. ABC Pharma Company has approached our analytics team to automate the identification process. The objective is to gather insights into the factors influencing persistency and build a classification model using the provided dataset.

For a detailed report on the project, go through the [Project Report](https://github.com/Ashish-Sasna/Healthcare-Project/blob/main/Week%2013%20Deliverables/Project%20Report.pdf)

### Problem Statement

The challenge involves understanding and predicting the persistency of drugs based on various patient and treatment-related factors. The primary task includes data understanding, cleaning, feature engineering, model development, selection, evaluation, and deploying the final model.

### Dataset

The dataset for this project can be accessed [here]([Dataset_Link](https://drive.google.com/file/d/1P_oMc6gOBlhw6dY5PxaqxV2swdHMUooK/view)).

### Task Breakdown

1. **Problem Understanding**
   - Define the problem statement and objectives.
  
2. **Data Understanding**
   - Explore and understand the dataset's structure, features, and distributions.
  
3. **Data Cleaning and Feature Engineering**
   - Preprocess the data, handle missing values, and engineer relevant features.
  
4. **Model Development**
   - Develop machine learning models to predict drug persistency based on identified features.
  
5. **Model Selection**
   - Evaluate and compare different models to select the most suitable one.

6. **Model Evaluation**
   - Report accuracy, precision, and recall for both classes of the target variable.
   - Report ROC-AUC for model performance assessment.

7. **Deployment**
   - Deploy the final model for future predictions.

### Feature Description

| Bucket | Variable |
|--------|----------|
| 1 Unique Row Id | Patient ID |
| 1 Target Variable | Persistency_Flag |
| 5 Demographics | Age, Gender, Region, Race, Ethnicity |
| 1 IDN Indicator | Flag indicating patients mapped to IDN |
| 3 Physician Attributes | NTM - Physician Specialty |
| 13 Clinical Factors | NTM - T-Score, DEXA Scans, Fragility Fracture, Glucocorticoids |
| 45 Disease/Treatment factors Factors | NTM - Risks, Comorbidities, Concomitant drugs | 

### Model Evaluation

![image](https://github.com/Ashish-Sasna/Healthcare-Project/assets/96835311/b98b7458-323f-4089-8e91-2f0d4e5a2bb5)

### HomePage

![image](https://github.com/Ashish-Sasna/Healthcare-Project/assets/96835311/4010e127-2aff-4698-88d8-6bbe87160e73)

