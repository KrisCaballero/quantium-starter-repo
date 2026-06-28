import pandas as pd
from pathlib import Path

dataSheets = Path('data')

spreadsheets = list(dataSheets.glob("*.csv"))

convert_csv_files = []
for file in spreadsheets:
    convert_csv = pd.read_csv(file)

    convert_csv = convert_csv[convert_csv["product"] == "pink morsel"]

    convert_csv["sales"] = convert_csv["quantity"] * convert_csv["price"]

    convert_csv = convert_csv[["sales","date","region"]]

    convert_csv_files.append(convert_csv)

    converted_csv = pd.concat(convert_csv_files, ignore_index=True)

    converted_csv.to_csv("finishedData.csv", index=False)

    print("Saved final file.")
