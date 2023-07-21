#pragma once
#include <vector>
#include "BaseModel.h"
class DemoModel : public BaseModel {
private:
    std::vector<std::string> regcognized_result = {};
public:
    DemoModel(std::string _name = "Demo", float _weight = 1.0, std::string _input = "", std::string _language = "English, Chinese");
    void recognize(std::string text);
    std::set<std::string> getHumanName(std::vector<std::string> text = {});
    std::set<std::string> getCompanyName(std::vector<std::string> text = {});
};

