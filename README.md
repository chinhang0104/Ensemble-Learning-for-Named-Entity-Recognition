# Named-Entity-Recognition
Utilize multiple Named Entity Recogniztion packages to detect human name and organization and determine the final output by conducting a voting process among the NER packages.

## Methodology
This program extracts all person and organization names from the given input 'text' (String).\
It utilizes three open-source Named Entity Recogniztion packages for each of two supported languages - English and Chinese.\
For English, nltk, spacy, and stanza are utilized. For Chinese, hanlp, lac, and stanza are utilized.
The final output is determined by a voting mechanism among the Named Entity Recogniztion packages.\
The 'rule' parameter specifies the minimum number of agreements required for a phrase to be classified as a person or organization.\
By default, the program starts with a flexible selection approach, trying rule = 3 first, then rule = 2, and finally rule = 1.\
The program returns four sets: English person names, Chinese person names, English organization names, and Chinese organization names.

## API
First argument: The input text to perform Named Entity Recogniztion.\
Second argument (optional): The minimum number of agreements required for a phrase to be classified as a person or organization.

## Example
English Text:
I am writing this letter to confirm that Edward Smith has been employed with Dexter Insurance Company since April , and is a reliable and trustworthy insurance agent for this company.

Results of each NER packages:\
English People Name:\
{'Dexter Insurance Company', 'Edward Smith'}\
{'Edward Smith'}\
{'Edward Smith'} \
English Company Name: \
None \
{'Dexter Insurance Company'}\
{'Dexter Insurance Company'}

Ensembled result:\
People: {'Edward Smith'}\
Company: {'Dexter Insurance Company'}

## Installation
pip install nltk==3.5\
pip install spacy==1.0.4\
pip install lac==2.1.2\
pip install stanza==1.5.0\
pip install hanlp==2.1.0b50\
pip install numpy==1.24.3\
pip install markupsafe==2.1.1\
python -m spacy download en_core_web_sm

## Reference
nltk: https://github.com/nltk/nltk/ \
spacy: https://github.com/explosion/spaCy/ \
LAC: https://github.com/baidu/lac/ \
stanza: https://github.com/stanfordnlp/stanza/ \
hanlp: https://github.com/hankcs/HanLP
