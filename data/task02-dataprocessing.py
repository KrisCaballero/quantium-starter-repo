import pandas as pd
from pathlib import Path

dataSheets = Path('data')

spreadsheets = list(dataSheets.glob("*.csv"))

convert_csv = []
for file in spreadsheets:
    convert_csv = pd.read_csv(file)

    concsv = concsv[convert_csv["product"] == "pink morsel"]

    convcsv["sales"] = concsv["quantity"] * concsv["price"]

    concsv = concsv[["sales","date","region"]]

    convert_csv.append(concsv)

    converted_csv = pd.concat(convert_csv, ignore_index=True)

    converted_csv.to_csv("finished_csv.csv", index=False)

    print("Saved final file.")
