import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from services.data_context import df

# Correlacion Uso de horas diarias, nivel de adicccion, conflictos, horas de sueno

def daily_usage_addiction_conflicts_sleep_correlation():
    x = df[['Avg_Daily_Usage_Hours', 'Addicted_Score', 'Conflicts_Over_Social_Media', 'Sleep_Hours_Per_Night']].corr()
    sns.heatmap(x, annot=True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }
    
def general_correlation_matrix():
    
    correlation_matrix = df.corr(numeric_only=True)
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de Calor de Correlación entre Variables')
    #plt.show()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return {
        "plot": image_base64
    }