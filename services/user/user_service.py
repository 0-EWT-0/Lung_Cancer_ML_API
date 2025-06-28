import psycopg2
from config import DB_CONFIG

def insert_user_data(data):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    query = """
        INSERT INTO prod_dataset (
            age, gender, academic_level, country, avg_daily_usage_hours,
            most_used_platform, sleep_hours_per_night, relationship_status,
            conflicts_over_social_media,
            affects_academic_performance, mental_health_score, addicted_score
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING student_id;
    """

    values = (
        int(data["age"]),
        str(data["gender"]),
        str(data["academic_level"]),
        str(data["country"]),
        float(data["avg_daily_usage_hours"]),
        str(data["most_used_platform"]),
        float(data["sleep_hours_per_night"]),
        str(data["relationship_status"]),
        int(data["conflicts_over_social_media"]),
        int(data["affects_academic_performance"]),
        int(data["mental_health_score"]),
        int(data["addicted_score"])
    )


    cursor.execute(query, values)
    new_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()
    return new_id

# def get_data_by_username(username):
#     conn = psycopg2.connect(**DB_CONFIG)
#     cursor = conn.cursor()

#     query = "SELECT * FROM local_dataset WHERE username = %s;"
#     cursor.execute(query, (username,))
#     result = cursor.fetchall()

#     columns = [desc[0] for desc in cursor.description]
#     data = [dict(zip(columns, row)) for row in result]

#     cursor.close()
#     conn.close()
#     return data
