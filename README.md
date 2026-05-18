# NLP Pipeline: SMS Spam Collection

Dataset source (License on website stating: 'unknown', downloaded on the 18.05.2026):

https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

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
