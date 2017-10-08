import pandas as pd
filename ='/Users/Dhanush/Desktop/Projects/GreenSO/Data/posts.csv'

chunksize = 10 ** 6
for chunk in pd.read_csv(filename, chunksize=chunksize):
    print chunk
    break