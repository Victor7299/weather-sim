from pathlib import Path
from calendar import Calendar
from datetime import date

import pandas as pd
import numpy as np

cwd = Path(__file__).parent
cal = Calendar()

def get_df(
    file_path: Path,
    columns: list = None,
    names: list = None,
    delimiter: str = ",",
    only_gt_zero: bool = False,
):
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path.name} doens't exists")
    
    if columns is None:
        columns = [1, 3]

    if names is None:
        names = ["Date", "Concentration"]

    if len(columns) != len(names):
        raise Exception("columns and names must have the same size")

    file = pd.read_csv(
        file_path,
        header=0,
        names=names,
        delimiter=delimiter,
        usecols=columns,
    )

    df = pd.DataFrame(file)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")
    df.set_index("Date", inplace=True)

    if only_gt_zero:
        df = df[df > 0]

    return df

if __name__ == "__main__":
    data = Path(__file__).parent / "concatenated_data"

    nox_18 = data / "nox" / "nox_18.csv"
    df = get_df(nox_18, [1,3, 5, 7], ["Date", "NO", "NOx", "NO2"])
    print(df.index[df.index > "2018/12/30"])