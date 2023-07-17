# Ensemble-Learning-for-Named-Entity-Recognition
Provides a platform for ensemble learning in the field of Named Entity Recognition.

## Features
Unified API: Provide classes that unify the API of various NER packages, simplifying the process of integrating different models into an ensemble. \
Easy features developement: Easily add, remove, and modify model features. For example, you can augment add location recognition capabilities by creating get_location function in Model class. \
Model Management: Flexible to add, remove, and modify NER models within the ensemble. This can be archieved by creating a subclass of Model. \
Customizable Ensembling Decision Rule: Simple way to modify the decision rule for ensembling. Common rules are ready to use.

## Benchmark 
This repository contains benchmark results for various models on the task of people recognition using the CoNLL-2003 dataset. \
The test set results for individual models and an ensemble method are provided below.
https://huggingface.co/datasets/tner/conll2003

### Result
#### Individual Model Performances
The following table shows the performance metrics of different models on the test set:
 Model      | Acuracy | Precision  | Recall
 --- | --- | ---| ---
 Ensembled|**0.6468842729970327** | **0.9159663865546218** | 0.6876971608832808
 spacy      | 0.49204328453214513| 0.7184014869888475| 0.6096214511041009 
stanza|0.5831593597773138| 0.8321747765640516| 0.6608832807570978
nltk|0.46747967479674796| 0.5679012345679012| **0.7255520504731862**

#### Ensemble Method
By using a simple ensemble method with at least two out of three voting, significant improvements achieved in accuracy and precision compared to the best model within the ensemble.
Metrics|	Improved Result
 --- | --- 
Accuracy|	64.7% (+6.4%)
Precision|	91.6% (+8.4%)

#### Confusion Matrix for the Ensemble Model
The confusion matrix for the ensemble model is as follows:
 Model      | True Positive | False Positive  | False Negative
 --- | --- | ---| ---
 Ensembled|872| **80**| 396
 spacy      | 773 | 303| 495 
stanza|838| 169| 430
nltk|**920**| 700| **348**

The benchmark results demonstrate that the ensemble method performs remarkably better in terms of accuracy and precision compared to individual models. 

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
Support loading multiple datasets - in progress.
C++ version. \
Show recognized result's index in string. \
CICD

## Reference
nltk: https://github.com/nltk/nltk/ \
spacy: https://github.com/explosion/spaCy/ \
LAC: https://github.com/baidu/lac/ \
stanza: https://github.com/stanfordnlp/stanza/ \
hanlp: https://github.com/hankcs/HanLP
