from typing import Literal
import os

import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel

load_dotenv()

app = FastAPI(
    title="Stage 2 API Service",
    version="1.0.0"
)


class RequestCreate(BaseModel):
    customer_id: int
    category: str
    priority: Literal["low", "medium", "high"]


def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )


def verify_api_key(x_api_key: str = Header(...)):
    expected_api_key = os.getenv("API_KEY")

    if x_api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/readiness")
def readiness():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT 1")
        cursor.fetchone()

        cursor.close()
        connection.close()

        return {
            "status": "ready",
            "database": "connected"
        }

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database not available"
        ) from error


@app.get("/requests")
def get_requests(x_api_key: str = Header(...)):
    verify_api_key(x_api_key)

    connection = get_connection()
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

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [
        {
            "id": row[0],
            "customer": row[1],
            "category": row[2],
            "priority": row[3]
        }
        for row in rows
    ]


@app.post("/requests", status_code=status.HTTP_201_CREATED)
def create_request(
    request: RequestCreate,
    x_api_key: str = Header(...)
):
    verify_api_key(x_api_key)

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT id
        FROM customers
        WHERE id = %s
        """, (request.customer_id,))

        customer = cursor.fetchone()

        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )

        cursor.execute("""
        INSERT INTO requests (customer_id, category, priority)
        VALUES (%s, %s, %s)
        RETURNING id
        """, (
            request.customer_id,
            request.category,
            request.priority
        ))

        new_id = cursor.fetchone()[0]

        connection.commit()

        return {
            "id": new_id,
            "customer_id": request.customer_id,
            "category": request.category,
            "priority": request.priority
        }

    except HTTPException:
        connection.rollback()
        raise

    except Exception as error:
        connection.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected database error"
        ) from error

    finally:
        cursor.close()
        connection.close()