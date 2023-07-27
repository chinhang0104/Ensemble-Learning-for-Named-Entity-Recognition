#pragma once
#include <string>
#include <set>
#include <sstream>

class BaseModel {
protected:
	std::string name;
	float weight;
	std::string input;
	std::string language;
public:
	std::string getName();
	void setName(std::string _name);
	float getWeight();
	void setWeight(float _weight);
	std::string getInput();
	void setInput(std::string _input);
	std::string getLanguage();
	void setLanguage(std::string _language);
	/**
	 * @brief Constructor for Model
	 * @param _name Name of the model.
	 * @param _weight Scoring weight of the model.
	 * @param _input Text that wanted to be recognize.
	 * @param _language Language of model supported.
	*/
	BaseModel(std::string _name = "", float _weight = 1.0, std::string _input = "", std::string _language = "English");
	/**
	 * @brief Get the general inforamtion of the model.
	 * @return Model's name and language supported.
	*/
	std::string about();
	/**
	 * @brief Things to do when an user first time loading the model. For example, downloading model and dictionary.
	*/
	virtual void init();
	/**
	 * @brief Recognize the input and stores NER results in regcognized_result.
	 * For example, self.regcognized_result = sth recognized from input
	 * @param text Text for recognize. Default is self.input.
	*/
	virtual void recognize(std::string text);
	/**
	 * @brief Template for extracting human name from regcognized_result
	 * @tparam T Class of regcognized result created by recognize
	 * @param text Text for recognize. Default is regcognized_result.
	 * @return All human name regcognized stored in a set.
	*/
	template<class T>
	std::set<std::string> getHumanName(T text);
	/**
	 * @brief Template for extracting company name from regcognized_result
	 * @tparam T Class of regcognized result created by recognize
	 * @param text Text for recognize. Default is regcognized_result.
	 * @return All company name regcognized stored in a set.
	*/
	template<class T>
	std::set<std::string> getCompanyName(T text);
};