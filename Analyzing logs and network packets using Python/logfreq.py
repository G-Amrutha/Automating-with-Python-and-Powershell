import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import interactive
interactive(True)


df_raw=pd.read_csv('appevent.csv',encoding="ISO-8859-1",skiprows=1)

#show column names in the log file
for col in df_raw.columns:
      print(col)

#extract two timestamps from the log file 
df_date=df_raw[['TimeGenerated','TimeWritten']]
print(df_date.head(5))

#convert TimeGenerated from object dtype to DateTime dtype
ts1=pd.to_datetime(df_date['TimeGenerated'], format='%m/%d/%Y %I:%M:%S %p')
df_ts1=pd.DataFrame(
      { "TimeGenerated": ts1 }
      )
print(df_ts1.head(5))

#generate a frequency table that is grouped the log entries by month in TimeGenerated
df_grp=df_ts1.groupby(pd.Grouper(key='TimeGenerated',freq='M')).TimeGenerated.count()
df_grp.plot()









