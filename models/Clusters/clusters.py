import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from io import BytesIO
import base64
from services.data_context import df


def daily_hours_addicted_age_relation ():
    
    X_cluster = df[['Addicted_Score', 'Avg_Daily_Usage_Hours', 'Age']]
    
    kmeans_model = KMeans(n_clusters=3, random_state=42)
    df['grupo'] = kmeans_model.fit_predict(X_cluster)
    
    x = df['Addicted_Score']
    y = df['Avg_Daily_Usage_Hours']
    z = df['Age']
    c = df['grupo']

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    scatter = ax.scatter(x, y, z, c=c, cmap='rainbow', alpha=0.8, s=60)

    ax.set_xlabel('Nivel de Adiccion')
    ax.set_ylabel('Uso Diario (Horas)')
    ax.set_zlabel('Edad')

    plt.title('Relacion entre Adiccion, Uso de Redes y Edad por cluster')

    cbar = plt.colorbar(scatter, pad=0.1, shrink=0.6)
    cbar.set_label('Grupo')

    ax.view_init(elev=20, azim=135)

    plt.tight_layout()
    plt.show()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }