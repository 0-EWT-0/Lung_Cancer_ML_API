from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df
import pandas as pd

# Arbol, Estudiante duerme lo suficiente segun horas que pasa en redes sociales

def student_sleeps_enough():
    df["duerme_bien"] = df["sleep_hours_per_night"].apply(lambda x: 1 if x >= 7 else 0)

    X = df[["avg_daily_usage_hours"]]
    y = df["duerme_bien"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=50)
    modelo = DecisionTreeClassifier()
    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_test)

    plt.figure(figsize=(25,10))
    plot_tree(modelo, feature_names=["Horas en redes"], class_names=["Duerme mal", "Duerme bien"], filled=True)
    plt.title("Árbol de decisión: ¿Duerme bien según uso de redes?")
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    # Exportar los datos usados
    data_points = pd.concat([X, y], axis=1).rename(columns={
        "avg_daily_usage_hours": "horas_en_redes",
        "duerme_bien": "duerme_bien"
    }).to_dict(orient="records")

    return {
        "prediction": int(pred[0]),
        "plot": image_base64,
        "data": data_points
    }

    
# Redes sociales += Imapcto academido

def social_media_impact_academics():
    X = df[['avg_daily_usage_hours']]
    y = df['affects_academic_performance']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    modelo = DecisionTreeClassifier(max_depth=3)
    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_test)

    plt.figure(figsize=(25, 10))
    plot_tree(modelo, feature_names=["Horas en redes"],
              class_names=["Sin impacto", "Con impacto"], filled=True)
    plt.title("¿El uso de redes sociales afecta el rendimiento académico?")
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    # Exportar los datos usados
    data_points = pd.concat([X, y], axis=1).rename(columns={
        "avg_daily_usage_hours": "horas_en_redes",
        "affects_academic_performance": "impacto_academico"
    }).to_dict(orient="records")

    return {
        "prediction": int(pred[0]),
        "plot": image_base64,
        "data": data_points
    }

    
#     # ESTADO SENTIMENTAL INFLUYE CON EL USO DE LAS REDES SOCIALES

# def social_media_usage_by_relationship_status():
    
#     df["muchas_horas"] = df["avg_daily_usage_hours"].apply(lambda x: 1 if x > 5 else 0)
    
#     le = LabelEncoder()
#     df["estado_codificado"] = le.fit_transform(df["relationship_status"].astype(str))
#     X = df[["estado_codificado"]]
#     y = df["muchas_horas"]
#     modelo = DecisionTreeClassifier(max_depth=3)
#     modelo.fit(X, y)
    
#     pred = modelo.predict([[le.transform(["Single"])[0]]])
    
#     plt.figure(figsize=(8, 5))
#     plot_tree(modelo,
#             feature_names=["Estado sentimental"],
#             class_names=["Pocas horas", "Muchas horas"],
#             filled=True)
#     plt.title("¿El estado sentimental influye en el uso de redes sociales?")
#     #plt.show()
    
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
#     plt.close()

#     return {
#         "prediction": int(pred[0]),
#         "plot": image_base64
#     }