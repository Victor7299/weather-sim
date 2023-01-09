import pandas as pd
import numpy as np
from pathlib import Path

def get_folders(dir: Path):
    folders = [folder for folder in dir.iterdir() if folder.is_dir()]
    return folders

def get_files(dir: Path):
    files = [str(file) for file in dir.iterdir() if file.is_file()]
    return files


def get_df(file_path: str):
    file = pd.read_csv(file_path, header=None, delimiter=",", usecols=[1,3])
    df = pd.DataFrame(file)
    return df

def get_stats(df):
    count, mean, median, std = df.count(), df.mean(), df.median(), df.std()
    return (count, mean, median, std)

def filter_median(col, median, std):
    # filtered = col[col.apply(lambda x: x > median-std and x < median+std)]
    filtered = col[(col > median-std) & (col < median+std)]
    return filtered


if __name__ == "__main__":
    # "data" folder that contain year data
    # data folder cotain a year folder that is represented by last 2 digits
    ## like 2018 is represented like "18"
    data = Path("data").resolve()
    # 
    year_dir = get_folders(data)[0] # 18
    feb = get_folders(year_dir)[1]
    files = get_files(feb)
    print(files)
    # files = get_files(folders)
    # file = "01.txt"
    # df = get_df(file)
    # # print(df[1])
    # stats = get_stats(df[1])
    # # print(stats)
    # m, s = stats[2], stats[3]
    # filtered_df = filter_median(df[1], m, s)
    # print(filtered_df)

    
