import pandas as pd 
import time
from usability import getUsabilityComments
from sentiment import getUsabilitySentiment

def main():
    brand = "Delonghi "
    series = ["All-In-One Combination coffee maker", "Stilosa", "La Specialista", 'Magnifica', "Dinamica", "Eletta", "Prima Donna", "Dedica","Icona", "Lattissima", "VertuoNext", "Maestosa", "Perfecta", "Clessidra"]
    search_terms = [brand + s for s in series]

    start= time.time()
    data = {}
    countdown = len(search_terms)

    # Step A: Get amazon reviews if each delonghi product line

    # Step B1: Read CSV Files
    for product in search_terms:
        if product == "Delonghi Maestosa":
            continue
        print("Product:", product)
        df = pd.read_csv(f"text_analysis/{product}/reviews.csv")
        # convert df to list by merging the list of lists into one list if item is not nan. 
        reviews = df["Review Description"].tolist()
        data[product] = reviews

    # Step B2: Drop comments which are not related to usability
    product_all_reviews = data
    product_usability_reviews = {}
    for product, reviews in product_all_reviews.items():
        print("Remaining: ", countdown)
        print("Product:", product)
        usability_reviews, results = getUsabilityComments(reviews[:10])
        product_usability_reviews[product] = usability_reviews
        countdown -= 1

        # Save results into csv 
        df = pd.DataFrame.from_dict(results)
        df.to_csv(f"text_analysis/{product}/usability_reviews.csv")


    # Step B3: For each usability comment in each search term, rate the comment by running sentiment analysis
    product_usability_score = {}
    for product, reviews in product_usability_reviews.items():
        print("Product:", product)
        score, results = getUsabilitySentiment(reviews)
        product_usability_score[product] = score
        # Save results into csv 
        df = pd.DataFrame.from_dict(results)
        df.to_csv(f"text_analysis/{product}/review_usability_sentiment.csv")

    print(product_usability_score)
    end = time.time()
    print("time taken", end-start)

    # Save final product_usability_score into csv
    df = pd.DataFrame.from_dict(product_usability_score, orient="index", columns=["score"])
    df.to_csv("text_analysis/product_usability_review_score.csv")

    # # Step C: Plot n-dimensional graph surface thingy to find the optimum feature combination and we're done! 




    # # {'Delonghi All-In-One Combination coffee maker': -0.2, 
    # # 'Delonghi Stilosa': 0.3333333333333333, 
    # # 'Delonghi La Specialista': -0.3333333333333333, 
    # # 'Delonghi Magnifica': 0.0, 
    # # 'Delonghi Dinamica': -0.5, 
    # # 'Delonghi Eletta': 0.2, 
    # # 'Delonghi Prima Donna': -1.0, 
    # # 'Delonghi Dedica': 0.2, 
    # # 'Delonghi Lattissima': 0.5, 
    # # 'Delonghi VertuoNext': 0.6, 
    # # 'Delonghi Maestosa': 0.2, 
    # # 'Delonghi Perfecta': -0.6, 
    # # 'Delonghi Clessidra': 0.2}

if __name__ == "__main__":
    main()