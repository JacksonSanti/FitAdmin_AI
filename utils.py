import pandas as pd
from flask import jsonify
import joblib

def get_exercise_model():

    return joblib.load('./Models/Treino/treino_model.pkl')

def get_exercise_columns():

    return joblib.load('./Models/Treino/treino_columns.pkl')

def get_exercise_csv():

    return pd.read_csv('./Models/Treino/treino_csv.csv')

def get_series_reps_model():

    return joblib.load('./Models/Serie/series_reps_model.pkl')

def get_series_reps_columns():

    return joblib.load('./Models/Serie/series_reps_columns.pkl')

def get_series_reps_csv():

    return pd.read_csv('./Models/Serie/series_reps_csv.csv')

def get_exercise(modalidade, nivel):
    modalidade_dict = {
        "musculacao": {
            "avancado": [
                "levantamento terra","agachamento livre","rosca alternada","remada unilateral",
                "pulley atrás","rosca martelo","supino declinado","triceps testa","abdominal oblíquo",
                "rosca direta","stiff",
            ],
            "intermediario": [
                "supino inclinado","agachamento no smith","elevação frontal","leg press",
                "remada curvada","pull-over","remada baixa","pulley frontal","rosca direta",
                "rosca alternada","crucifixo inclinado","crucifixo reto","abdominal infra",
                "triceps banco","glúteo máquina","stiff",
            ],
            "iniciante": [
                "encolhimento de ombros","abdominal na prancha","panturrilha em pé","elevação lateral",
                "desenvolvimento com halteres","crucifixo reto","rosca direta","abdominal supra",
                "supino reto","agachamento no smith","cadeira extensora","cadeira flexora",
                "glúteo com caneleira","triceps pulley","supino reto",
            ],
        },
        "zumba": {
            "iniciante": [
                "passo mambo","cumbia para frente","step touch","zumba cooldown",
                "salsa passo lateral","merengue básico","grapevine","zumba fit balance","cha-cha-cha",
            ],
            "intermediario": [
                "rebolado lateral","zumba cardio","passo quatro tempos","samba básico",
                "zumba cardio","passo cruzado","jazz step","reggaeton baixo","passo africano",
                "zumba twist","axé quadril","zumba squat","batida reggaeton","movimento circular de quadril",
                "twist","zumba corrida",
            ],
            "avancado": [
                "zumba cardio","zumba burn","power zumba","passo africano cruzado",
                "paso doble","movimento de tronco","passo flamenco","zumba boxe",
            ],
        },
        "fisioterapia": {
            "avancado": [
                "reducação postural","deslizamento do nervo ciático",
                "atividade funcional com bola","prancha",
            ],
            "intermediario": [
                "ponte pélvica","coordenação braço-perna","mobilidade torácica","fortalecimento de core",
                "transferência de peso","deslizamento escápulo-torácico","elevação de calcanhar",
                "movimento circular de tornozelo","agachamento assistido","isometria de quadríceps",
                "escada alternada","exercício com faixa elástica","prancha","equilíbrio unilateral",
                "deslizamento neural",
            ],
            "iniciante": [
                "alongamento peitoral","mobilidade escapular", "alongamento cervical","elevação de perna",
                "alongamento de piriforme","caminhada em linha reta","alongamento de tríceps sural",
                "alongamento de lombar","rotação externa de ombro","ativação de glúteos","abdução de quadril",
                "movimentos oculares de coordenação","alongamento de isquiotibiais","ponte pélvica",
            ],
        },
        "crossfit": {
            "avancado": [
                "clean","muscle-up","squat clean","handstand push-up","chest to bar","power clean","snatch",
            ],
            "intermediario": [
                "overhead squat","burpee","thruster","man maker","push jerk","pull-up","split jerk",
                "double under","bear crawl","front squat","push press","power clean","deadlift","snatch",
            ],
            "iniciante": [
                "box jump","lunges","running","toes to bar","burpee","kettlebell swing",
                "plank hold","assault bike","row","wall ball","farmers carry","dumbbell snatch",
            ],
        },
    }
    
    return modalidade_dict[modalidade][nivel][0]

def df_encoded_generic(df, columns):

    df_encoded = pd.get_dummies(df)
    
    for col in columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    return df_encoded[columns]

def general_response(json_data):
    
    return jsonify(json_data) 