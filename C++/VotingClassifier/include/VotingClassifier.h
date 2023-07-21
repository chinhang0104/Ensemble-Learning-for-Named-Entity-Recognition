#pragma once
#include <map>
#include <vector>
#include "BaseModel.h"
class VotingClassifier {
private:
	std::vector<std::unique_ptr<BaseModel>> models;
	std::map<std::string, float> votingMatrix;
public:

};