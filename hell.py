import pandas as pd 

#Basic day granularity of .csv file (day)

dfg = pd.read_csv('Henry_Hub_Natural_Gas_Spot_Price.csv', skiprows=4)
dfg.index = pd.to_datetime(dfg["Day"],format='%m/%d/%Y')
dfg.to_csv('gas-details_day.csv', index=False) 

#Other granularities and sections of the .csv file (month)

dfg_month = dfg['Henry Hub Natural Gas Spot Price Dollars per Million Btu'].resample('M').sum()
df = pd.DataFrame(dfg_month, index=dfg_month.index.strftime("%m"))
df.to_csv('gas-details_month.csv', index=True)

#Other granularities and sections of the .csv file (year)
dfg_year = dfg['Henry Hub Natural Gas Spot Price Dollars per Million Btu'].resample('Y').sum()
df = pd.DataFrame(dfg_year, index=dfg_year.index.strftime("%Y"))
df.to_csv('gas-details_year.csv', index=True)

print("Exctracted Succesfully")