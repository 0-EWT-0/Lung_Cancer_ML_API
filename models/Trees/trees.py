from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df

# Arbol, Estudiante duerme lo suficiente segun horas que pasa en redes sociales

def student_sleeps_enough():
    
    df["duerme_bien"] = df["Sleep_Hours_Per_Night"].apply(lambda x: 1 if x >= 7 else 0)
    
    X = df[["Avg_Daily_Usage_Hours"]]
    y = df["duerme_bien"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=50)
    modelo = DecisionTreeClassifier()
    modelo.fit(X_train, y_train)
    
    pred = modelo.predict(X_test)
    
    plt.figure(figsize=(25,10))
    plot_tree(modelo, feature_names=["Horas en redes"], class_names=["Duerme mal", "Duerme bien"], filled=True)
    plt.title("Árbol de decisión: ¿Duerme bien según uso de redes?")
    plt.show()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "prediction": int(pred[0]),
        "plot": image_base64
    }
    
# Redes sociales += Imapcto academido

def social_media_impact_academics():
    
    X = df[['Avg_Daily_Usage_Hours']]
    y = df['Affects_Academic_Performance']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    modelo = DecisionTreeClassifier(max_depth=3)
    modelo.fit(X_train, y_train)
    
    pred = modelo.predict(X_test)
    
    plt.figure(figsize=(25, 10))
    plot_tree(modelo, feature_names=["Horas en redes"],
    class_names=["Sin impacto", "Con impacto"], filled=True)
    plt.title("¿El uso de redes sociales afecta el rendimiento académico?")
    plt.show()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "prediction": int(pred[0]),
        "plot": image_base64
    }
    
#     # ESTADO SENTIMENTAL INFLUYE CON EL USO DE LAS REDES SOCIALES

# def social_media_usage_by_relationship_status():
    
#     df["muchas_horas"] = df["Avg_Daily_Usage_Hours"].apply(lambda x: 1 if x > 5 else 0)
    
#     le = LabelEncoder()
#     df["estado_codificado"] = le.fit_transform(df["Relationship_Status"].astype(str))
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
#     plt.show()
    
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
#     plt.close()

#     return {
#         "prediction": int(pred[0]),
#         "plot": image_base64
#     }