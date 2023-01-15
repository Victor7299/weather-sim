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
):
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path.name} doens't exists")
    if columns is None:
        columns = [1, 3]

    if names is None:
        names = ["Date", "Concentration"]

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
    return df