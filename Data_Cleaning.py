import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/realpython/python-data-cleaning/master/Datasets/BL-Flickr-Images-Book.csv")
to_drop = ["Edition Statement", "Corporate Author", "Corporate Contributors",
           "Former owner", "Engraver", "Contributors", "Issuance type", "Shelfmarks"]
df.drop(to_drop, inplace= True, axis=1)
# df.drop(columns= to_drop, inplace= True)
# print (df["Identifier"].is_unique)
df = df.set_index("Identifier")
regex = r'^(\d{4})'
extr = df["Date of Publication"].str.extract(regex, expand = False)
# print (extr.head(n=5))
# print (extr.loc[206])
df["Date of Publication"] = pd.to_numeric(extr)
# print (df["Date of Publication"].dtype)
pub = df["Place of Publication"]
london = pub.str.contains("London")
oxford = pub.str.contains("Oxford")
# print (london[:])
df["Place of Publication"] = np.where(london, "London",
                                      np.where(oxford, "Oxford",
                                               pub.str.replace("-", "")))
# print (df.head(n = 5))

