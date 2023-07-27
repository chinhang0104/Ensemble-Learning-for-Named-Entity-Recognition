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
	/**
	 * @brief Constructor of VotingClassifier
	 * @param _models Vector of Models class pointer. Will perform sumWeight() automatically.
	*/
	VotingClassifier(std::vector<BaseModel*> _models = {});
	std::string about();
	/**
	 * @brief Sum up all models' weight and store it in summedWeight. This function will be called automatically during construction.
	 * @param _models Vector of Models class pointer. 
	 * @return Summed weight
	*/
	float sumWeight(std::vector<BaseModel*> _models = {});
	/**
	 * @brief Create a dictionay that has key-value pairs represcenting word and its total score.
	 * @param recognized_results Vector of sets. Each set is contains entity recognized by a model, for example, return from BaseModel::getHumanName()
	 * @param _models Vector of model class.
	 * @return The map that has key-value pairs represcenting word and its total score.
	*/
	std::map<std::string, float> buildVotingMatrix(std::vector<std::set<std::string>>* recognizedResults, std::vector<BaseModel*> _models = {});
	/**
	 * @brief Find the highest score words among votingMatrix
	 * @param _votingMatrix The word-score pair map. Default is VotingClassifier::votingMatrix
	 * @return The highest score
	*/
	float findMaxScore(std::map<std::string, float>* _votingMatrix = nullptr);
	/**
	 * @brief Weighted Average Probabilities (Soft Voting as sklearn). Can used as Majority Voting (Hard Voting as sklearn) when are models' weight are set as equal.
	 * @param _votingMatrix Map of word, score pair. Default is VotingClassifier::votingMatrix.
	 * @return The vector of entities' string pointers.  
	*/
	std::vector<const std::string*> weightedAverageProbabilities(std::map<std::string, float>* _votingMatrix = nullptr);
	/**
	 * @brief Find the list of entities that has score within percentage of highest score.
	 * @param percentage The percentage. For example, 0.8 means find all entities that has score at least 80 percent of highest score.
	 * @param _votingMatrix Map of word, score pair. Default is VotingClassifier::votingMatrix.
	 * @return The vector of entities' string pointers.  
	*/
	std::vector<const std::string*> percentageWithinHighestScore(float percentage = 0.8, std::map<std::string, float>* _votingMatrix = nullptr);
	/**
	 * @brief Find the list of entities that has score within percentage of total score.
	 * @param percentage The percentage. For example, 0.8 means find all entities that has score at least 80 percent of total score.
	 * @param _votingMatrix Map of word, score pair. Default is VotingClassifier::votingMatrix.
	 * @return The vector of entities' string pointers. 
	*/
	std::vector<const std::string*> minimumWeightedScore(float percentage = 0.8, std::map<std::string, float>* _votingMatrix = nullptr);
};