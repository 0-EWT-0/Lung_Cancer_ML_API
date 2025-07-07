import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from io import BytesIO
import base64
from services.data_context import df


def daily_hours_addicted_age_relation():
    X_cluster = df[['addicted_score', 'avg_daily_usage_hours', 'age']].copy()
    
    kmeans_model = KMeans(n_clusters=3, random_state=42)
    df['grupo'] = kmeans_model.fit_predict(X_cluster)

    # Datos para enviar al frontend
    data_points = df[['addicted_score', 'avg_daily_usage_hours', 'age', 'grupo']].to_dict(orient='records')

    # Gráfica opcional en base64
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(df['addicted_score'], df['avg_daily_usage_hours'], df['age'], c=df['grupo'], cmap='rainbow', alpha=0.8, s=60)
    ax.set_xlabel('Nivel de Adicción')
    ax.set_ylabel('Uso Diario (Horas)')
    ax.set_zlabel('Edad')
    plt.title('Relación entre Adicción, Uso de Redes y Edad por cluster')
    cbar = plt.colorbar(scatter, pad=0.1, shrink=0.6)
    cbar.set_label('Grupo')
    ax.view_init(elev=20, azim=135)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64,
        "data": data_points
    }

    
    X_cluster = df[['addicted_score', 'avg_daily_usage_hours', 'age']]
    
    kmeans_model = KMeans(n_clusters=3, random_state=42)
    df['grupo'] = kmeans_model.fit_predict(X_cluster)
    
    x = df['addicted_score']
    y = df['avg_daily_usage_hours']
    z = df['age']
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
    #plt.show()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }