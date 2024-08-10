import pandas as pd

df_raw=pd.read_csv('appevent.csv',encoding="ISO-8859-1",skiprows=1)
print(df_raw.tail(1))
for col in df_raw.columns:
      print(col)

print("\n")
#df1=df_raw.tail(100)
#show source of events

print(df_raw['Source'].value_counts(),"\n")







