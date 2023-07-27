#include "VotingClassifier.h"
VotingClassifier::VotingClassifier(std::vector<BaseModel*> _models){
	if (!_models.empty()) {
		models = _models;
		sumWeight();
	}
}
std::string VotingClassifier::VotingClassifier::about() {
	std::stringstream ss;
	ss << "Loaded models: ";
	for (int i = 0; i < models.size(); ++i) {
		ss << models[i]->getName() << ", ";
	}
	ss << "Total weight: " << summedWeight;
	return ss.str();
}
float VotingClassifier::sumWeight(std::vector<BaseModel*> _models) {
	if (_models.empty()) {
		_models = models;
	}
	else {
		models = _models;
	}
	float sumOfWeight = 0.0;
	for (int i = 0; i < _models.size(); ++i) {
		sumOfWeight += _models[i]->getWeight();
	}
	summedWeight = sumOfWeight;
	return summedWeight;
}
std::map<std::string, float> VotingClassifier::buildVotingMatrix(std::vector<std::set<std::string>>* recognizedResults, std::vector<BaseModel*> _models) {
	if (_models.empty()) {
		_models = models;
	}
	else {
		models = _models;
	}
	std::map<std::string, float> _votingMatrix = {};
	for (int i = 0; i < recognizedResults->size(); ++i) {
		if (!recognizedResults[i].empty()) {
			for (std::set<std::string>::iterator it = (*recognizedResults)[i].begin(); it != (*recognizedResults)[i].end(); it++) {
				if (_votingMatrix.find(*it) != _votingMatrix.end()) {
					_votingMatrix[*it] += _models[i]->getWeight();
				}
				else {
					_votingMatrix[*it] = _models[i]->getWeight();
				}

			}
		}
	}
	votingMatrix = _votingMatrix;
	return votingMatrix;
}
float VotingClassifier::findMaxScore(std::map<std::string, float>* _votingMatrix) {
	if (!_votingMatrix) {
		_votingMatrix = &votingMatrix;
	}
	float _maxScore = 0.0;
	for (std::map<std::string, float>::iterator it = _votingMatrix->begin(); it != _votingMatrix->end(); it++) {
		_maxScore = std::max(maxScore, it->second);
	}
	maxScore = _maxScore;
	return maxScore;
}
std::vector<const std::string*> VotingClassifier::weightedAverageProbabilities(std::map<std::string, float>* _votingMatrix) {
	if (!_votingMatrix) {
		_votingMatrix = &votingMatrix;
	}
	findMaxScore();
	std::vector<const std::string*> results = {};
	for (std::map<std::string, float>::iterator it = _votingMatrix->begin(); it != _votingMatrix->end(); it++) {
		if (it->second == maxScore) {
			results.push_back(&(it->first));
		}
	}
	return results;
}
std::vector<const std::string*> VotingClassifier::percentageWithinHighestScore(float percentage, std::map<std::string, float>* _votingMatrix) {
	if (!_votingMatrix) {
		_votingMatrix = &votingMatrix;
	}
	float cutoffScore = findMaxScore()*percentage;
	std::vector<const std::string*> results = {};
	for (std::map<std::string, float>::iterator it = _votingMatrix->begin(); it != _votingMatrix->end(); it++) {
		if (it->second >= cutoffScore) {
			results.push_back(&(it->first));
		}
	}
	return results;
}
std::vector<const std::string*> VotingClassifier::minimumWeightedScore(float percentage, std::map<std::string, float>* _votingMatrix) {
	if (!_votingMatrix) {
		_votingMatrix = &votingMatrix;
	}
	float cutoffScore = summedWeight * percentage;
	std::vector<const std::string*> results = {};
	for (std::map<std::string, float>::iterator it = _votingMatrix->begin(); it != _votingMatrix->end(); it++) {
		if (it->second >= cutoffScore) {
			results.push_back(&(it->first));
		}
	}
	return results;
}