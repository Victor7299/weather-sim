from pathlib import Path
from calendar import Calendar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

cal = Calendar()


NOX_DATA = Path("../data/nox/data.csv")


def get_df(file_path: str):
    file = pd.read_csv(
        file_path,
        header=None,
        delimiter=",",
        usecols=[1,3],
    )
    df = pd.DataFrame(file)
    df[1] = pd.to_datetime(df[1], format="%Y/%m/%d")
    return df

def monthly_df(df, start_date, end_date):
    month = df.loc[(df[1] > start_date) & (df[1] <= end_date)]
    return month

def daily_avg(month_df, year, month):
    days = tuple(day for day in cal.itermonthdays(year, month) if day != 0)
    avg = []
    df_days = []
    for day in days: # np.datetime64(a.isoformat())
        daily_records = month_df.loc[(month_df[1] >=  np.datetime64(date(year, month, day).isoformat())) &\
                                     (month_df[1] < np.datetime64(date(year, month, day).isoformat()) + np.timedelta64(1,"D"))]
        avg.append(daily_records[3].mean())
        df_days.append(date(year, month, day).isoformat())

    df = dict(
        days = df_days,
        avg = avg,
    )
    return pd.DataFrame(df)


def get_stats(df):
    count, mean, median, std = df.count(), df.mean(), df.median(), df.std()
    return (count, mean, median, std)

def filter_median(df, median, std):
    filtered = df[(df[3] > median-2*std) & (df[3] < median+2*std)]
    return filtered

def filter_zeros(df):
    filtered = df[(df[3] != 0.0)]
    return filtered




if __name__ == "__main__":
    df = get_df(NOX_DATA)
    df = filter_zeros(df) 
    df.set_index(1)
    # print(df)
    
    # january = monthly_df(df, "2018/01/01", "2018/01/31")

    # print(january)
    february = monthly_df(df, "2018/02/01", "2018/02/28")
    feb_daily_avg = daily_avg(february, 2018, 2)
    feb_daily_avg = feb_daily_avg.set_index("days")
    print(feb_daily_avg)
    plt.plot(feb_daily_avg["avg"])
    plt.show()
