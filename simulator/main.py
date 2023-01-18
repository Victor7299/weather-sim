from utils.data_selector import get_df
from calendar import Calendar
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date
from calendar import Calendar

cal = Calendar()

def monthly_df(df, date: str = None):
    month = df[(df.index >= np.datetime64(date)) &\
                (df.index < np.datetime64(date)+np.timedelta64(1,"M"))]
    return month

def month_by_daily_avg(month_df):
    df = month_df.groupby(pd.Grouper(freq='d')).mean().dropna(how='all')
    return df

def year_by_monthly_avg(year_df):
    df = year_df.groupby(pd.Grouper(freq='m')).mean().dropna(how='all')
    return df



if __name__ == "__main__":
    nox_18 = Path("/home/fernando/Projects/weather-sim/simulator/concatenated_data/nox/nox_18.csv")
    
    # df = get_df(so2_18,names=["Date", "SO2"], only_gt_zero=True)
    nox_df = get_df(nox_18, [1, 3, 5, 7], ["Date", "NO", "NOx", "NO2"], only_gt_zero=True)
    
    february = monthly_df(nox_df, "2018-02")

    feb_daily_avg = month_by_daily_avg(february)
    # february.plot()
    # feb_daily_avg.plot()

    nox_18_df_month_avg = year_by_monthly_avg(nox_df)
    # plt.plot(feb_daily_avg)
    # plt.legend(feb_daily_avg.columns)
    plt.plot(nox_18_df_month_avg)
    plt.title("Concentración mensual promedio de NO, NOX y NO2 en el año 2018")
    plt.legend(nox_df.columns)
    plt.show()



