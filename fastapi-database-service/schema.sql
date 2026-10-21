-- PostgreSQL database structure for the Stage 2 API Service

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS requests (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL
        CHECK (priority IN ('low', 'medium', 'high')),
    CONSTRAINT fk_requests_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
);

CREATE INDEX IF NOT EXISTS idx_requests_customer_id
ON requests (customer_id);