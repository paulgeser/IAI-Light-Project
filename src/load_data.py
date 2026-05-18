import os
import pandas as pd
from sklearn.model_selection import train_test_split




def load_and_split():
    file_path = os.path.join("data", "raw", "spam.csv")
    process_directory = os.path.join("data", "processed")
    df = pd.read_csv(file_path, encoding="latin-1", usecols=[0, 1],
                     names=["label", "text"], header=0)
    df["label"] = df["label"].map({"ham": 0, "spam": 1})

    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=42, stratify=df["label"]
    )

    os.makedirs(process_directory, exist_ok=True)
    train_df.to_csv(os.path.join(process_directory, "train.csv"), index=False)
    test_df.to_csv(os.path.join(process_directory, "test.csv"), index=False)

    print(f"Train: {len(train_df)} and Test: {len(test_df)}")
    return train_df, test_df


if __name__ == "__main__":
    load_and_split()
