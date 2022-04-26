import random
from transformers import pipeline
import pandas as pd

candidates = ["size","weight", "cup height","pump pressure", "water tank", "power"]
classifier = pipeline("zero-shot-classification")
print("After pipeline")

def featureClassifier(text):
    print("Evaluating:", text)
    results = classifier(text, candidate_labels=candidates)
    size_text = []
    weight_text = []
    cup_text = []
    pump_text = []
    water_text = []
    power_text = []
    for result in results:
        print(result)
        max_value = max(result["scores"])
        max_index = result['scores'].index(max_value)
        if result['labels'][max_index] == 'size':
            size_text.append(result['sequence'])
        elif result['labels'][max_index] == 'weight':
            weight_text.append(result['sequence'])
        elif result['labels'][max_index] == 'cup height':
            cup_text.append(result['sequence'])
        elif result['labels'][max_index] == 'pump pressure':
            pump_text.append(result['sequence'])
        elif result['labels'][max_index] == 'water tank':
            water_text.append(result['sequence'])
        elif result['labels'][max_index] == 'power':
            power_text.append(result['sequence'])
        return size_text, weight_text, cup_text, pump_text, water_text, power_text, results