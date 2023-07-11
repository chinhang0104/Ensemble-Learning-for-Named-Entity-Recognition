# Named-Entity-Recognition
Utilize multiple Named Entity Recogniztion packages to detect human name and organization and determine the final output by conducting a voting process among the NER packages.

## Methodology
This program extracts all person and organization names from the given input 'text' (String).\n
It utilizes three open-source Named Entity Recogniztion packages for each of two supported languages - English and Chinese.\n
For English, nltk, spacy, and stanza are utilized. For Chinese, hanlp, lac, and stanza are utilized.
The final output is determined by a voting mechanism among the Named Entity Recogniztion packages.\n
The 'rule' parameter specifies the minimum number of agreements required for a phrase to be classified as a person or organization.\n
By default, the program starts with a flexible selection approach, trying rule = 3 first, then rule = 2, and finally rule = 1.\n
The program returns four sets: English person names, Chinese person names, English organization names, and Chinese organization names.\n

## API
First argument: The input text to perform Named Entity Recogniztion.\n
Second argument (optional): The minimum number of agreements required for a phrase to be classified as a person or organization.

## Installation
pip install nltk==3.5\n
pip install spacy==1.0.4\n
pip install lac==2.1.2\n
pip install stanza==1.5.0\n
pip install hanlp==2.1.0b50\n
pip install numpy==1.24.3\n
pip install markupsafe==2.1.1\n
python -m spacy download en_core_web_sm

## Reference
nltk: https://github.com/nltk/nltk/\n
spacy: https://github.com/explosion/spaCy/\n
LAC: https://github.com/baidu/lac/\n
stanza: https://github.com/stanfordnlp/stanza/\n
hanlp: https://github.com/hankcs/HanLP
