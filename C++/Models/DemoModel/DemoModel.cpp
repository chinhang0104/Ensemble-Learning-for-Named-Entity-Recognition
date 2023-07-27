#include "DemoModel.h"
#include <vector>
DemoModel::DemoModel(std::string _name, float _weight, std::string _input, std::string _language) {
	name = _name;
	weight = _weight;
	input = _input;
	language = _language;
}
void DemoModel::recognize(std::string text = "") {
	if (text.empty()) {
		text = input;
	}
	regcognized_result = {"Human name", "Organization name"};
}
std::set<std::string> DemoModel::getHumanName(std::vector<std::string> text) {
	if (text.empty()) {
		text = regcognized_result;
	}
	std::set<std::string> humanNames = std::set<std::string>();
	humanNames.insert(text[0]);
	return humanNames;
};
std::set<std::string> DemoModel::getCompanyName(std::vector<std::string> text) {
	if (text.empty()) {
		text = regcognized_result;
	}
	std::set<std::string> companyNames = std::set<std::string>();
	companyNames.insert(text[1]);
	return companyNames;
};