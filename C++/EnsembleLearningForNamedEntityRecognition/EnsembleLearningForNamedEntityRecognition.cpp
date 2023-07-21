#include <iostream>

#include "BaseModel.h"
#include "DemoModel.h"
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

}