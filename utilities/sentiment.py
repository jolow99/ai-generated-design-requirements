from transformers import pipeline

print("Setting up")
classifier = pipeline('sentiment-analysis')
print("Done")

def averageSentiment(text):
    reduced_text = []
    for word in text: 
        if len(word) > 512:
            reduced_text.append(word[:512])
        else:
            reduced_text.append(word)
    results = classifier(reduced_text)
    sum = 0
    for result in results:
        if result['label'] == 'POSITIVE':
            sum += 1
        elif result['label'] == 'NEGATIVE':
                sum -= 1
        else: 
            print("Error")
            print(result) # Should not happen

    if len(results) == 0:
        return None, None
    average = sum / len(results)
    print("Average:", average)
    print("All Results", results)
    return average, results