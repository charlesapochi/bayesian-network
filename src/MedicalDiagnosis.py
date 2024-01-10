
class MedicalDiagnosis:
    def __init__(self, bayesian_network, uncertainty_model):
        self.bayesian_network = bayesian_network
        self.uncertainty_model = uncertainty_model

    def setup_diagnosis_model(self, probability_tables):
        nodes = [
            "Gender",
            "Age",
            "Hypertension",
            "Heart Disease",
            "Ever Married",
            "Work Type",
            "Residence Type",
            "Avg Glucose Level",
            "BMI",
            "Smoking Status",
            "Alzheimer's Disease",
        ]

        relationships = {
            "Alzheimer's Disease": [
                "Gender",
                "Age",
                "Hypertension",
                "Heart Disease",
                "Ever Married",
                "Work Type",
                "Residence Type",
                "Avg Glucose Level",
                "BMI",
                "Smoking Status"
            ]
        }

        # Adding nodes to the network
        for node in nodes:
            parents = relationships.get(node, [])
            self.bayesian_network.add_node(node, parents=parents)
            if node in probability_tables:
                self.bayesian_network.add_prob_table(node, probability_tables[node])

    def perform_diagnosis(self, query_node, query_value, evidence):
        self.uncertainty_model.update_with_evidence(evidence)

        diagnosis_result = self.bayesian_network.perform_inference(query_node, query_value, evidence)

        return diagnosis_result
