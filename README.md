# 🩺 Diabetes Prediction using Machine Learning

This project uses machine learning to predict whether a person is **diabetic or not** based on medical diagnostic features such as glucose level, BMI, insulin, age, and other health indicators.

## 📌 Objective

The objective of this project is to:

* Analyze a healthcare dataset
* Handle missing and invalid data
* Train machine learning models for classification
* Evaluate model performance
* Build an interactive **Streamlit web app** for predictions

---

## 📊 Dataset

The dataset contains **768 records** with the following features:

* **Pregnancies** – Number of pregnancies
* **Glucose** – Blood glucose level
* **BloodPressure** – Blood pressure level
* **SkinThickness** – Skin thickness measurement
* **Insulin** – Insulin level
* **BMI** – Body Mass Index
* **DiabetesPedigreeFunction** – Genetic risk factor
* **Age** – Age of the individual
* **Outcome** – Target variable (0 = Non-diabetic, 1 = Diabetic)

---

## ⚙️ Project Workflow

1. Data loading
2. Data cleaning and preprocessing
3. Handling zero/invalid values
4. Exploratory Data Analysis (EDA)
5. Train-test split (with stratification)
6. Feature scaling using StandardScaler
7. Model training:

   * Linear SVM
   * RBF SVM
8. Model evaluation
9. Model comparison
10. Final model selection
11. Model saving
12. Streamlit app development

---

## 🧠 Models Used

* **Linear Support Vector Machine (SVM)**
* **RBF Kernel SVM (Final Model)**

---

## 📈 Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🏆 Results

* Linear SVM achieved moderate performance
* **RBF SVM performed better and was selected as the final model**

---

## 💡 Key Insights

* Glucose and BMI are strong indicators of diabetes
* Handling zero values significantly improves model performance
* Feature scaling is crucial for SVM models

---

## 💾 Model Saving

The trained model and scaler are saved for deployment:

```python
with open("diabetes_model.pkl", "wb") as file:
    pickle.dump(rbf_classifier, file)

with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)
```

---

## 🖥️ Streamlit App

An interactive web app was built using Streamlit.

### Features:

* User inputs health parameters
* Model predicts diabetes status
* Instant result display

### Run the app:

```bash
streamlit run app.py
```

