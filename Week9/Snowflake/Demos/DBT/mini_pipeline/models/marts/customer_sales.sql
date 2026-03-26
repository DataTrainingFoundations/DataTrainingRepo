SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_sales
FROM {{ ref('stg_orders') }}
GROUP BY customer_id
