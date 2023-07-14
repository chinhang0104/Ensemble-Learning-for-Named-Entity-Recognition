from typing import Optional
class Scoring:
    # Scoring and weighting
    
    def __init__(self, _models: Optional[list] = None):
        self.models = _models
        self.summed_weight = 0
        self.scoring_matrix = None
    
    def __str__(self) -> str:
        return f"Loaded models: {self.models}"
    
    ## @brief
    # Sum models' weight
    # @param _models list of model instances
    # @return Summed up weight
    def sum_weight(self, _models: Optional[list] = None) -> float:
        if _models == None:
            _models = self.models
        sum_of_weight = 0
        for model in _models:
            sum_of_weight += model.weight
        self.summed_weight = sum_of_weight
        return sum_of_weight
    
    ## @brief
    # Create a dictionay that has key-value pairs represcenting word and its total score.
    # @param recognized_results List of sets. Each set is contains entity recognized by a model, 
    # for example, return from Model.get_human_name()
    # @param _models list of model instances
    # @return The dictionary that has key-value pairs represcenting word and its total score.
    def build_scoring_matrix(self, recognized_results: list, _models: Optional[list] = None) -> dict:
        if _models == None:
            _models = self.models        
        # Summing up score for each word
        _scoring_matrix = {}
        for i in range(len(recognized_results)):
            for word in recognized_results[i]:
                if word in _scoring_matrix:
                    _scoring_matrix[word] += _models[i].weight
                else:
                    _scoring_matrix[word] = _models[i].weight
        self.scoring_matrix = _scoring_matrix
        return _scoring_matrix
    
    ## @brief
    # Find the list of entities that has highest score.
    # @param _scoring_matrix Dictionary of word, score pair. Default is self.scoring_matrix.
    # @return The list of entities.    
    def highest_score(self, _scoring_matrix: Optional[dict] = None) -> list:
        if _scoring_matrix == None:
            _scoring_matrix = self.scoring_matrix
        return [key for key, value in _scoring_matrix.items() if value == max(_scoring_matrix.values())]
    
    ## @brief
    # Find the list of entities that has score within percentage of highest score.
    # @param percentage The percentage. For example, 0.8 means find all entities that has score at least 
    # 80 percent of highest score.
    # @param _scoring_matrix Dictionary of word, score pair. Default is self.scoring_matrix.
    # @return The list of entities.     
    def percentage_within_highest_score(self, percentage = 0.8, _scoring_matrix: Optional[dict] = None) -> list:
        if _scoring_matrix == None:
            _scoring_matrix = self.scoring_matrix
        return [key for key, value in _scoring_matrix.items() if value >= max(_scoring_matrix.values()) * percentage]
    
    ## @brief
    # Find the list of entities that has score within percentage of total score.
    # @param percentage The percentage. For example, 0.8 means find all entities that has score at least 
    # 80 percent of total score.
    # @param _summed_weight Total weight. Default is self.summed_weight.
    # @param _scoring_matrix Dictionary of word, score pair. Default is self.scoring_matrix.
    # @return The list of entities.  
    def minimum_weighted_score(self, percentage = 0.8, _summed_weight: Optional[float] = None, _scoring_matrix: Optional[dict] = None) -> list:
        if _summed_weight == None:
            _summed_weight = self.summed_weight
        if _scoring_matrix == None:
            _scoring_matrix = self.scoring_matrix
        return[key for key, value in _scoring_matrix.items() if value >= _summed_weight * percentage]