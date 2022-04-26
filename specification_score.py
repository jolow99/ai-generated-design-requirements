import pandas as pd 
import time
from utilities.sentiment import averageSentiment

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
    "Delonghi Stilosa",
    ]
features = ["size","weight", "cup height","pump pressure", "water tank", "power"]

start= time.time()
data = {}
countdown = len(products)

# Step C1: Read CSV Files of all comments
for product in products:
    df = pd.read_csv(f"youtube/support/{product}/clean_comments.csv")
    df = df.iloc[:, 1:]
    # df = df.dropna(how='all')

    # convert df to list by merging the list of lists into one list if item is not nan. 
    comments = df.values.tolist()
    comments = [item for sublist in comments for item in sublist if not isinstance(item, float)]

    data[product] = comments

keywords = {
    "Volume (m^3)": ["volume", "dimensions","size"],
    "Weight (Kg)" : ["heavy","bulky", "move", "shift", "clunky", "light"],
    "Maximum cup height (mm)": ["cup", "glass", "fits", "tall"],
    "Pump pressure (bar)": ["pump", "pressure", "bars","rotary","vibratory", "force"],
    "Water tank capacity (l)": ["water", "tank", "capacity", "litres", "refill"],
    "Input power (W)": ["power", "electricity", "wattage", "watts", "energy","rating","draw","current"]
}

# Step C2: Categorise comments relating to each individual feature 
product_all_comments = data
product_feature_comments = {}
for product, comments in product_all_comments.items():
    print(f"Currently on {product}, Remaining: {countdown} products")
    print(f"Analysing a total of {len(comments)} comments")
    feature_comments = {
    "Volume (m^3)": [],
    "Weight (Kg)" : [],
    "Maximum cup height (mm)": [],
    "Pump pressure (bar)": [],
    "Water tank capacity (l)": [],
    "Input power (W)": []
}

    for comment in comments: 
        feature_score = {
            "Volume (m^3)": 0,
            "Weight (Kg)" : 0,
            "Maximum cup height (mm)": 0,
            "Pump pressure (bar)": 0,
            "Water tank capacity (l)": 0,
            "Input power (W)": 0
        }
        if isinstance(comment, bool):
            continue
        for feature, words in keywords.items():
            for word in words:
                if word in comment.lower():
                    feature_score[feature] += 1
        # Get the key of the maximum feature_score
        max_feature = max(feature_score, key=feature_score.get)
        for feature, score in feature_score.items():
            if score > 0:
                feature_comments[feature].append(comment)
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
        "Volume (m^3)": 0,
        "Weight (Kg)" : 0,
        "Maximum cup height (mm)": 0,
        "Pump pressure (bar)": 0,
        "Water tank capacity (l)": 0,
        "Input power (W)": 0
    }
    for feature, comments in features.items():
        print(f"Analysing {feature} which has {len(comments)} comments")
        average, result = averageSentiment(comments)
        feature_sentiment[feature] = average
    product_feature_sentiment[product] = feature_sentiment
    countdown -= 1
    
# Save results into csv
df = pd.DataFrame.from_dict(product_feature_sentiment)
df.to_csv(f"youtube/support/product_feature_sentiment.csv")
