"""! @brief Ensemble Learning for Named Entity Recognition"""

##
# @mainpage Ensemble Learning for Named Entity Recognition
# @brief Provides a platform for ensemble learning in the field of Named Entity Recognition.
#
# @section Features
# Unified API: Provide classes that unify the API of various NER packages, simplifying the process of integrating different models into an ensemble. \n
# Easy features developement: Easily add, remove, and modify model features. For example, you can augment add location recognition capabilities by creating get_location function in Model class. \n
# Model Management: Flexible to add, remove, and modify NER models within the ensemble. This can be archieved by creating a subclass of Model. \n
# Customizable Ensembling Decision Rule: Simple way to modify the decision rule for ensembling. Common rules are ready to use.
#
# @section Demos
# Class demo: \n
# Example of using APIs and construct classes. \n
# \n
# Commond line program demo: \n
# Example of using commond line program to read text files and put recognized entities into a json file. \n
# Argument: The path of text files to perform Named Entity Recogniztion.
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