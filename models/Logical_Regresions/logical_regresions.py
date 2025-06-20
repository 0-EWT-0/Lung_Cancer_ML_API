from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df

# Prediccion Logica para saber si las personas que pasan pmas tiempo en redes sociales estan solas

def single_more_hours_social_media(hours: float):
    X = df[["Avg_Daily_Usage_Hours"]]
    y = df["Relationship_Status_Single"]

    model = LogisticRegression()
    model.fit(X, y)

    pred = model.predict([[hours]])
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Datos reales')
    plt.plot(X, model.predict(X), color="red", label='Regresion logistica')
    plt.xlabel("Horas promedio en redes sociales por día")
    plt.ylabel("Es soltero?")
    plt.legend()
    plt.title("Mas horas en redes implica mayor probabilidad de estar soltero?")
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

# Prediccion Logica para saber si estar en una relacion afecta el rendimiento academico

def relations_affect_academy_preformance (is_in_relationship: bool):
    
    X = df[["Relationship_Status_In Relationship"]]
    y = df["Affects_Academic_Performance"]

    model = LogisticRegression()
    model.fit(X, y)

    pred = model.predict([[int(is_in_relationship)]])
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Datos reales')
    plt.plot(X, model.predict(X), color="red", label='Regresion logistica')
    plt.xlabel("Afecta el rendimientro academico?")
    plt.ylabel("Esta en una relacion?")
    plt.legend()
    plt.title("Estar en una relacion implica menor rendimiento academico?")
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

# Prediccion Logica para saber si esta en un estado de relasion complicado pasas menos horas de sueno

def less_sleep_in_complicated_relationship(sleep_hours: float):
    
    X = df[["Sleep_Hours_Per_Night"]]
    y = df["Relationship_Status_Complicated"]

    model = LogisticRegression()
    model.fit(X, y)

    pred = model.predict([[sleep_hours]])
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Datos reales')
    plt.plot(X, model.predict(X), color="red", label='Regresion logistica')
    plt.xlabel("Afecta las horas de sueno?")
    plt.ylabel("Esta en una relacion complicada?")
    plt.legend()
    plt.title("Estar en una relacion complicada implica menor rendimiento academico?")
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

