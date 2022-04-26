import random
from transformers import pipeline
import pandas as pd

candidates = ["usability", "not usability", "video"]
classifier = pipeline("zero-shot-classification")
print("After pipeline")

def usabilityClassifier(text):
    print("Evaluating:", text)
    results = classifier(text, candidate_labels=candidates)
    usability_text = []
    for result in results:
        print(result)
        max_value = max(result["scores"])
        max_index = result['scores'].index(max_value)
        if result['labels'][max_index] == 'usability':
            usability_text.append(result['sequence']) 

    return usability_text, results