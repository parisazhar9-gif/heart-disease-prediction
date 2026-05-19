# ❤️ Heart Disease Prediction

ML project using Random Forest & SVM to predict heart disease.

## Dataset
- Source: [Kaggle - Heart Disease UCI](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
- File: `data/raw/heart.csv`

## Project Structure
heart-disease-prediction/
├── data/           # Raw & processed data
├── notebooks/      # EDA & training notebooks
├── src/            # Python modules
├── models/         # Saved models (.pkl)
├── webapp/         # Flask web app
└── reports/        # EDA figures
## How to Run
1. `pip install -r requirements.txt`
2. Kaggle se dataset `data/raw/` mein rakho
3. `notebooks/01_EDA.ipynb` run karo
4. `notebooks/02_model_training.ipynb` run karo
5. `python webapp/app.py`