import os
import pandas as pd


def combine_csv_files(directory, filename):
    combined_filename = os.path.join(os.path.dirname(directory), filename)
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    if len(csv_files) == 0:
        print(f"No CSV files found in the directory: {directory}")
        return

    combined_data = pd.concat([pd.read_csv(os.path.join(directory, file)) for file in csv_files])
    combined_data.to_csv(combined_filename, index=False)