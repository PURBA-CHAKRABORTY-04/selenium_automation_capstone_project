import csv


class CSVReader:

    @staticmethod
    def read_data(file_path):

        with open(
            file_path,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            return list(reader)