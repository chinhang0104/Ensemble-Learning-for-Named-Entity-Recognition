#include <iostream>

#include "BaseModel.h"
#include "DemoModel.h"
#include "VotingClassifier.h"
int main(){
	//BaseModel model = BaseModel("Hello");
	//model.setName("Demo");
	DemoModel demo = DemoModel();
	std::cout << demo.about() << std::endl;
	demo.recognize("");
	std::set<std::string> humans = demo.getHumanName();
	for (std::set<std::string>::iterator it = humans.begin(); it != humans.end(); it++) {
		std::cout << *it << std::endl;
	}
	std::set<std::string> companies = demo.getCompanyName();
	for (std::set<std::string>::iterator it = companies.begin(); it != companies.end(); it++) {
		std::cout << *it << std::endl;
	}
	std::vector<BaseModel*> _models = {new BaseModel("BaseClass"), new DemoModel("SubClass")};
	VotingClassifier v = VotingClassifier(_models);
	std::cout << v.about() << std::endl;
	if (0.0) {
		std::cout << "WRONG";
	}
}