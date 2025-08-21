import pandas as pd

s1 = pd.Series([1,3,5,7,9])
# print(s1)

s2 = pd.Series([10,20,30,40],index=["a","b","c","d"])
# s2 = pd.Series([10,20,30,40])

# print(s2)

# fruits = {"apple":3,"kiwi":2,"banana":5}

# seriesFruits = pd.Series(fruits)
# print(seriesFruits)

# print(s1*2)
# print(s1+s2)

# boolean
# print(s2[s2>15])
# print(s2['a'])

# dataframe
data = {
    "Name":["xyz","abc","def"],
    "age":[20,30,32],
    "city":["CBE","Salem","Erode"]
}

df = pd.DataFrame(data)
# df = pd.DataFrame(data,index=["first","second","third"])
# print(df)

# print(df.head(2))
# print(df.tail(1))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

df['email'] = ["abc@gmail.com","xyz@gmail.com","def@gmail.com"]

# print(df)

# print(df.loc['first'])

# print(df.loc[0,2,'Name'])
# print(df.loc[0:2,"Name"])
# print(df.loc[0])
print(df.iloc[0:2,0:2])

df.to_csv("out.csv" ,index=True)
# df.to_csv("output.csv" ,index=False)