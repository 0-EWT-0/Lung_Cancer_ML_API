import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df

def sleep_hours_histogram():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Sleep_Hours_Per_Night'], bins=15, color='mediumseagreen', edgecolor='black')
    plt.title('Distribución de Horas de Sueño por Noche')
    plt.xlabel('Horas de sueño')
    plt.ylabel('Cantidad de estudiantes')
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }
    
def daily_usage_hours_histogram():
    
    plt.figure(figsize=(10, 6))
    plt.hist(df['Avg_Daily_Usage_Hours'], bins=15, color='cornflowerblue', edgecolor='black')
    plt.title('Distribución del Uso Diario de Redes Sociales')
    plt.xlabel('Horas por día')
    plt.ylabel('Cantidad de estudiantes')
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }
    
def age_histogram(): 
    
    df['Age'].hist()
    plt.title('Distribución de Edad')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    
    plt.figure(figsize=(10, 6))
    plt.hist(df['Avg_Daily_Usage_Hours'], bins=15, color='cornflowerblue', edgecolor='black')
    plt.title('Distribución del Uso Diario de Redes Sociales')
    plt.xlabel('Horas por día')
    plt.ylabel('Cantidad de estudiantes')
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }