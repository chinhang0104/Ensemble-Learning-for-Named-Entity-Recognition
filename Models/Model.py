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

class Model:    
    # A template of NLP model.

    ## @brief 
    # Constructor for Model.
    # @param name: Name of the model.
    # @param weight: Scoring weight of the model.
    # @param input: Text that wanted to be recognize.
    def __init__(self, name=None, weight=1.0, input="", init=None, recognize=None, get_human_name=None, get_company_name=None) -> None:
        self.name = name
        self.weight = weight
        self.input = input
        self._init = init() if init else None
        self._recognize = recognize() if recognize else None
        self._get_human_name = get_human_name() if get_human_name else None
        self._get_company_name = get_company_name() if get_company_name else None
        self.recognized_result = ""

    def __str__(self) -> str:
        return self.name
    
    
    