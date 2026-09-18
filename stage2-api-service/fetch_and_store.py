import os

import httpx
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )


def fetch_external_data():
    api_url = "https://" + "jsonplaceholder.typicode.com/todos/1"

    response = httpx.get(
        api_url,
        timeout=20,
    )

    response.raise_for_status()
    return response.json()


def save_external_data(data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS external_results (
        id SERIAL PRIMARY KEY,
        external_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    )
    """)

    cursor.execute("""
    INSERT INTO external_results (
        external_id,
        title,
        completed
    )
    VALUES (%s, %s, %s)
    """, (
        data["id"],
        data["title"],
        data["completed"],
    ))

    connection.commit()

    cursor.close()
    connection.close()


if __name__ == "__main__":
    external_data = fetch_external_data()

    print("External API result:")
    print(external_data)

    save_external_data(external_data)

    print("External API result stored in PostgreSQL successfully.")