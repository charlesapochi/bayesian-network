import csv

def read_patient_data(file_path):
    patient_data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patient_data.append({
                'id': row['id'],
                'gender': row['gender'],
                'age': row['age'],
                'hypertension': int(row['hypertension']),
                'heart_disease': int(row['heart_disease']),
                'ever_married': row['ever_married'],
                'work_type': row['work_type'],
                'Residence_type': row['Residence_type'],
                'avg_glucose_level': float(row['avg_glucose_level']),
                'bmi': row['bmi'] if row['bmi'] != 'N/A' else None,
                'smoking_status': row['smoking_status'],
                'alzheimer': int(row['alzheimer'])
            })
    return patient_data

# file_path = 'data/patient_data.csv'
# patient_data = read_patient_data(file_path)

# for patient in patient_data:
#     print(patient)
