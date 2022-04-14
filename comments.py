import random


# Step A1: Search for top 5 videos using each term, and save all the comments from each video
search_terms = [
    "Delonghi All-In-One Combination coffee maker",
    "Delonghi Stilosa",
    "Delonghi La Specialista",
    "Delonghi Magnifica",
    "Delonghi Dinamica",
    "Delonghi Eletta",
    "Delonghi Prima Donna",
    "Delonghi Dedica",
    "Delonghi Lattissima",
    "Delonghi VertuoNext",
    "Delonghi Maestosa",
    "Delonghi Perfecta",
    "Delonghi Clessidra",
]

# Step A2: For each comment in each search term, flag out comments related to usability
product_all_comments = {
    "Delonghi All-In-One Combination coffee maker": [
        "Usability is great",
        "flimsy cheap-ass product",
        "easy to use coffee maker",
    ],
    "Delonghi Stilosa": [
        "easy to use",
        "difficult to refill the water tank",
        "value for money product",
        "coffee tastes great",
    ],
}


def isUsabilityRelated(comment):
    return random.choice([True, False])


product_usability_comments = {}

for product, comments in product_all_comments.items():
    usability_comments = []
    for comment in comments:
        if isUsabilityRelated(comment):
            usability_comments.append(comment)
    product_usability_comments[product] = usability_comments


# Step A3: For each usability comment in each search term, rate the comment by running sentiment analysis
# product_usability_comments = {
#     "Delonghi All-In-One Combination coffee maker": ["Usability is great", "flimsy cheap-ass product", "easy to use coffee maker"],
#     "Delonghi Stilosa": ["easy to use", "difficult to refill the water tank"]}


def usabilitySentiment(comment):
    return random.randint(-5, 5)


product_usability_comments_sentiments = {}
for product, comments in product_usability_comments.items():
    usability_comments = []
    for comment in comments:
        comment_sentiment = [comment, usabilitySentiment(comment)]
        usability_comments.append(comment_sentiment)
    product_usability_comments_sentiments[product] = usability_comments

# Step A4: Rate every product based on how usable it is
# product_usability_comments_sentiments = {
#     "Delonghi All-In-One Combination coffee maker": [["Usability is great",5], ["flimsy cheap-ass product",-4], ["easy to use coffee maker",3]],
#     "Delonghi Stilosa": [["easy to use",1] , ["difficult to refill the water tank",-3]],
#     }

product_usability_score = {}
for product, comments in product_usability_comments_sentiments.items():
    usability_score = 0
    for comment in comments:
        usability_score += comment[1]
    product_usability_score[product] = usability_score

# Final Output
# product_usability_score = {
#     "Delonghi All-In-One Combination coffee maker": 4,
#     "Delonghi Stilosa": -2
#     }
from pprint import pprint as pprint

print(
    "Step A1: Search for top 5 videos using each term, and save all the comments from each video"
)
pprint(f"Input: {search_terms}")
pprint(f"Output: {product_all_comments}")
print(" ")

print(
    "Step A2: For each comment in each search term, flag out comments related to usability"
)
pprint(f"Input: {product_all_comments}")
pprint(f"Output: {product_usability_comments}")
print(" ")

print(
    "Step A3: For each usability comment in each search term, rate the comment by running sentiment analysis"
)
pprint(f"Input: {product_usability_comments}")
pprint(f"Output: {product_usability_comments_sentiments}")
print(" ")

print("Step A4: Rate every product based on how usable it is")
pprint(f"Input: {product_usability_comments_sentiments}")
pprint(f"Output: {product_usability_score}")
print(" ")

# Step B1: Create a list of product with score above x (e.g. -5)
usable_products = []
for product, score in product_usability_score.items():
    if score > -5:
        usable_products.append(product)

# Step B2: Get commments of the usable products
usable_products_comments = {}
for product, comments in product_all_comments.items():
    if product in usable_products:
        usable_products_comments[product] = comments

# Step B3: Categorise each comment of the usable products into features
candidates = [
    "Dimensions",
    "Weight",
    "Rated voltage/Frequency",
    "Maximum cup height",
    "Pump pressure",
    "Water tank capacity",
    "Input power",
    "Beans container capacity",
    "Grounds container capacity",
    "Energy class",
    "Milk carafe capacity",
    "Used capsule container",
    "Cups",
]

def candidateClassifier(comment):
    return random.choice(candidates)  

comments_categorised_by_features = {}
for product, comments in usable_products_comments.items():
    comments_categorised_by_features[product] = {}
    for feature in candidates:
        comments_categorised_by_features[product][feature] = []
    for comment in comments:
        feature = candidateClassifier(comment)
        comments_categorised_by_features[product][feature].append(comment)

print(comments_categorised_by_features)

# Step B4 Run sentiment analysis on each comment in each feature and output a dictionary of features and the product with the maximum sentiment score
def featureSentiment(comments):
    return random.randint(-5, 5)

feature_sentiment = {}
max_sentiment_score = None
for product, features in comments_categorised_by_features.items():
    for features, comments in features.items():
        sentiment_score = 0
        for comment in comments:
            sentiment_score += featureSentiment(comment)
        if max_sentiment_score is None:
            max_sentiment_score = sentiment_score
        elif sentiment_score > max_sentiment_score:
            max_sentiment_score = sentiment_score
            feature_sentiment[feature] = product 

# Step B5 Output design requirements, using the same specifications of product with the maximum sentiment score in each feature
inp_example = {
    "Feature1": "Product 1", 
    "Feature2": "Product 2",
    "Feature3": "Product 2",
    "Feature4": "Product 1",
}

out_example = {
    "Feature1": "Product 1's feature1",
    "Feature2": "Product 2's feature2", 
    "Feature3": "Product 2's feature3",
    "Feature4": "Product 1's feature4",
}

    