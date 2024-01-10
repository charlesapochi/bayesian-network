from src.BayesianNetwork import BayesianNetwork
from src.UncertaintyModeling import UncertaintyModeling
from src.MedicalDiagnosis import MedicalDiagnosis
from utils.probability_tables import generate_probability_tables

def main():
    bayes_net = BayesianNetwork()
    uncertainty_model = UncertaintyModeling()
    probability_tables = generate_probability_tables()

    evidence = {
    "Gender": "Female",
    "Age": "Middle-aged",
    "Hypertension": 0,
    "Heart Disease": 1,
    "Ever Married": "Yes",
    "Work Type": "Private",
    "Residence Type": "Urban",
    "Avg Glucose Level": "Medium",
    "BMI": "Normal",
    "Smoking Status": "never smoked"
    }

    uncertainty_model.update_with_evidence(evidence )

    medical_diagnosis = MedicalDiagnosis(bayes_net, uncertainty_model)
    medical_diagnosis.setup_diagnosis_model(probability_tables)

    # Perform diagnosis
    query_node = "Alzheimer's Disease"
    query_value = 1
    diagnosis = medical_diagnosis.perform_diagnosis(query_node, query_value, evidence)
    print(f"Probability of having Alzheimer's Disease: {diagnosis}")

if __name__ == "__main__":
    main()
