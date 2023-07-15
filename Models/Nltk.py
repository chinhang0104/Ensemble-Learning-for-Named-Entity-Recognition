import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import ne_chunk

from BaseModel import BaseModel

class Nltk(BaseModel):    
    def __init__(self):
        super().__init__(name = "nltk")

    def init(self) -> None:
        """
        Downloading model and dictionary.
        """
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')

    ## @brief 
    # Setting up recognize
    def recognize(self, _input = None):
        if _input is None:
            _input = self.input
        self.recognized_result = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(_input)))

    ## @brief 
    # Get human names
    def get_human_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        human = set()
        for phase in _recognized_result:
            if type(phase) is nltk.Tree:
                if phase.label() == 'PERSON':
                    human_char = ''
                    for i in phase.leaves():
                        human_char += (i[0] + ' ') 
                    human.add(human_char.strip())
        return human

    ## @brief 
    # Get company names
    def get_company_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        company = set()
        for phase in _recognized_result:
            if type(phase) is nltk.Tree:
                if phase.label() == 'ORGANIZATION':
                    company_char = ''
                    for i in phase.leaves():
                        company_char += (i[0] + ' ') 
                    company.add(company_char.strip())
        return company