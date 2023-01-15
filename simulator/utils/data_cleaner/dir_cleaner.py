"""Clean the directory, removing any file that is not a txt file"""
from pathlib import Path

file_exts = [".txt", ".TXT"]


def clean_dir(dir: Path):
    """Simple confirmation prompt before deleting everything"""
    opt = input("Are you sure? (write down 'yes'): ").strip()
    if opt != "yes":
        print(f"Your input {opt} is not the same as 'yes'")
        exit(1)
        # return
    _rm_useless_files(dir)
    print("Useless files and directories have been removed")



def _rm_useless_files(dir: Path):
    """Remove all non txt files and empty directories, use this by your own risk"""
    if dir.is_file():
        raise OSError(f"{dir} is a file, not a directory")
    if not dir.exists():
        raise FileNotFoundError

    matches = sorted(dir.rglob("*"))
    for match_ in matches:
        if match_.is_file() and match_.suffix not in file_exts:
            match_.unlink()
            # continue

        if match_.is_dir():
            try:
                match_.rmdir()
            except OSError as e:
                print(e)


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "raw_data"
    clean_dir(data_dir)