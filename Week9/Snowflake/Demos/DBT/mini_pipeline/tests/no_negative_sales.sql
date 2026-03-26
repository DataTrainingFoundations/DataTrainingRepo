SELECT *
FROM {{ ref('customer_sales') }}
WHERE total_sales < 0
