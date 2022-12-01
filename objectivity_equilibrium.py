# Theorem: Objectives are defined by a function that measures similarity to another model
# Create a ModelSelection class to select the most objective model for a dataset
# by @nissmogt "Names matter"

class ModelSelection:
    def __init__(self, models):
        self.models = models

    # Define a function that takes in measures similarity between models.

    def model_similarity(self, model1, model2):
        # Calculate the logical similarity between two models
        import logic as lgc
        similarity = lgc.logical_similarity(model1, model2)

        return similarity
    # Define a function that takes in a list of models and returns the model that is most similar
    # to the other models.

    def most_similar_model(self, models):
        # Calculate the similarity between each pair of models
        similarities = []
        for model1 in models:
            for model2 in models:
                similarity = self.model_similarity(model1, model2)
                similarities.append(similarity)
        # Return the model that is most similar to the other models
        return most_similar_model


    def select_model(self, dataset):
        # Select most objective model for the dataset using logic.py functions
        import logic as lgc
        objective_model = lgc.select_most_logical(self.models, dataset)

        return objective_model


