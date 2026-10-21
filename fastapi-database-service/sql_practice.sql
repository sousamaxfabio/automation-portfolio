-- Stage 2 SQL practice and troubleshooting evidence
-- Database: PostgreSQL
--
-- The UPDATE and DELETE demonstrations use transactions followed
-- by ROLLBACK, so they do not permanently change the sample data.


-- 1. SELECT, ORDER BY and LIMIT
-- Return the five most recent service requests.

SELECT
    id,
    customer_id,
    category,
    priority
FROM requests
ORDER BY id DESC
LIMIT 5;


-- 2. WHERE
-- Return only high-priority requests.

SELECT
    id,
    customer_id,
    category,
    priority
FROM requests
WHERE priority = 'high'
ORDER BY id;


-- 3. Aggregate function and GROUP BY
-- Count requests in each priority group.

SELECT
    priority,
    COUNT(*) AS request_count
FROM requests
GROUP BY priority
ORDER BY request_count DESC;


-- 4. INNER JOIN
-- Return requests that have a matching customer.

SELECT
    requests.id,
    customers.name AS customer_name,
    requests.category,
    requests.priority
FROM requests
INNER JOIN customers
    ON requests.customer_id = customers.id
ORDER BY requests.id;


-- 5. LEFT JOIN
-- Return every customer, including customers without requests.

SELECT
    customers.id,
    customers.name,
    COUNT(requests.id) AS request_count
FROM customers
LEFT JOIN requests
    ON customers.id = requests.customer_id
GROUP BY
    customers.id,
    customers.name
ORDER BY customers.id;


-- 6. Investigate missing relationships
-- A returned row would indicate a request with no matching customer.

SELECT
    requests.id,
    requests.customer_id,
    requests.category
FROM requests
LEFT JOIN customers
    ON requests.customer_id = customers.id
WHERE customers.id IS NULL;


-- 7. Investigate incorrect priority data
-- A returned row would contain an unexpected priority value.

SELECT
    id,
    priority
FROM requests
WHERE priority NOT IN ('low', 'medium', 'high');


-- 8. Parameterised-query pattern
-- Python and psycopg supply the value represented by %s.
--
-- SELECT id, category, priority
-- FROM requests
-- WHERE customer_id = %s;


-- 9. UPDATE inside a safe transaction
-- ROLLBACK prevents the demonstration from becoming permanent.

BEGIN;

UPDATE requests
SET priority = 'high'
WHERE id = 1;

SELECT
    id,
    priority
FROM requests
WHERE id = 1;

ROLLBACK;


-- 10. DELETE inside a safe transaction
-- ROLLBACK restores the deleted row.

BEGIN;

DELETE FROM requests
WHERE id = 1;

SELECT
    id,
    customer_id,
    category,
    priority
FROM requests
WHERE id = 1;

ROLLBACK;


-- 11. Basic index
-- This can improve joins and searches using customer_id.

CREATE INDEX IF NOT EXISTS idx_requests_customer_id
ON requests (customer_id);