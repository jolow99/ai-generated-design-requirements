import pandas as pd

clean_comments = pd.read_pickle("clean_comments.pkl")
raw_comments = pd.read_pickle("raw_comments.pkl")

from pprint import pprint as pprint 

# convert list of lists to dataframe
clean_comments_df = pd.DataFrame(clean_comments)
raw_comments_df = pd.DataFrame(raw_comments)

# output clean comments dataframe to csv file 
clean_comments_df.to_csv("clean_comments.csv")

# output raw comments dataframe to csv file 
raw_comments_df.to_csv("raw_comments.csv")
