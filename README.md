
# AI-Based Student Performance Prediction and Personalized Guidance Using a Small Language Model

## Project Overview
This project predicts students' final academic performance using machine learning and aims to provide personalized educational guidance using a Small Language Model (SLM).

## Dataset
- Dataset: UCI Student Performance Dataset
- Total records: 395
- Training records: 276
- Validation records: 59
- Testing records: 60
- Target variable: G3 (final grade)

## Machine Learning Model
Random Forest Regressor is used to predict students' final grades.

## Model Evaluation

| Metric | Validation | Test |
|---|---:|---:|
| MAE | 1.03 | 1.13 |
| RMSE | 1.72 | 1.88 |
| R2 Score | 0.876 | 0.824 |

## Technologies
- Python
- Pandas
- Scikit-learn
- Hugging Face
- Small Language Model (SLM)
- Streamlit

## Design Thinking
1. Empathize: Understand students' academic challenges.
2. Define: Identify the need for early academic performance insights.
3. Ideate: Explore AI-based prediction and personalized guidance.
4. Prototype: Develop a student performance prediction application.
5. Test: Evaluate the model using validation and test datasets.

## Important Note
The Random Forest model predicts grades. It is separate from the SLM, which is intended to generate student guidance.
