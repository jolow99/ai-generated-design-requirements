from transformers import pipeline

print("Setting up")
classifier = pipeline('sentiment-analysis')
print("Done")

def usabilitySentiment(text):
    results = classifier(text)
    if results == None or results == []:
        return None, None
    print("Results: ", results)
    # Take the average score. If label is 'NEGATIVE', score should be negative.
    # If label is 'POSITIVE', score should be positive.
    # If label is 'NEUTRAL', score should be 0.
    print("Results len", len(results))
    n = len(text)
    print("n", n)
    sum = 0
    for result in results:
        print(result)
        if result['label'] == 'POSITIVE':
            sum += 1
        elif result['label'] == 'NEGATIVE':
            sum -= 1
        else: 
            print(result) # Should not happen
    average = sum / n
    print(average)
    return average, results
