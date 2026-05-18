from src.load_data import load_and_split
from src.classical import run as run_classical
from src.transformer import run as run_transformer
from src.evaluate import evaluate, save_results, print_table


def main():
    train_df, test_df = load_and_split()

    y_pred_classical = run_classical(train_df, test_df)
    y_pred_transformer = run_transformer(test_df)
    y_true = test_df["label"].tolist()

    results = [
        evaluate(y_true, y_pred_classical, "TF-IDF + Logistic Regression"),
        evaluate(y_true, y_pred_transformer, "DistilBERT (pretrained, zero-shot)"),
    ]

    save_results(results)
    print_table(results)


if __name__ == "__main__":
    main()