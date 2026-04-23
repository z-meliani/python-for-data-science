import pandas as pd


def load(path: str) -> pd.DataFrame:

    try:
        dt = pd.read_csv(path)

        print(f"Loading dataset of dimensions {dt.shape}")

    except Exception as e:
        print(f"Error: {e}")
        return None

    return dt
