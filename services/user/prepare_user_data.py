from sklearn.linear_model import LinearRegression, LogisticRegression
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df

def predict_user_results(sleep_hours: float, avg_usage: float):
    results = {}

    # Adicción
    X1 = df[['sleep_hours_per_night', 'avg_daily_usage_hours']]
    y1 = df['addicted_score']
    model1 = LinearRegression().fit(X1, y1)
    addicted_score = model1.predict([[sleep_hours, avg_usage]])[0]

    plt.figure()
    plt.scatter(df['sleep_hours_per_night'], y1)
    plt.axhline(addicted_score, color="red", linestyle="--", label=f"Tu nivel: {addicted_score:.1f}")
    plt.title("Tu nivel de adicción a redes")
    plt.xlabel("Sueño")
    plt.ylabel("Adicción")
    plt.legend()
    b1 = BytesIO(); plt.savefig(b1, format='png'); b1.seek(0)
    plt.close()

    # Rendimiento académico
    X2 = df[['addicted_score', 'avg_daily_usage_hours']]
    y2 = df['affects_academic_performance']
    model2 = LogisticRegression().fit(X2, y2)
    affects_academic = model2.predict([[addicted_score, avg_usage]])[0]

    plt.figure()
    plt.scatter(df['addicted_score'], y2)
    plt.axvline(addicted_score, color="blue", linestyle="--", label="Tu nivel")
    plt.title("¿Afecta tu rendimiento académico?")
    plt.xlabel("Adicción")
    plt.ylabel("Impacto académico")
    plt.legend()
    b2 = BytesIO(); plt.savefig(b2, format='png'); b2.seek(0)
    plt.close()

    # Salud mental
    X3 = df[['sleep_hours_per_night', 'addicted_score']]
    y3 = df['mental_health_score']
    model3 = LinearRegression().fit(X3, y3)
    mental_health = model3.predict([[sleep_hours, addicted_score]])[0]

    plt.figure()
    plt.scatter(df['sleep_hours_per_night'], y3)
    plt.axhline(mental_health, color="green", linestyle="--", label=f"Tu salud mental: {mental_health:.1f}")
    plt.title("Salud mental estimada")
    plt.xlabel("Sueño")
    plt.ylabel("Salud Mental")
    plt.legend()
    b3 = BytesIO(); plt.savefig(b3, format='png'); b3.seek(0)
    plt.close()

    return {
        "addicted_score": round(addicted_score, 2),
        "affects_academic": int(affects_academic),
        "mental_health": round(mental_health, 2),
        "graphs": {
            "addicted_plot": base64.b64encode(b1.read()).decode(),
            "academic_plot": base64.b64encode(b2.read()).decode(),
            "mental_plot": base64.b64encode(b3.read()).decode()
        }
    }
