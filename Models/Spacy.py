import spacy
from spacy import displacy
import en_core_web_sm

from BaseModel import BaseModel

class Spacy(BaseModel):
    def __init__(self, name = "spacy"):
        super().__init__(name)

    ## @brief 
    # Setting up recognize
    def recognize(self, _input = None):
        if _input is None:
            _input = self.input
        nlp = en_core_web_sm.load()
        self.recognized_result = nlp(_input)

    ## @brief 
    # Get human names
    def get_human_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        human = set()
        for entity in _recognized_result.ents:
            if entity.label_ == 'PERSON':
                human.add(entity.text)
        return human

    ## @brief 
    # Get company names
    def get_company_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        company = set()
        for entity in _recognized_result.ents:
            if entity.label_ == 'ORG':
                company.add(entity.text)
        return company