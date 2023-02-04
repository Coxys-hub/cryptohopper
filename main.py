#crypto hopper - take csv feed and weed out cryptos that tripped between a certain number of hits eg, only tickers that
#tripped between 8 and 15 times per month

import csv
import pandas as pd

cryptocsv = pd.read_csv("cryptos-jan23.csv", names=["ticker", "count", "date"])
df = cryptocsv.groupby(["ticker"]).count()
print(df)


# ask if user wants to dump contents of dataframe to CSV
exportcontrol = input("Do you want to dump the above to csv? Y/N ")

# if statement supporting the user input
if exportcontrol.lower() == "y":
    df.to_csv("./csvdump.csv")
    print("dumped to csv")
else:
    print("DID NOT DUMP TO CSV")

