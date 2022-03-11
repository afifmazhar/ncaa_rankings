import csv
import os
import pandas as pd

INPUT_DIR = r"C:\Users\sliff\PycharmProjects\ncaa\data\raw\rpi"
OUTPUT_DIR = r"C:\Users\sliff\PycharmProjects\ncaa\data\clean"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "rpi_clean_1994_2019.csv")

if __name__ == '__main__':

    with open(OUTPUT_PATH, "w+") as out_file:
        csv_writer = csv.writer(out_file)
        header = ["team", "rpi", "year"]
        csv_writer.writerow(header)

        for i in range(1994, 2020):
            INPUT_YEAR = str(i)
            INPUT_PATH = os.path.join(INPUT_DIR, "rpi_" + INPUT_YEAR + ".csv")
            with open(INPUT_PATH, "r") as in_file:
                df = pd.read_csv(in_file, skiprows=11)[:-1] \
                    .loc[:, ["School", "RPI"]] \
                    .assign(year=INPUT_YEAR) \
                    .dropna() \
                    .to_csv(out_file, header=False, index=False, mode="a")










