class Model:    
    # A template of NLP model.

    ## @brief 
    # Constructor for Model.
    # @param name: Name of the model.
    # @param weight: Scoring weight of the model.
    # @param input: Text that wanted to be recognize.
    def __init__(self, name=None, weight=1.0, input="", language = "English") -> None:
        self.name = name
        self.weight = weight
        self.input = input
        self.language = language

    def __str__(self) -> str:
        return f"Model: {self.name}, Support language: {self.language}"
    
    def init(self) -> None:
        """
        Things to do when an user first time loading the model. For example, downloading model and dictionary.
        """
        pass

    ## @brief 
    # Recognize the input and stores NER results in regcognized_result.
    # For example, self.regcognized_result = sth recognized from input        
    # @param text: Text for recognize. Default is self.input.
    def recognize(self, text = input) -> None:
        # self.regcognized_result = sth recognized from input
        pass

    ## @brief 
    # Template for extracting human name from regcognized_result      
    # @param text: Text for recognize. Default is self.regcognized_result. 
    # @return All human name regcognized stored in a set.
    def get_human_name(self, text = None) -> set:
        #if text is None:
        #    text = self.regcognized_result
        # Code below to extract human name here
        return {}

    ## @brief 
    # Template for extracting company name from regcognized_result      
    # @param text: Text for recognize. Default is self.regcognized_result.\
    # @return All company name regcognized stored in a set.
    def get_company_name(self, text = None) -> set:
        #if text is None:
        #    text = self.regcognized_result
        # Code below to extract company name here
        return {}
        
    