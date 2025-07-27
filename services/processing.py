# services/processing.py
import os
import pandas as pd

def prepare_dataset():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '..', 'data', 'lung_cancer_dataset_final.xlsx')

    df = pd.read_excel(data_path)

    df_encoded = df.copy()
    df_encoded["gender"] = df_encoded["gender"].map({"Male": 0, "Female": 1})
    df_encoded["family_history"] = df_encoded["family_history"].map({"No": 0, "Yes": 1})
    df_encoded["smoking_status"] = df_encoded["smoking_status"].map({
        "Never Smoked": 0,
        "Passive Smoker": 1,
        "Former Smoker": 2,
        "Current Smoker": 3
    })
    df_encoded["treatment_type"] = df_encoded["treatment_type"].map({
        "Chemotherapy": 0,
        "Surgery": 1,
        "Combined": 2,
        "Radiation": 3
    })
    
    df_encoded["cancer_stage"] = df_encoded["cancer_stage"].map({
        "Stage I": 1,
        "Stage II": 2,
        "Stage III": 3,
        "Stage IV": 4
    })

    return df_encoded
