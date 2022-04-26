import pandas as pd 
import time
from utilities.usability import usabilityClassifier
from utilities.sentiment import averageSentiment

#     "Delonghi Maestosa" removed due to insufficient videos on youtube

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

start= time.time()
data = {}
countdown = len(products)

# Step A: For each search term, get all youtube comments of top 5 videos by running code 1 and code 2, then using the clean_comments csv file

# Step B1: Read CSV Files
for product in products:
    df = pd.read_csv(f"youtube/support/{product}/clean_comments.csv")
    df = df.iloc[:, 1:]
    df = df.dropna(how="all")

    # convert df to list by merging the list of lists into one list if item is not nan. 
    comments = df.values.tolist()
    all_comments = []
    for sublist in comments:
        for item in sublist:
            if isinstance(item,str):
                all_comments.append(item)

    data[product] = all_comments

# # Step B2: Drop comments which are not related to usability
product_all_comments = data
product_usability_comments = {}
for product, product_comments in product_all_comments.items():
    print(f"Currently on {product}, Remaining: {countdown}")
    usability_comments, results = usabilityClassifier(product_comments)
    product_usability_comments[product] = usability_comments
    countdown -= 1

    # Save results into csv 
    df = pd.DataFrame.from_dict(results)
    df.to_csv(f"youtube/support/{product}/usability_comments.csv")


# Step B3: For each usability comment in each search term, rate the comment by running sentiment analysis
product_usability_score = {}
countdown = len(products)
for product, comments in product_usability_comments.items():
    print(f"Currently on {product}, Remaining: {countdown}")
    print(" ")
    score, results = averageSentiment(comments)
    product_usability_score[product] = score
    countdown -= 1
    # Save results into csv 
    df = pd.DataFrame.from_dict(results)
    df.to_csv(f"youtube/support/{product}/usability_sentiment.csv")

print(product_usability_score)
end = time.time()
print("time taken", end-start)

# Save final product_usability_score into csv
df = pd.DataFrame.from_dict(product_usability_score, orient="index", columns=["score"])
df.to_csv("youtube/support/product_usability_score.csv")
