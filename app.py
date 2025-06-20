from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import *
import pandas as pd
import joblib


def create_app():

    app = Flask(__name__)
    CORS(app) 

    exercise_model = get_exercise_model()
    exercise_columns = get_exercise_columns()

    series_reps_model = get_series_reps_model()
    series_reps_columns = get_series_reps_columns()

    def get_series(exercise, plan, nivel):
        df = pd.DataFrame([{
            'modalidade': plan,
            'nivel': nivel,
            'nome': exercise
        }])

        df_encoded = df_encoded_generic(df, series_reps_columns)
        result = series_reps_model.predict(df_encoded)

        return {
            'exercicio': exercise.capitalize(),
            'series': int(result[0][0]),
            'repeticoes': int(result[0][1])
        }

    def get_exercise(plan, nivel, quantity=6):
        quantity = max(1, quantity)
        df = pd.DataFrame([{
            'modalidade': plan,
            'nivel': nivel
        }])

        df_encoded = df_encoded_generic(df, exercise_columns)

        probas = exercise_model.predict_proba(df_encoded)[0]
        rotulos = exercise_model.classes_

        prob_map = list(zip(rotulos, probas))
        prob_map.sort(key=lambda x: x[1], reverse=True)

        top_exercises = [nome for nome, _ in prob_map if nome != 'outros'][:quantity]

        treino = [get_series(exercise, plan, nivel) for exercise in top_exercises]

        return jsonify({'treino': treino})

    @app.route('/fitai', methods=['POST'])
    def get_data():

        data = request.get_json()

        plan = data.get('plan')
        nivel = data.get('nivel')

        if nivel == 'iniciante':
            return get_exercise(plan, nivel, 6)
        elif nivel == 'intermediario':
            return get_exercise(plan, nivel, 8)
        elif nivel == 'avancado':
            return get_exercise(plan, nivel, 10)
        
    return app
