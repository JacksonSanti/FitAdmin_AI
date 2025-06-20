from Models.Treino.model import check_model_accuracy as check_exercise_accuracy
from Models.Serie.model import check_model_accuracy as check_series_reps_accuracy
from utils import *

'''
O modelo Exercise, requer uma accuracy maior, pois ele faz a predição mais detalhada.
O modelo Series_Reps, requer uma accuracy acima de 10% levando-se em conta que ele apenas faz
a predição quantitativa do exercicio. Ou seja de forma unitaria.
'''

def test_accuracy_model_exercise():

    csv = get_exercise_csv()

    model = get_exercise_model()

    columns = get_exercise_columns()

    accuracy = check_exercise_accuracy(csv, model, columns)

    assert accuracy >= 0.80, f"Acurácia fora do Padrão: {accuracy}"


def test_accuracy_model_series_reps():

    csv = get_series_reps_csv()

    model = get_series_reps_model()

    columns = get_series_reps_columns()

    accuracy = check_series_reps_accuracy(csv, model, columns)

    assert accuracy >= 0.20, f"Acurácia fora do Padrão: {accuracy}"


