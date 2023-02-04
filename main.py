#crypto hopper - take csv feed and weed out cryptos that tripped between a certain number of hits eg, only tickers that
#tripped between 8 and 15 times per month

import csv
import pandas as pd

cryptocsv = pd.read_csv("cryptos-jan23.csv", names=["ticker", "count", "date"])
cryptocsv["ticker"] = cryptocsv["ticker"].str.replace('\W', '', regex=True)
df = cryptocsv.groupby(["ticker"]).count()
df2 = df.loc[df['count'].isin([40])]
print(df2)


# ask if user wants to dump contents of dataframe to CSV
exportcontrol = input("Do you want to dump the above to csv? Y/N ")

# if statement supporting the user input
if exportcontrol.lower() == "y":
    df2.to_csv("./csvdump.csv")
    print("dumped to csv")
else:
    print("DID NOT DUMP TO CSV")

