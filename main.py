import pandas as pd 
import time
from utilities.usability import usabilityClassifier
from utilities.sentiment import usabilitySentiment


products = [
    "Delonghi All-In-One Combination coffee maker", 
    "Delonghi Clessidra", 
    "Delonghi Dedica",
    "Delonghi Dinamica",
    "Delonghi Eletta",
    "Delonghi Icona",
    "Delonghi La Specialista",
    "Delonghi Lattissima",
    "Delonghi Maestosa",
    "Delonghi Magnifica",
    "Delonghi Perfecta",
    "Delonghi Prima Donna",
    "Delonghi Stilosa",
    "Delonghi Vertuo Next"
    ]

start= time.time()
data = {}
countdown = len(products)

# Step A: For each search term, get all youtube comments of top 5 videos by running code 1 and code 2, then using the clean_comments csv file

# Step B1: Read CSV Files
for product in products:
    df = pd.read_csv(f"youtube/support/{product}/clean_comments.csv")
    df = df.iloc[:, 1:]
    df = df.dropna(how='all')

    # convert df to list by merging the list of lists into one list if item is not nan. 
    comments = df.values.tolist()
    comments = [item for sublist in comments for item in sublist if not isinstance(item, float)]

    data[product] = comments

# Step B2: Drop comments which are not related to usability
product_all_comments = data
product_usability_comments = {}
for product, comments in product_all_comments.items():
    print("Remaining: ", countdown)
    usability_comments, results = usabilityClassifier(comments[:5])
    product_usability_comments[product] = usability_comments
    countdown -= 1

    # Save results into csv 
    df = pd.DataFrame.from_dict(results)
    df.to_csv(f"youtube/support/{product}/usability_comments.csv")


# Step B3: For each usability comment in each search term, rate the comment by running sentiment analysis
product_usability_score = {}
for product, comments in product_usability_comments.items():
    score, results = usabilitySentiment(comments)
    product_usability_score[product] = score
    # Save results into csv 
    df = pd.DataFrame.from_dict(results)
    df.to_csv(f"youtube/support/{product}/usability_sentiment.csv")

print(product_usability_score)
end = time.time()
print("time taken", end-start)

# Save final product_usability_score into csv
df = pd.DataFrame.from_dict(product_usability_score, orient="index", columns=["score"])
df.to_csv("youtube/support/product_usability_score.csv")

# Step C: Plot n-dimensional graph surface thingy to find the optimum feature combination and we're done! 



# {'Delonghi All-In-One Combination coffee maker': -0.2, 
# 'Delonghi Stilosa': 0.3333333333333333, 
# 'Delonghi La Specialista': -0.3333333333333333, 
# 'Delonghi Magnifica': 0.0, 
# 'Delonghi Dinamica': -0.5, 
# 'Delonghi Eletta': 0.2, 
# 'Delonghi Prima Donna': -1.0, 
# 'Delonghi Dedica': 0.2, 
# 'Delonghi Lattissima': 0.5, 
# 'Delonghi VertuoNext': 0.6, 
# 'Delonghi Maestosa': 0.2, 
# 'Delonghi Perfecta': -0.6, 
# 'Delonghi Clessidra': 0.2}