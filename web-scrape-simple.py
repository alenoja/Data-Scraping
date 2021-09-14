
import pandas as pd

tables = pd.read_html('https://en.wikipedia.org/wiki/Radiohead')

df1 = tables[0]
print('First Table')
print(df1.head())