from services.data_context import df
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os

# Ruta absoluta del archivo Excel
DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/lung_cancer_dataset_final.xlsx')

# Features base para el modelo
BASE_FEATURES = ["smoking_status", "family_history", "bmi", "cholesterol_level",
                 "asthma", "hypertension", "cirrhosis", "other_cancer", "age", "gender"]
y_train = df["survived"]

# Entrena el modelo base una sola vez al iniciar
model_base = RandomForestClassifier(n_estimators=100, random_state=42)
model_base.fit(df[BASE_FEATURES], y_train)


def predict_survival(smoking_status: int, family_history: int, bmi: float, cholesterol_level: int,
                     asthma: int, hypertension: int, cirrhosis: int, other_cancer: int,
                     age: int, gender: int, country: str = None,
                     cancer_stage=None, diagnosis_date=None, treatment_type=None, end_treatment_date=None):

    # Crear input base
    input_dict = {
        "smoking_status": smoking_status,
        "family_history": family_history,
        "bmi": bmi,
        "cholesterol_level": cholesterol_level,
        "asthma": asthma,
        "hypertension": hypertension,
        "cirrhosis": cirrhosis,
        "other_cancer": other_cancer,
        "age": age,
        "gender": gender
    }

    # Agregar features opcionales si se proporcionan
    if cancer_stage is not None:
        input_dict["cancer_stage"] = cancer_stage
    if treatment_type is not None:
        input_dict["treatment_type"] = treatment_type

    input_data = pd.DataFrame([input_dict])

    # Entrenar modelo solo si hay features adicionales
    if cancer_stage is not None or treatment_type is not None:
        features = BASE_FEATURES.copy()
        if cancer_stage is not None:
            features.append("cancer_stage")
        if treatment_type is not None:
            features.append("treatment_type")

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(df[features], y_train)
    else:
        model = model_base  # Usa el modelo base entrenado

    # Predicción
    pred = int(model.predict(input_data)[0])
    prob = float(model.predict_proba(input_data)[0][1])

    # Guardar en Excel solo si vienen los datos completos (incluyendo fechas)
    if cancer_stage is not None and treatment_type is not None and diagnosis_date and end_treatment_date:
        new_entry = input_dict.copy()
        new_entry.update({
            "country": country,
            "cancer_stage": cancer_stage,
            "treatment_type": treatment_type,
            "diagnosis_date": diagnosis_date,
            "end_treatment_date": end_treatment_date,
            "survived": pred
        })

        # Leer y escribir solo una vez
        df_excel = pd.read_excel(DATA_PATH)
        df_excel = pd.concat([df_excel, pd.DataFrame([new_entry])], ignore_index=True)
        df_excel.to_excel(DATA_PATH, index=False)

    # Filtrar datos similares
    filter_mask = (
        (df["age"].between(age - 2, age + 2)) &
        (df["bmi"].between(bmi - 2, bmi + 2)) &
        (df["gender"] == gender) &
        (df["smoking_status"] == smoking_status)
    )
    if country:  # Solo filtrar por país si se proporciona
        filter_mask &= (df["country"] == country)

    # Limitar resultados para mejorar rendimiento
    similar_filtered = df[filter_mask].head(50)
    similar = similar_filtered[["age", "bmi", "gender", "smoking_status", "country", "survived"]].to_dict(orient="records")

    # Respuesta final
    return {
        "prediction": pred,
        "probability": round(prob, 4),
        "input": input_data.to_dict(orient="records")[0],
        "filtered_data": similar
    }
