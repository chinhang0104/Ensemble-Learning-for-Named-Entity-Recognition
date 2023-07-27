#pragma once
#include <map>
#include <vector>
#include "BaseModel.h"
class VotingClassifier {
private:
	std::vector<BaseModel*>  models;
	std::map<std::string, float> votingMatrix = {};
	float summedWeight = 0.0;
	float maxScore = 0.0;
public:
	VotingClassifier(std::vector<BaseModel*> _models = {});
	std::string about();
	float sumWeight(std::vector<BaseModel*> _models = {});
	std::map<std::string, float> buildVotingMatrix(std::vector<std::set<std::string>> recognizedResults, std::vector<BaseModel*> _models = {});
	float findMaxScore(std::map<std::string, float>* _votingMatrix = nullptr);
	std::vector<const std::string*> weightedAverageProbabilities(std::map<std::string, float>* _votingMatrix = nullptr);
	//std::vector<const std::string*> percentageWithinHighestScore(float percentage = 0.8, std::map<std::string, float>* _votingMatrix = nullptr);
	//std::vector<const std::string*> minimumWeightedScore(float percentage = 0.8, std::map<std::string, float>* _votingMatrix = nullptr);
};