from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from utils import get_exercise_csv
import pandas as pd
import joblib


def check_model_accuracy(csv, model, columns):

    y = csv["exercicios"]
    X = csv.drop(columns=["exercicios"])

    counts = y.value_counts()
    limite = 2
    y = y.apply(lambda x: x if counts[x] >= limite else 'outros')

    X_encoded = pd.get_dummies(X)
    X_encoded = X_encoded.reindex(columns=columns, fill_value=0)

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42
    )

    y_pred = model.predict(X_test)

    return accuracy_score(y_test, y_pred)

def create_model():

    csv = get_exercise_csv()

    y = csv['exercicios']
    X = csv.drop(columns=['exercicios'])

    counts = y.value_counts()
    limite = 2 
    y_agrupado = y.apply(lambda x: x if counts[x] >= limite else 'outros')


    X_encoded = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_agrupado, test_size=0.2, random_state=42)

    RandomForest = RandomForestClassifier(random_state=42)
    RandomForest.fit(X_train, y_train)

    y_pred = RandomForest.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    if acc >= 0.6:
        joblib.dump(RandomForest, f'RandomForest_dump_exercise.pkl')
        joblib.dump(X_encoded.columns.tolist(), f'RandomForest_columns_exercise.pkl')
        print("Modelo de Treino salvo na Raiz do projeto")
    else: 
        print("Accuracy menor do que o esperado no padrão")