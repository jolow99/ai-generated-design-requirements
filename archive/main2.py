import pandas as pd 
import time
# from utilities.sentiment import usabilitySentiment
from utilities.sentiment2 import specificationSentiment

# List of usable products
products = [
    "Delonghi Dedica",
    "Delonghi Dinamica",
    "Delonghi Eletta",
    "Delonghi Icona",
    "Delonghi La Specialista",
    "Delonghi Lattissima",
    "Delonghi Magnifica",
    "Delonghi Perfecta",
    "Delonghi Prima Donna",
]
    # "Delonghi Stilosa",
features = ["size","weight", "cup height","pump pressure", "water tank", "power"]

start= time.time()
data = {}
countdown = len(products)

# Step C1: Read CSV Files of all comments
for product in products:
    df = pd.read_csv(f"youtube/support/{product}/clean_comments.csv")
    df = df.iloc[:, 1:]
    df = df.dropna(how='all')

    # convert df to list by merging the list of lists into one list if item is not nan. 
    comments = df.values.tolist()
    comments = [item for sublist in comments for item in sublist if not isinstance(item, float)]

    data[product] = comments

keywords = {
    "Volume (m^3)": ["size", "dimensions", "volume"],
    "Weight (Kg)" : ["heavy","bulky", "move", "clunky", "light"],
    "Maximum cup height (mm)": ["cup height", "glass", "fits"],
    "Pump pressure (bar)": ["pump", "pressure", "bars","rotary","vibratory"],
    "Water tank capacity (l)": ["reservoir","tank", "capacity"],
    "Input power (W)": ["power", "electricity", "wattage", "watts", "energy","rating"]
}

# Step C2: Categorise comments relating to each individual feature 
product_all_comments = data
product_feature_comments = {}
for product, comments in product_all_comments.items():
    print(f"Currently on {product}, Remaining: {countdown}")
    feature_comments = {
    "Volume (m^3)": [],
    "Weight (Kg)" : [],
    "Maximum cup height (mm)": [],
    "Pump pressure (bar)": [],
    "Water tank capacity (l)": [],
    "Input power (W)": []
}
    for comment in comments: 
        if isinstance(comment, bool):
            continue
        for feature, words in keywords.items():
            for word in words:
                if isinstance(word, bool):
                     continue
                if word in comment.lower():
                    feature_comments[feature].append(comment)
                    break
    product_feature_comments[product] = feature_comments
    countdown -= 1

print("Step C2 done")
for product, features in product_feature_comments.items():
    for feature, comments in features.items():
        print(f"{product} {feature} has {len(comments)} comments")

# Save results into csv
df = pd.DataFrame.from_dict(product_feature_comments)
df.to_csv(f"youtube/support/product_feature_comments.csv")

# Step C3: Run sentiment analysis on each product's feature comments
product_feature_sentiment = {}
countdown = len(products)
for product, features in product_feature_comments.items():
    print(f"Currently on {product}, Remaining: {countdown}")
    feature_sentiment = {
        "size": 0,
        "weight" : 0,
        "cup": 0,
        "pump": 0,
        "water": 0,
        "power": 0
    }
    for feature, comments in features.items():
        print(f"Currently on {feature}, and analysing {len(comments)} comments")
        average, result = specificationSentiment(comments)
        feature_sentiment[feature] = average
    product_feature_sentiment[product] = feature_sentiment
    countdown -= 1
    
# Save results into csv
df = pd.DataFrame.from_dict(product_feature_sentiment)
df.to_csv(f"youtube/support/product_feature_sentiment.csv")
