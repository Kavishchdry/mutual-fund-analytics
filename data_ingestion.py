import pandas as pd
import os

DATA_PATH = "data/raw"

for file in os.listdir(DATA_PATH):
    if file.endswith(".csv"):
        path = os.path.join(DATA_PATH, file)

        df = pd.read_csv(path)

        print("\n" + "="*60)
        print(file)
        print("="*60)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())