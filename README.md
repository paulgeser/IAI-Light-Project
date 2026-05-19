# NLP Pipeline: SMS Spam Collection

| | |
|---|---|
| **Modul** | Introduction to AI (IAI) |
| **Professor** | Prof. Dr. Marcel Blattner |
| **Student** | Paul Geser |
| **Projekt** | Light Challenge |


Dataset source (License on website stating: 'unknown', downloaded on the 18.05.2026):

https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Results

| Approach | Accuracy | Macro F1 |
|---|---|---|
| TF-IDF + Logistic Regression | 0.9686 | 0.9251 |
| DistilBERT (pretrained, zero-shot) | 0.5516 | 0.3891 |

## Run

**Docker run:**
```bash
docker build -t nlp-hw .
docker run --rm nlp-hw
```

**Local python run:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m src.main
```
