import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def run(train_df: pd.DataFrame, test_df: pd.DataFrame) -> list:
    vec = TfidfVectorizer(max_features=20000, ngram_range=(1, 2))
    X_train = vec.fit_transform(train_df["text"])
    X_test = vec.transform(test_df["text"])

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, train_df["label"])
    y_pred = clf.predict(X_test)

    return y_pred.tolist()
