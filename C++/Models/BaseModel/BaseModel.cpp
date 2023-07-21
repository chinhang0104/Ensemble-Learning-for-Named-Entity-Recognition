#include <string>
#include <set>
#include <sstream>

#include "BaseModel.h"

std::string BaseModel::getName() { return name; }
void BaseModel::setName(std::string _name) { name = _name; }
float BaseModel::getWeight() { return weight; }
void BaseModel::setWeight(float _weight) { weight = _weight; }
std::string BaseModel::getInput() { return input; }
void BaseModel::setInput(std::string _input) { input = _input; }
std::string BaseModel::getLanguage() { return language; }
void BaseModel::setLanguage(std::string _language) { language = _language; }
BaseModel::BaseModel(std::string _name, float _weight, std::string _input, std::string _language) {
	name = _name;
	weight = _weight;
	input = _input;
	language = _language;
}
std::string BaseModel::about() {
	std::stringstream ss;
	ss << "Model: " << name << ", Support language: " << language;
	return ss.str();
	//return std::format(Model: {}, Support language: {}, name, language); //// Supported on C++ 20
}

void BaseModel::init() {}
void BaseModel::recognize(std::string text = "") {
	if (text.empty()) {
		text = input;
	}
	// auto regcognized_result = sth recognized from input
}
template<class T>
std::set<std::string> BaseModel::getHumanName(T text) {
	if (text == NULL) {
		// text = regcognized_result;
	}
}
template<class T>
std::set<std::string> BaseModel::getCompanyName(T text) {
	if (text == NULL) {
		// text = regcognized_result;
	}
}
