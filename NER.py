"""! @brief Named Entity Recogniztion"""

##
# @mainpage Named Entity Recogniztion Project
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
# The program returns four sets: English person names, Chinese person names, English organization names, and Chinese organization names.\n
# 
#
# @section API
# First argument: The input text to perform Named Entity Recogniztion.\n
# Second argument (optional): The minimum number of agreements required for a phrase to be classified as a person or organization.
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
#import csv
from collections import Counter
from tkinter import CHAR
import re
import traceback
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import ne_chunk
import spacy
from spacy import displacy
import en_core_web_sm
from LAC import LAC
import stanza
import hanlp

# Setup for packages
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nlp = en_core_web_sm.load()
lac_seg = LAC(mode='seg')
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH, tasks=['ner/ontonotes'])

"""""
def dataloader(file_path: str) -> str:
    # Reading txt file (file_path)
    # Return the text as string
    text = []
    with open (file_path, 'r', encoding="utf8") as f:
        reader = csv.reader(f,delimiter='\t')
        for row in reader:
            text.append(' '.join(row))
    return ' '.join(text)
"""""
def NLTK_NER(text: str):
    chunks = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))
    temp = []
    temp_org = []
    for phase in chunks:
        if type(phase) is nltk.Tree:
            if phase.label() == 'PERSON':
                temp_char = ''
                for i in phase.leaves():
                    temp_char += (i[0] + ' ') 
                temp.append(temp_char.strip())
            if phase.label() == 'ORGANIZATION':
                temp_char = ''
                for i in phase.leaves():
                    temp_char += (i[0] + ' ') 
                temp_org.append(temp_char.strip())
    return temp, temp_org

def spacy_NER(text: str, Lang: str):
    temp = []
    temp_org = []
    if Lang == 'E': 
        doc = nlp(text)
        for entity in doc.ents:
            if entity.label_ == 'PERSON':
                temp.append(entity.text)
            if entity.label_ == 'ORG':
                temp_org.append(entity.text)  

    return temp, temp_org

def lac_NER(text: str):
    temp = []
    temp_org = []
    lac = LAC(mode='lac')
    lac = lac.run(text) #Without spacing is better
    for i in range(len(lac[0])):
        if lac[1][i] == 'PER':
            temp.append(lac[0][i])
        if lac[1][i] == 'ORG':
            temp_org.append(lac[0][i])           
    return temp, temp_org

def stanza_NER(text: str, Lang: str):
    temp = []
    temp_org = []

    if Lang == 'E': 
        nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
        doc = nlp(text)
        for ent in doc.ents:
            if ent.type == 'PERSON':
                temp.append(ent.text.strip())
            if ent.type == 'ORG':
                temp_org.append(ent.text.strip())   
            
    if Lang == 'C':     
        nlp = stanza.Pipeline(lang='zh', processors='tokenize,ner')
        doc = nlp(text)
        for ent in doc.ents:
            if ent.type == 'PERSON':
                temp.append(ent.text.strip())
            if ent.type == 'ORG':
                temp_org.append(ent.text.strip())                  

    return temp, temp_org

def hanlp_NER(text: str):
    Output = HanLP(text)
    temp = []
    temp_org = []
    for i in Output['ner/ontonotes']:
        if i[1] == 'PERSON':
            temp.append(i[0])
        if i[1] == 'ORG':
            temp_org.append(i[0])               
    return temp, temp_org

## @brief 
#
# This program returns all people and organization in the given input 'text' (String). \n
# This program utilize three open source NER packages for each language. \n
# The final output is based on voting of the NER packages. 
#
# @param text The input text to perform Named Entity Recogniztion.
# @param rule The number of NER packages required to be agreed on a phase to be classified as a person or organization. \n
# By default, the program will run on flexible selection: runs on rule = 3 first. If returns none, runs on rule = 2 and then 1. \n
#
# @return The program will return 4 sets: English names, Chinese names, English organization, Chinese organization. \n
# The result will be saved at "result.txt" at current directory.
def NER(text: str, rule: int):
    Eng = []
    Chin = []
    nltk_ppl = nltk_org = spacy_ppl = spacy_org = stanza_E_ppl = stanza_E_org =     hanlp_ppl = hanlp_org = lac_ppl = lac_org = stanza_ppl = stanza_org = set()

    English = ' '.join(re.findall(r'[A-Za-z,.:-]+', text)) # Screen out all English 
    if not English == '': 
        nltk_ = NLTK_NER(English)
        nltk_ppl, nltk_org = set(nltk_[0]), set(nltk_[1])
        spacy_E = spacy_NER(English, 'E')
        spacy_ppl, spacy_org = set(spacy_E[0]), set(spacy_E[1])        
        stanza_E_ = stanza_NER(English, 'E')
        stanza_E_ppl, stanza_E_org = set(stanza_E_[0]), set(stanza_E_[1])        

    Chinese = '，'.join(re.findall(r'[，。（）「」·\u4e00-\u9fff]+', text.replace("（",'').replace("）",''))) # Screen out all Chinese. 
    if not Chinese == '': 
        #spacy_C = spacy_NER(Chinese, 'C')
        hanlp_ = hanlp_NER(Chinese)
        hanlp_ppl, hanlp_org = set(hanlp_[0]), set(hanlp_[1])
        lac_ = lac_NER(Chinese)
        lac_ppl, lac_org = set(lac_[0]), set(lac_[1])
        stanza_ = stanza_NER(Chinese, 'C')
        stanza_ppl, stanza_org = set(stanza_[0]), set(stanza_[1])

    if rule == 3:
        return (nltk_ppl&spacy_ppl&stanza_E_ppl if len(nltk_ppl&spacy_ppl&stanza_E_ppl) != 0 else None \
                ,hanlp_ppl&lac_ppl&stanza_ppl if len(hanlp_ppl&lac_ppl&stanza_ppl) != 0 else None \
                ,nltk_org&spacy_org&stanza_E_org if len(nltk_org&spacy_org&stanza_E_org) != 0 else None \
                ,hanlp_org&lac_org&stanza_org if len(hanlp_org&lac_org&stanza_org) != 0 else None)
    elif rule == 2:
        return ((nltk_ppl&spacy_ppl)|(spacy_ppl&stanza_E_ppl)|(stanza_E_ppl&nltk_ppl) if len((nltk_ppl&spacy_ppl)|(spacy_ppl&stanza_E_ppl)|(stanza_E_ppl&nltk_ppl)) != 0 else None \
                ,(hanlp_ppl&lac_ppl)|(lac_ppl&stanza_ppl)|(stanza_ppl&hanlp_ppl) if len((hanlp_ppl&lac_ppl)|(lac_ppl&stanza_ppl)|(stanza_ppl&hanlp_ppl)) != 0 else None \
                ,(nltk_org&spacy_org)|(spacy_org&stanza_E_org)|(stanza_E_org&nltk_org) if len((nltk_org&spacy_org)|(spacy_org&stanza_E_org)|(stanza_E_org&nltk_org)) != 0 else None \
                ,(hanlp_org&lac_org)|(lac_org&stanza_org)|(stanza_org&hanlp_org) if len((hanlp_org&lac_org)|(lac_org&stanza_org)|(stanza_org&hanlp_org)) != 0 else None)
    elif rule == 1:
        return (nltk_ppl|spacy_ppl|stanza_E_ppl if len(nltk_ppl|spacy_ppl|stanza_E_ppl) != 0 else None \
                ,hanlp_ppl|lac_ppl|stanza_ppl if len(hanlp_ppl|lac_ppl|stanza_ppl) != 0 else None \
                ,nltk_org|spacy_org|stanza_E_org if len(nltk_org|spacy_org|stanza_E_org) != 0 else None \
                ,hanlp_org|lac_org|stanza_org if len(hanlp_org|lac_org|stanza_org) != 0 else None)
    
    # Default flexible selection
    output = [None,None,None,None]
    if len(nltk_ppl&spacy_ppl&stanza_E_ppl) != 0:
        output[0] = nltk_ppl&spacy_ppl&stanza_E_ppl
    elif len((nltk_ppl&spacy_ppl)|(spacy_ppl&stanza_E_ppl)|(stanza_E_ppl&nltk_ppl)) != 0:
        output[0] = (nltk_ppl&spacy_ppl)|(spacy_ppl&stanza_E_ppl)|(stanza_E_ppl&nltk_ppl)
    elif 0 < len(nltk_ppl|spacy_ppl|stanza_E_ppl) <= 3: # Not returning noisy output 
        output[0] = nltk_ppl|spacy_ppl|stanza_E_ppl

    if len(hanlp_ppl&lac_ppl&stanza_ppl) != 0:
        output[1] = hanlp_ppl&lac_ppl&stanza_ppl
    elif len((hanlp_ppl&lac_ppl)|(lac_ppl&stanza_ppl)|(stanza_ppl&hanlp_ppl)) != 0:
        output[1] = (hanlp_ppl&lac_ppl)|(lac_ppl&stanza_ppl)|(stanza_ppl&hanlp_ppl)
    elif 0 < len(hanlp_ppl|lac_ppl|stanza_ppl) <= 3:
        output[1] = hanlp_ppl|lac_ppl|stanza_ppl

    if len(nltk_org&spacy_org&stanza_E_org) != 0:
        output[2] = nltk_org&spacy_org&stanza_E_org
    elif len((nltk_org&spacy_org)|(spacy_org&stanza_E_org)|(stanza_E_org&nltk_org)) != 0:
        output[2] = (nltk_org&spacy_org)|(spacy_org&stanza_E_org)|(stanza_E_org&nltk_org)
    elif  0 < len(nltk_org|spacy_org|stanza_E_org) <= 3:
        output[2] = nltk_org|spacy_org|stanza_E_org

    if len(hanlp_org&lac_org&stanza_org) != 0:
        output[3] = hanlp_org&lac_org&stanza_org
    elif len((hanlp_org&lac_org)|(lac_org&stanza_org)|(stanza_org&hanlp_org)) != 0:
        output[3] = (hanlp_org&lac_org)|(lac_org&stanza_org)|(stanza_org&hanlp_org)
    elif 0 < len(hanlp_org|lac_org|stanza_org) <= 3: 
        output[3] = hanlp_org|lac_org|stanza_org
        
    return output[0], output[1], output[2], output[3]    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        rule = 0
    else:
        if sys.argv[2] not in {1, 2, 3}:
            print(len(sys.argv))
            print(sys.argv[2])
            raise ValueError("Rule must be 1, 2, or 3. Ignore this argument if you wish to use flexible mode.")
        rule = sys.argv[2]
    print("loading results")
    #file_paths = str(sys.argv[1]).split(", ")
    result = []
    #for path in file_paths:
    #    result.append(NER(dataloader(path), rule))
    result.append(NER(sys.argv[1], rule))
    with open("./result.txt", "w", encoding="utf8") as f:
        for i in result:
            f.write(str(i)+"\n")
    print("Done")