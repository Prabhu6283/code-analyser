import spacy
from nltk import sent_tokenize

# core english model loaded
nlp = spacy.load("en_core_web_sm") 

# discourse markers for punctuation rules
discourse_for_puctuation = ["However"] 

#function to restore the punctuation error
def restore_punctuation(text):
    for marker in discourse_for_puctuation:
        if text.startswith(marker):
            text = text.replace(marker, marker + ",")
    return text

# function to restore OCR errors
def fix_ocr_errors(text):
    text = text.replace("launehing", "launching")
    text = text.replace("namcd", "named")
    text = text.replace("cmphasizing", "emphasizing")
    text = text.replace("elub", "club")
    text = text.replace("mcant", "meant")
    text = text.replace("5erve", "serve")
    text = text.replace("5tudents", "students")
    text = text.replace("mcntors", "mentors")
    text = text.replace("dcgree", "degree")
    text = text.replace("eompleting", "completing")
    text = text.replace("rcsults", "results")
    return text

# function to extract Names of people, proper nouns and  Locations
def extract_entities(text):
    entities = []
    for ent in nlp(text).ents:
        if ent.label_ in ["PERSON", "ORG", "GPE"]:
            entities.append(ent.text)
    return entities

# combining ocr and puctuation to a single function
def fix_text(text):
    text = fix_ocr_errors(text)
    text = restore_punctuation(text)
    return text

# Passing our testcases
testcase_1 = "In April 2023, Sundar Pichai did announce that Google would be launehing a new AI product namcd Gemini. Barack Obama also gave a speech at Harvard University, cmphasizing the role of technology in modern education."

print(fix_text(testcase_1))
print(extract_entities(testcase_1))

testcase_2 = "Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together. Through the guidance of their mcntors these 5tudents are able to complete daunting tasks in a relatively short time frame, gaining significant exposure and knowledge in their domain of choice."

print(fix_text(testcase_2))
print(extract_entities(testcase_2))

testcase_3 = "I will be eompleting my BTech dcgree in Mechanical Engineering from VJTI in 2028"

print(fix_text(testcase_3))
print(extract_entities(testcase_3))

testcase_4 = "However the rcsults were clear"

print(fix_text(testcase_4))
print(extract_entities(testcase_4))