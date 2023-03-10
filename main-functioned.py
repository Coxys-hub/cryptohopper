#crypto hopper - take csv feed and weed out cryptos that tripped between a certain number of hits eg, only tickers that
#tripped between 8 and 15 times per month

import csv
import pandas as pd

cryptocsv = pd.read_csv("cryptos-jan23.csv", names=["ticker", "count", "date"])

#strip BS characters from the ticker colum
cryptocsv["ticker"] = cryptocsv["ticker"].str.replace('\W', '', regex=True)

#slice out cryptos that match [XX]count
#df = cryptocsv.loc[cryptocsv["count"].isin([20])]

df = cryptocsv[(cryptocsv['count'] >= 35) & (cryptocsv['count'] <=51)]

#df = cryptocsv.groupby(['ticker'])
#print(df.first())
print(df)

# ask if user wants to dump contents of dataframe to CSV
def export_control():
    asktosave = input("Do you want to dump the above to csv? Y/N ")

    if asktosave.lower() == "y":
        df.to_csv("./csvdump.csv")
        print("dumped to csv")
    else:
        print("DID NOT DUMP TO CSV")

export_control()

