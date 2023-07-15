"""! @brief Named Entity Recogniztion"""

##
# @mainpage Named Entity Recogniztion using Ensemble Learning
# @brief Utilize multiple Named Entity Recogniztion packages to detect human name and organization and 
# determine the final output by conducting a voting process among the NER packages.
#
# @section Methodology
# This program extracts all person and organization names from the given input 'text' (String).\n
# It utilizes three open-source Named Entity Recogniztion packages for each of two supported languages - English and Chinese.\n
# For English, nltk, spacy, and stanza are utilized. For Chinese, hanlp, lac, and stanza are utilized.
# The final output is determined by a voting mechanism among the Named Entity Recogniztion packages.\n
# The 'rule' parameter specifies the minimum number of agreements required for a phrase to be classified as a person or organization.\n
# By default, the program starts with a flexible selection approach, trying rule = 3 first, then rule = 2, and finally rule = 1.\n
# The program returns four sets: English person names, Chinese person names, English organization names, and Chinese organization names.\n# 
#
# @section API
# First argument: Text files to perform Named Entity Recogniztion.\n
# Return: 
#
# @section Installation
# pip install nltk==3.5\n
# pip install spacy==1.0.4\n
# pip install lac==2.1.2\n
# pip install stanza==1.5.0\n
# pip install hanlp==2.1.0b50\n
# pip install numpy==1.24.3\n
# pip install markupsafe==2.1.1\n
# python -m spacy download en_core_web_sm
#
# @section Reference
# nltk: https://github.com/nltk/nltk/\n
# spacy: https://github.com/explosion/spaCy/\n
# LAC: https://github.com/baidu/lac/\n
# stanza: https://github.com/stanfordnlp/stanza/\n
# hanlp: https://github.com/hankcs/HanLP

import sys
sys.path.append("Models")
import Stanza
import Spacy
import Nltk
import Lac
#import Hanlp
import VotingClassifier

def dataloader(file_path: str) -> str:
    # Reading txt file (file_path)
    # Return the text as string
    with open (file_path, 'r', encoding="utf8") as f:
        return f.read()

if __name__ == "__main__":
    # Create intances of models
    stanza_instance = Stanza.Stanza()
    spacy_instance = Spacy.Spacy()
    nltk_instance = Nltk.Nltk()
    lac_instance = Lac.Lac()
    #hanlp_instance = Hanlp.Hanlp()
    models = [stanza_instance, spacy_instance, nltk_instance, lac_instance]
    file_paths = str(sys.argv[1]).split(", ")

    results_for_output = {"File": {}}

    for file in file_paths:

        # Recognize text
        for model in models:
            model.recognize(dataloader(file))

        # Get human names
        humans = []
        for model in models:
            humans.append(model.get_human_name())

        # Get company names
        companies = []
        for model in models:
            companies.append(model.get_company_name())

        # Finding the suitable entities by ensemble laerning
        voting_instance = VotingClassifier.VotingClassifier(models)
        # Human first
        voting_instance.build_voting_matrix(humans)
        # Different voting methods
        human_found = voting_instance.highest_score()
        #human_found = voting_instance.percentage_within_highest_score()
        #human_found = voting_instance.minimum_weighted_score()
        # Company after
        voting_instance.build_voting_matrix(companies)
        # Different voting methods
        company_found = voting_instance.highest_score()
        #company_found = voting_instance.percentage_within_highest_score()
        #company_found = voting_instance.minimum_weighted_score()
        
        # Add recognized results
        results_for_output["File"][file] = {"Recognized Entities": {"humans": human_found, "companies": company_found}}

    # Write the result to a json file
    json_to_write = json.dumps(results_for_output)
    with open("./result.json", "w", encoding="utf8") as f:
        f.write(json_to_write)