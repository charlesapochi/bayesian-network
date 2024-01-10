class UncertaintyModeling:
    def __init__(self):
        self.nodes = {}
        self.prior_beliefs = {}

    def define_prior_beliefs(self, beliefs):
        self.prior_beliefs = beliefs

    def update_with_evidence(self, new_evidence):
        for node, value in new_evidence.items():
            if node in self.nodes:
                self.prior_beliefs[node] = value
    
    def get_prior_beliefs(self):
        return self.prior_beliefs