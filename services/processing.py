import pandas as pd
import psycopg2
from config import DB_CONFIG

def prepare_dataset():
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT * FROM this_dataset;" 
    
    df = pd.read_sql(query, conn)
    
    print(df.head())

    # df['affects_academic_performance'] = df['affects_academic_performance'].apply(lambda x: 1 if x == "Yes" else 0)

    df = pd.get_dummies(df, columns=['relationship_status', 'gender'], drop_first=False)

    conn.close()
    return df

