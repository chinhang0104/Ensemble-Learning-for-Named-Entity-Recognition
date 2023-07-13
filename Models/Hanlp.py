import hanlp

from Model import Model

class Hanlp(Model):
    def __init__(self, name = "hanlp"):
        super().__init__(name)

    ## @brief 
    # Setting up recognize
    def recognize(self, _input = None):
        if _input is None:
            _input = self.input
        HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH, tasks=['ner/ontonotes'])
        self.recognized_result = HanLP(_input)

    ## @brief 
    # Get human names
    def get_human_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        human = set()
        for i in _recognized_result['ner/ontonotes']:
                if i[1] == 'PERSON':
                    human.add(i[0])
        return human

    ## @brief 
    # Get company names
    def get_company_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        company = set()
        for i in _recognized_result['ner/ontonotes']:
                if i[1] == 'ORG':
                    company.add(i[0])
        return company