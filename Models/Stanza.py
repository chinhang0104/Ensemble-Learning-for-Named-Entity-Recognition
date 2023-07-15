import stanza

from BaseModel import BaseModel

class Stanza(BaseModel):
    def __init__(self, name = "stanza"):
        super().__init__(name)

    ## @brief 
    # Setting up recognize
    def recognize(self, _input = None):
        if _input is None:
            _input = self.input
        nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
        self.recognized_result = nlp(_input)

    ## @brief 
    # Get human names
    def get_human_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        human = set()
        for ent in _recognized_result.ents:
            if ent.type == 'PERSON':
                human.add(ent.text.strip())
        return human

    ## @brief 
    # Get company names
    def get_company_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        company = set()
        for ent in _recognized_result.ents:
            if ent.type == 'ORG':
                company.add(ent.text.strip())
        return company