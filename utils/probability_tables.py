import pandas as pd

def generate_probability_tables():
    data = pd.read_csv('data/patient_data.csv')

    # Discretizing 'age' into categories
    data['age_category'] = pd.cut(data['age'], bins=[0, 30, 60, float('inf')], labels=['Young', 'Middle-aged', 'Old'])

    # Discretizing 'avg_glucose_level' and 'bmi' into quartiles
    data['glucose_level_category'] = pd.qcut(data['avg_glucose_level'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
    data['bmi_category'] = pd.qcut(data['bmi'], q=4, labels=['Underweight', 'Normal', 'Overweight', 'Obese'])


    categorical_columns = ['gender', 'age_category', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'glucose_level_category', 'bmi_category', 'smoking_status']


    probability_tables = {}
    for column in categorical_columns:
        column_counter = data[column].value_counts(normalize=True).to_dict()
        probability_tables[column] = column_counter

    return probability_tables


