from pathlib import Path

NOX_DIR = Path("../data/nox").resolve()

TARGET_NOX_FILE = Path("../data/nox/data.csv").resolve()


class Concatenator:
    def __init__(self, dir: Path):
        self.dir = dir

    def concatenate(self, target_name: str):
        b_data = b""
        files = sorted(self.dir.rglob(f"{target_name}/**/*.TXT"))
        for file in files:
            b_data += file.read_bytes()

        target = ""
        
        return 

if __name__ == "__main__":
    # files = sorted(NOX_DIR.rglob("18/**/*.TXT"))

    # b_data = b""
    # for file in files:
    #     b_data += file.read_bytes()

    # TARGET_NOX_FILE.write_bytes(b_data)
    print(__file__)