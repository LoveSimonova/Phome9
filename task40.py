import pandas as pd

df = pd.read_csv('california_housing_train.csv')
count=df[df['population']<=500].shape[0]
print(count)
val=int(df[df['population']<=500]['median_house_value'].sum())
print(val/count)