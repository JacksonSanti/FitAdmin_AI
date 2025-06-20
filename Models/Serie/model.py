from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils import get_series_reps_csv
import numpy as np
import pandas as pd
import joblib



def check_model_accuracy(csv, model, columns):

    X_raw = csv[["nome", "nivel"]]
    y_true = csv[["series", "repeticoes"]] 

    X_encoded = pd.get_dummies(X_raw)
    X_encoded = X_encoded.reindex(columns=columns, fill_value=0)

    y_pred = model.predict(X_encoded)

    correct = np.all(y_pred == y_true.values, axis=1)
    accuracy = np.mean(correct)

    return accuracy

def create_model():

    csv = get_series_reps_csv()

    X = csv[["nome", "nivel"]]
    y = csv[["series", "repeticoes"]]

    X_encoded = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42
    )

    rf_model = RandomForestClassifier(random_state=42)

    multi_model = MultiOutputClassifier(rf_model)

    multi_model.fit(X_train, y_train)

    y_pred = multi_model.predict(X_test)

    acc_series = accuracy_score(y_test["series"], y_pred[:, 0])
    acc_reps = accuracy_score(y_test["repeticoes"], y_pred[:, 1])

    if acc_series and acc_reps >= 0.4:
        joblib.dump(multi_model, 'RandomForest_dump_series_reps.pkl')
        joblib.dump(X_encoded.columns.tolist(), f'RandomForest_columns.pkl')
        print("Modelo de Series / Reps salvo na Raiz do projeto")
    else: 
        print("Accuracy menor do que o esperado no padrão")
        