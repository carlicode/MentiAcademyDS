import pandas as pd

data = pd.read_csv('cleanData.csv')
data.to_excel('cleanData.xlsx', index=False)
