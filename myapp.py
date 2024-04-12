import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model_joblib_heart')

# Function to predict heart disease
def predict_heart_disease(age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [gender],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.title('Heart Disease Prediction')

    st.write('Fill in the following details to predict the probability of heart disease.')

    age = st.slider('Age', 18, 100, 50)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    trestbps = st.slider('Resting Blood Pressure (mm Hg)', 90, 200, 120)
    chol = st.slider('Cholesterol (mg/dl)', 100, 600, 200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
    restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
    thalach = st.slider('Maximum Heart Rate Achieved', 60, 220, 150)
    exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.0, 2.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.slider('Number of Major Vessels Colored by Flourosopy', 0, 4, 0)
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    if st.button('Predict'):
        # Convert categorical inputs to numerical values
        gender = 1 if gender == 'Male' else 0
        fbs = 1 if fbs == 'True' else 0
        exang = 1 if exang == 'Yes' else 0

        # Convert categorical inputs to numerical values
        cp_dict = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
        restecg_dict = {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}
        slope_dict = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
        thal_dict = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

        cp = cp_dict[cp]
        restecg = restecg_dict[restecg]
        slope = slope_dict[slope]
        thal = thal_dict[thal]

        # Make prediction
        prediction = predict_heart_disease(age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        if prediction == 1:
            st.error('The model predicts that you are at risk of heart disease.')
        else:
            st.success('The model predicts that you are not at risk of heart disease.')

if __name__ == '__main__':
    main()
