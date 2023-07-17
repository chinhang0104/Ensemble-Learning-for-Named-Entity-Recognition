from LAC import LAC

from BaseModel import BaseModel

class Lac(BaseModel):
    def __init__(self, name = "lac"):
        super().__init__(name)

    ## @brief 
    # Setting up recognize
    def recognize(self, _input = None):
        if _input is None:
            _input = self.input
        lac = LAC(mode='lac')
        self.recognized_result = lac.run(_input)

    ## @brief 
    # Get human names
    def get_human_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        human = set()
        for i in range(len(_recognized_result[0])):
                if _recognized_result[1][i] == 'PER':
                    human.add(_recognized_result[0][i])
        return human

    ## @brief 
    # Get company names
    def get_company_name(self, _recognized_result = None) -> set:
        if _recognized_result is None:
            _recognized_result = self.recognized_result
        company = set()
        for i in range(len(_recognized_result[0])):
                if _recognized_result[1][i] == 'ORG':
                    company.add(_recognized_result[0][i])
        return company