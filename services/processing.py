import pandas as pd
import mysql.connector

def prepare_dataset():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="admin",
        password="123",
        database="datasetDB"
    )

    query = "SELECT * FROM local_dataset;" 
    
    df = pd.read_sql(query, conn)

    # df['Affects_Academic_Performance'] = df['Affects_Academic_Performance'].apply(lambda x: 1 if x == "Yes" else 0)

    df = pd.get_dummies(df, columns=['Relationship_Status', 'Gender'], drop_first=False)

    conn.close()

    return df
