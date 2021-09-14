import pandas as pd
import numpy as np

#! Source of Data https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv")

# * candy-data.csv includes attributes for each candy along with its ranking. For binary variables, 1 means yes, 0 means no.
# * There are 13 different attributes in the dataset

# * The Class of this dataset is the different kind of candy bars
# * chocolate | Does it contain chocolate?
# * fruity | Is it fruit flavored?
# * caramel | Is there caramel in the candy?
# * peanutalmondy | Does it contain peanuts, peanut butter or almonds?
# * nougat | Does it contain nougat?
# * crispedricewafer | Does it contain crisped rice, wafers, or a cookie component?
# * hard | Is it a hard candy?
# * bar | Is it a candy bar?
# * pluribus | Is it one of many candies in a bag or box?
# * sugarpercent | The percentile of sugar it falls under within the data set.
# * pricepercent | The unit price percentile compared to the rest of the set.
# * winpercent | The overall win percentage according to 269,000 matchups.

print('Number of instances = %d' % (df.shape[0]))
print('Number of attributes = %d' % (df.shape[1]))

print(df.head())

for col in df.columns:
    print(f"{col}: {df[col].isna().sum()}")