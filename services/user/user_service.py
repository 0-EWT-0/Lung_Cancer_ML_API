import mysql.connector

def insert_user_data(data):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="admin",
        password="123",
        database="datasetDB"
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO local_dataset (
            Age, Gender, Academic_Level, Country, Avg_Daily_Usage_Hours,
            Most_Used_Platform, Sleep_Hours_Per_Night, Relationship_Status,
            Conflicts_Over_Social_Media, username,
            Affects_Academic_Performance, Mental_Health_Score, Addicted_Score
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data["Age"],
        data["Gender"],
        data["Academic_Level"],
        data["Country"],
        data["Avg_Daily_Usage_Hours"],
        data["Most_Used_Platform"],
        data["Sleep_Hours_Per_Night"],
        data["Relationship_Status"],
        data["Conflicts_Over_Social_Media"],
        data["username"],
        data["Affects_Academic_Performance"],
        data["Mental_Health_Score"],
        data["Addicted_Score"]
)


    cursor.execute(query, values)
    conn.commit()
    new_id = cursor.lastrowid

    cursor.close()
    conn.close()
    return new_id


def get_data_by_username(username):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="admin",
        password="123",
        database="datasetDB"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM local_dataset WHERE username = %s;"
    cursor.execute(query, (username,))
    result = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in result]

    cursor.close()
    conn.close()
    return data
