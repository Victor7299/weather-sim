"""Cancatenate all txt files from the data directories"""
from pathlib import Path


def concatenate(root_dir: Path, target: Path|str = None):
    if isinstance(type(target), str):
        target = root_dir.parent / target

    if target is None:
        target = root_dir.parent / "concatenated_data"
    
    target.mkdir(exist_ok=True)

    folder_names = [str(folder).split("/")[-1] \
                    for folder in root_dir.iterdir()]

    for folder in folder_names:
        dir = root_dir / folder


        years = [str(year).split("/")[-1] \
                for year in dir.iterdir()]


        dir_by_year = []
        for year in years:
            dir_by_year.append(dir / year)


        files_by_year = []

        for dir_ in dir_by_year:
            files = sorted(dir_.rglob("*.TXT"))
            files_by_year.append(files)


        for year_, files in zip(years, files_by_year):
            b_data = b""
            for file in files:
                b_data += file.read_bytes()
            
            output_folder = target / folder
            output_folder.mkdir(exist_ok=True)
            output_file = output_folder/ f"{folder}_{year_}.csv"
            output_file.write_bytes(b_data)
            
        

if __name__ == "__main__":
    data_dir = Path(__file__).parent / "raw_data"
    concatenate(data_dir)


    # files = sorted(root_dir.rglob("/*.TXT"))

    # b_data = b""
    # for file in files:
    #     b_data += file.read_bytes()

    # target.write_bytes(b_data)