import sys
sys.path.append("Models")
import json

import Stanza
import Spacy
import Nltk
import Lac
import Hanlp
import Scoring

# Create intances of models
stanza_instance = Stanza.Stanza()
spacy_instance = Spacy.Spacy()
nltk_instance = Nltk.Nltk()
lac_instance = Lac.Lac()
#hanlp_instance = Hanlp.Hanlp()

models = [stanza_instance, spacy_instance, nltk_instance, lac_instance]

text = "I am writing this letter to confirm that Edward Smith has been employed with Dexter Insurance Company since April , and is a reliable and trustworthy insurance agent for this company."

# Recognize text
for model in models:
    model.recognize(text)

# Get human names
humans = []
for model in models:
    humans.append(model.get_human_name())

# Get company names
companies = []
for model in models:
    companies.append(model.get_company_name())

# Finding the suitable entities by ensemble laerning
scoring_instance = Scoring(models)
# Human first
scoring_instance.build_scoring_matrix(humans)
# Different scoring methods
human_found = scoring_instance.highest_score()
#human_found = scoring_instance.percentage_within_highest_score()
#human_found = scoring_instance.minimum_weighted_score()
# Company after
scoring_instance.build_scoring_matrix(companies)
# Different scoring methods
company_found = scoring_instance.highest_score()
#company_found = scoring_instance.percentage_within_highest_score()
#company_found = scoring_instance.minimum_weighted_score()

# Write the result to a json file
json_to_write = json.dumps({"humans": human_found, "companies": company_found})
with open("./result.json", "w", encoding="utf8") as f:
    f.write(json_to_write)