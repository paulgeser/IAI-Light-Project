import pandas as pd
from transformers import pipeline


def run(test_df: pd.DataFrame) -> list:
    clf = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )

    texts_test = test_df["text"].tolist()
    y_pred = [
        1 if clf(t)[0]["label"] == "POSITIVE" else 0
        for t in texts_test
    ]

    return y_pred
