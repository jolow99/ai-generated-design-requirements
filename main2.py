import pandas as pd 
from usability import getUsabilityComments
from sentiment import getUsabilitySentiment

brand = "Delonghi "
series = ["All-In-One Combination coffee maker", "Stilosa", "La Specialista", 'Magnifica', "Dinamica", "Eletta", "Prima Donna", "Dedica", "Lattissima", "VertuoNext", "Maestosa", "Perfecta", "Clessidra"]
search_terms = [brand + s for s in series]

data = {}

# Step A: For each search term, get the usability comments by running code 1 and code 2, then using the clean_comments csv file

# Step B1: Read CSV Files
for product in search_terms:
    df = pd.read_csv(f"text_analysis/{product}/clean_comments.csv")
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
    usability_comments = getUsabilityComments(comments)
    product_usability_comments[product] = usability_comments

# Step B3: For each usability comment in each search term, rate the comment by running sentiment analysis
product_usability_score = {}
for product, comments in product_usability_comments.items():
    score = getUsabilitySentiment(comments[0:5])
    product_usability_score[product] = score

print(product_usability_score)
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

# Step C: Plot n-dimensional graph surface thingy to find the optimum feature combination and we're done! 