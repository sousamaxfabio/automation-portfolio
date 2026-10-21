import sqlite3
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent
DATABASE_FILE = PROJECT_FOLDER / "stage2_local.db"


def create_database() -> None:
    with sqlite3.connect(DATABASE_FILE) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL
                    CHECK (priority IN ('low', 'medium', 'high')),
                FOREIGN KEY (customer_id)
                    REFERENCES customers(id)
            )
            """
        )

        connection.execute(
            """
            CREATE INDEX IF NOT EXISTS
                idx_requests_customer_id
            ON requests (customer_id)
            """
        )

        connection.executemany(
            """
            INSERT OR IGNORE INTO customers (id, name)
            VALUES (?, ?)
            """,
            [
                (1, "Example Company"),
                (2, "Sample Customer"),
            ],
        )

        connection.executemany(
            """
            INSERT OR IGNORE INTO requests (
                id,
                customer_id,
                category,
                priority
            )
            VALUES (?, ?, ?, ?)
            """,
            [
                (1, 1, "billing", "high"),
                (2, 2, "technical", "medium"),
            ],
        )


def display_requests() -> None:
    with sqlite3.connect(DATABASE_FILE) as connection:
        rows = connection.execute(
            """
            SELECT
                requests.id,
                customers.name,
                requests.category,
                requests.priority
            FROM requests
            INNER JOIN customers
                ON requests.customer_id = customers.id
            ORDER BY requests.id
            """
        ).fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    create_database()
    display_requests()
    print(f"SQLite database ready: {DATABASE_FILE.name}")