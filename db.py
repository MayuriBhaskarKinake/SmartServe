import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="smartserve",
        user="postgres",
        password="PLAYER"
    )

    cursor = conn.cursor()

    print("Database Connected Successfully")

except Exception as e:
    print("Connection Error:", e)