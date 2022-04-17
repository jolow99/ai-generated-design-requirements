import random
from transformers import pipeline

candidates = ["usable", "not usable"]
classifier = pipeline("zero-shot-classification")
print("After pipeline")

def getUsabilityComments(comments):
    print("Evaluating:", comments)
    results = classifier(comments, candidate_labels=candidates)
    usability_comments = []
    for result in results:
        max_value = max(result["scores"])
        max_index = result['scores'].index(max_value)
        if result['labels'][max_index] == 'usable':
            usability_comments.append(result['sequence']) 
    return usability_comments