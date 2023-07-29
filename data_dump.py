
from wineQuality.utils.common import dump_data_to_mongodb


if __name__ == "__main__":
    # Provide the path to the CSV file containing the WineQuality data
    csv_file_path = r"C:\Users\Gaurang\Downloads\winequality-data\winequality-red.csv"
    dump_data_to_mongodb(csv_file_path)
