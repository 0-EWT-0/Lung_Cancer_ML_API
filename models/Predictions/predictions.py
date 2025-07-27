from services.data_context import df
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/lung_cancer_dataset_final.xlsx')

def train_model(features):
    X = df[features]
    y = df["survived"]
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_survival(smoking_status: int, family_history: int, bmi: float, cholesterol_level: int,
                     asthma: int, hypertension: int, cirrhosis: int, other_cancer: int,
                     age: int, gender: int, country: str = None,
                     cancer_stage=None, diagnosis_date=None, treatment_type=None, end_treatment_date=None):

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

    if cancer_stage is not None:
        input_dict["cancer_stage"] = cancer_stage
    if treatment_type is not None:
        input_dict["treatment_type"] = treatment_type

    input_data = pd.DataFrame([input_dict])

    model = train_model(input_data.columns.tolist())
    pred = int(model.predict(input_data)[0])
    prob = float(model.predict_proba(input_data)[0][1])

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

        df_excel = pd.read_excel(DATA_PATH)
        df_excel = pd.concat([df_excel, pd.DataFrame([new_entry])], ignore_index=True)
        df_excel.to_excel(DATA_PATH, index=False)

    filter_mask = (
        (df["age"].between(age - 2, age + 2)) &
        (df["bmi"].between(bmi - 2, bmi + 2)) &
        (df["gender"] == gender) &
        (df["smoking_status"] == smoking_status)
    )

    if country:
        filter_mask &= (df["country"] == country)

    similar = df[filter_mask][[
        "age", "bmi", "gender", "smoking_status", "country", "survived"
    ]].to_dict(orient="records")


    return {
        "prediction": pred,
        "probability": round(prob, 4),
        "input": input_data.to_dict(orient="records")[0],
        "filtered_data": similar
    }
