class BayesianNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, parents=None):
        if name in self.nodes:
            raise ValueError(f"Node '{name}' already exists in the network.")
        self.nodes[name] = {
            'parents': parents if parents else [],
            'prob_table': {}
        }

    def add_prob_table(self, node_name, prob_table):
        if node_name not in self.nodes:
            raise ValueError(f"Node '{node_name}' does not exist in the network.")
        self.nodes[node_name]['prob_table'] = {tuple(k): v for k, v in prob_table.items()}

    def get_probability(self, node_name, node_value, evidence={}):
        node = self.nodes[node_name]
        parents = node['parents']
        prob_table = self.nodes[node_name]['prob_table']

        if not parents:
            return prob_table[node_value]

        parent_values = tuple(evidence[parent] for parent in parents)
        return prob_table[parent_values][node_value]
    
    def perform_inference(self, query_node, query_value, evidence={}):
        total_probability = 0
        query_node_prob_table = self.nodes[query_node]['prob_table']

        for value, probabilities in query_node_prob_table.items():
            if value in evidence:
                new_evidence = evidence.copy()
                new_evidence[query_node] = value[0]  
                probability = self.calculate_probability(query_node, query_value, new_evidence)
                total_probability += probability

        return total_probability


    def calculate_probability(self, query_node, query_value, evidence={}):
        probability = 1.0
        for node_name, node_value in evidence.items():
            probability *= self.get_probability(node_name, node_value, evidence)

        return probability