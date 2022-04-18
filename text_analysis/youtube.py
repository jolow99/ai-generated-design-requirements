import pandas as pd

data = {'Delonghi All-In-One Combination coffee maker': -0.2, 'Delonghi Stilosa': 0.3333333333333333, 'Delonghi La Specialista': -0.3333333333333333, 'Delonghi Magnifica': 0.0, 'Delonghi Dinamica': -0.5, 'Delonghi Eletta': 0.2, 'Delonghi Prima Donna': -1.0, 'Delonghi Dedica': 0.2, 'Delonghi Lattissima': 0.5, 'Delonghi VertuoNext': 0.6, 'Delonghi Maestosa': 0.2, 'Delonghi Perfecta': -0.6, 'Delonghi Clessidra': 0.2}
df = pd.DataFrame.from_dict(data,orient="index", columns=["score"])
df.to_csv("testing.csv")

# clean_comments = pd.read_pickle("clean_comments.pkl")
# raw_comments = pd.read_pickle("raw_comments.pkl")

# from pprint import pprint as pprint 

# # convert list of lists to dataframe
# clean_comments_df = pd.DataFrame(clean_comments)
# raw_comments_df = pd.DataFrame(raw_comments)

# # output clean comments dataframe to csv file 
# clean_comments_df.to_csv("clean_comments.csv")

# # output raw comments dataframe to csv file 
# raw_comments_df.to_csv("raw_comments.csv")
