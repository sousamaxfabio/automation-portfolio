import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = psycopg.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cursor = connection.cursor()

cursor.execute("""
SELECT
    requests.id,
    customers.name,
    requests.category,
    requests.priority
FROM requests
INNER JOIN customers
ON requests.customer_id = customers.id
ORDER BY requests.id
""")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()