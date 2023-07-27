#include <iostream>

#include "BaseModel.h"
#include "DemoModel.h"
#include "VotingClassifier.h"
int main(){
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
	std::vector<std::set<std::string>> recognizedResults = {};
	recognizedResults.push_back(humans);
	recognizedResults.push_back(companies);
	v.buildVotingMatrix(&recognizedResults);
	std::vector<const std::string*> result = v.weightedAverageProbabilities();
	for (int i = 0; i < result.size(); ++i) {
		std::cout << *result[i] << std::endl;
	}
}