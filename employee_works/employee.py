import pandas as pd

data = pd.read_csv("C:/Users/hp/Desktop/EDA/employee_works/sample (1).csv")
# read the data from the csv file

df = pd.DataFrame(data)
# convert into data structure

print(df)

print(df.describe())