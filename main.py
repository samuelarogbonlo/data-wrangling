import pandas as pd 

#Basic granularity of .csv file (day)

dfg = pd.read_csv('Henry_Hub_Natural_Gas_Spot_Price.csv',
                 index_col='Day',parse_dates=True,infer_datetime_format=False,skiprows=4)
dfg.sort_index(inplace=True)
dfg.to_csv('gas-details_day.csv', index=True) 

#Other granularities and sections of the .csv file (month)
dfg_month = dfg['Henry Hub Natural Gas Spot Price Dollars per Million Btu'].resample('M').sum()
df = pd.DataFrame(dfg_month, index=dfg_month.index.strftime("%m"))
df.to_csv('gas-details_month.csv', index=True) 


#Other granularities and sections of the .csv file (year)
dfg_year = dfg['Henry Hub Natural Gas Spot Price Dollars per Million Btu'].resample('Y').sum()
df = pd.DataFrame(dfg_year, index=dfg_year.index.strftime("%Y"))
df.to_csv('gas-details_year.csv', index=True)

print("Exctracted Succesfully")