from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df



# Prediccion Linear para saber si mientras mas adicto a las redes sociales, mas conflictos dentro de ellas tienes

def social_media_addiction_conflicts(addicted_score: float):
    
    X = df[["Addicted_Score"]]
    y = df["Conflicts_Over_Social_Media"]

    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict([[int(addicted_score)]])

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Datos reales')
    plt.plot(X, model.predict(X), color="red")
    plt.xlabel("Nivel de adicción")
    plt.ylabel("Conflictos")
    plt.title("Relación entre adicción y conflictos")
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "prediction": int(pred[0]),
        "plot": image_base64
    }
    
# Prediccion linear para saber que tanto influye las horas de sueno y la salud mental con el uso diario de las redes sociales

def slepp_hours_affect_mental_health (sleep_hours: float, mental_health_score: float):
    
    X = df[['Sleep_Hours_Per_Night','Mental_Health_Score']]
    y = df['Avg_Daily_Usage_Hours']

    model = LinearRegression();
    model.fit(X,y);

    pred = model.predict([[int(sleep_hours), int(mental_health_score)]]);
    
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x = df['Sleep_Hours_Per_Night']
    y = df['Mental_Health_Score']
    z = df['Avg_Daily_Usage_Hours']

    scatter = ax.scatter(x, y, z, c=z, cmap='viridis', alpha=0.8)

    ax.set_xlabel('Horas de Sueño por Noche')
    ax.set_ylabel('Puntaje de Salud Mental')
    ax.set_zlabel('Uso Diario de Redes (Horas)')

    plt.title('Relación entre Sueño, Salud Mental y Uso de Redes Sociales')

    cbar = plt.colorbar(scatter, pad=0.1, shrink=0.6)
    cbar.set_label('Horas en Redes Sociales')

    ax.view_init(elev=20, azim=135)

    plt.tight_layout()
    #plt.show()

    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "prediction": int(pred[0]),
        "plot": image_base64
    }


# Prediccion Linear, Mas redes usa=menos sueño

def less_sleep_more_social_media(media_hours: float):
    
    X = df[['Avg_Daily_Usage_Hours']]
    y = df['Sleep_Hours_Per_Night']
    
    model = LinearRegression();
    model.fit(X,y);

    pred = model.predict([[int(media_hours)]]);
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X,y, label='Datos reales')
    plt.plot(X,model.predict(X), color="red")
    plt.xlabel('Horas de uso diario de redes sociales')
    plt.ylabel('Horas de sueño por noche')
    plt.legend("Prediccion:" + str(int(pred[0])))
    plt.title('Relación entre uso de redes y sueño')
    #plt.show();
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "prediction": int(pred[0]),
        "plot": image_base64
    }