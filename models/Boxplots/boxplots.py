import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df
import pandas as pd

# Boxplot de salud mental por nivel de uso

def mental_health_by_usage_boxplot():
    df['Categoria_Uso'] = pd.cut(df['avg_daily_usage_hours'],
        bins=[0, 2, 4, 6, 24],
        labels=['Bajo', 'Moderado', 'Alto', 'Excesivo']
    )

    plt.figure(figsize=(10, 6))
    df.boxplot(column='mental_health_score', by='Categoria_Uso', grid=False)
    plt.title('Salud mental según nivel de uso de redes sociales')
    plt.suptitle('')
    plt.xlabel('Nivel de uso de redes')
    plt.ylabel('Puntaje de salud mental')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    # Retornar también los datos usados
    data_points = df[['Categoria_Uso', 'mental_health_score']].dropna().to_dict(orient='records')

    return {
        "plot": image_base64,
        "data": data_points
    }

    
    
# Boxplot de uso de redes según estado sentimental

def usage_by_relationship_status_boxplot():
    plt.figure(figsize=(10, 6))
    df.boxplot(column='avg_daily_usage_hours', by='relationship_status', grid=False)
    plt.title('Uso diario de redes sociales según estado sentimental')
    plt.suptitle('')
    plt.xlabel('Estado sentimental')
    plt.ylabel('Horas diarias en redes')
    plt.xticks(rotation=45)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    # Retornar también los datos usados
    data_points = df[['relationship_status', 'avg_daily_usage_hours']].dropna().to_dict(orient='records')

    return {
        "plot": image_base64,
        "data": data_points
    }

    