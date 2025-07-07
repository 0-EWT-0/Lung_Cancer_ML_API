from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df
import pandas as pd  # Importar pandas como pd


# Prediccion Linear para saber si mientras mas adicto a las redes sociales, mas conflictos dentro de ellas tienes

def social_media_addiction_conflicts(addicted_score: float):
    
    X = df[["addicted_score"]]
    y = df["conflicts_over_social_media"]

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
    
    X = df[['sleep_hours_per_night','mental_health_score']]
    y = df['avg_daily_usage_hours']

    model = LinearRegression();
    model.fit(X,y);

    pred = model.predict([[int(sleep_hours), int(mental_health_score)]]);
    
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x = df['sleep_hours_per_night']
    y = df['mental_health_score']
    z = df['avg_daily_usage_hours']

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
    
    X = df[['avg_daily_usage_hours']]
    y = df['sleep_hours_per_night']
    
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

# Predicción lineal para evaluar si las redes sociales aíslan (impacto en salud mental y conflictos)
def social_media_mental_health(avg_daily_usage_hours: float, addicted_score: float):
    # Preparar datos para salud mental
    X_mental = df[['avg_daily_usage_hours', 'addicted_score']]
    y_mental = df['mental_health_score']

    model_mental = LinearRegression()
    model_mental.fit(X_mental, y_mental)

    pred_mental = model_mental.predict([[avg_daily_usage_hours, addicted_score]])

    # Preparar datos para conflictos
    X_conflicts = df[['avg_daily_usage_hours', 'addicted_score']]
    y_conflicts = df['conflicts_over_social_media']

    model_conflicts = LinearRegression()
    model_conflicts.fit(X_conflicts, y_conflicts)

    pred_conflicts = model_conflicts.predict([[avg_daily_usage_hours, addicted_score]])

    # Graficar relación con salud mental
    plt.figure(figsize=(10, 6))
    plt.scatter(X_mental['avg_daily_usage_hours'], y_mental, label='Datos reales (Salud Mental)')
    plt.plot(X_mental['avg_daily_usage_hours'], model_mental.predict(X_mental), color='red', label='Regresión')
    plt.xlabel('Horas de uso diario')
    plt.ylabel('Puntaje de salud mental')
    plt.title('Impacto del uso de redes en la salud mental')
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "prediction_mental_health": int(pred_mental[0]),
        "prediction_conflicts": int(pred_conflicts[0]),
        "plot_base64": image_base64,
        "coefficient_mental": float(model_mental.coef_[0]),  # Coeficiente para avg_daily_usage_hours
        "coefficient_conflicts": float(model_conflicts.coef_[0])  # Coeficiente para avg_daily_usage_hours en conflictos
    }