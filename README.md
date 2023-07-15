# Ensemble-Learning-for-Named-Entity-Recognition
Provides a platform for ensemble learning in the field of Named Entity Recognition.

## Features
Unified API: Provide classes that unify the API of various NER packages, simplifying the process of integrating different models into an ensemble. \
Easy features developement: Easily add, remove, and modify model features. For example, you can augment add location recognition capabilities by creating get_location function in Model class. \
Model Management: Flexible to add, remove, and modify NER models within the ensemble. This enables you to experiment with different models. \
Customizable Ensembling Decision Rule: Simple way to modify the decision rule for ensembling. This allows you to fine-tune the behavior of the ensemble and optimize performance based on your requirements.

## Benchmark 
Work in progress.

## Demos
Class demo: \
Example of using APIs and construct classes.

Commond line program demo: \
Example of using commond line program to read text files and put recognized entities into a json file. \
Argument: The path of text files to perform Named Entity Recogniztion.

## Installation
pip install nltk==3.5\
pip install spacy==1.0.4\
pip install lac==2.1.2\
pip install stanza==1.5.0\
pip install hanlp==2.1.0b50\
pip install numpy==1.24.3\
pip install markupsafe==2.1.1\
python -m spacy download en_core_web_sm

## Documents
Full documents refer to release. 
Support doxygen.

## To do
C++ version. \
Show recognized result's index in string. \
CICD

## Reference
nltk: https://github.com/nltk/nltk/ \
spacy: https://github.com/explosion/spaCy/ \
LAC: https://github.com/baidu/lac/ \
stanza: https://github.com/stanfordnlp/stanza/ \
hanlp: https://github.com/hankcs/HanLP
