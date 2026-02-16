SET SESSION cte_max_recursion_depth=300000;

DROP TABLE IF EXISTS mydb.ordersi;
DROP TABLE IF EXISTS mydb.customersi;

CREATE TABLE mydb.customersi(
	customer_id INT PRIMARY KEY auto_increment,
    name VARCHAR(100),
    city VARCHAR(100)
    );
    
CREATE TABLE mydb.ordersi(
	order_id INT PRIMARY KEY auto_increment,
    customer_id INT,
    order_total DECIMAL(10,2),
    order_date DATE);

INSERT INTO mydb.customersi(name,city)
WITH RECURSIVE seq AS (
	SELECT 1 AS n
    UNION ALL
    SELECT n+1 FROM seq WHERE n<50000
    )
SELECT 
	CONCAT('Customer',n),
    CASE
		when n%4=0 THEN 'New York'
        WHEN n%4 =1 THEN 'Chicago'
        WHEN n%4 =2 THEN 'DALLAS'
        ELSE 'Miami'
	END
FROM seq;

INSERT INTO mydb.ordersi(customer_id,order_total,order_date)
WITH RECURSIVE seq AS (
	SELECT 1 AS n
    UNION ALL
    SELECT n+1 FROM seq WHERE n<300000
    )
SELECT 
	FLOOR(1+RAND() *50000),
    RAND() *1000,
    date_sub(CURDATE(),INTERVAL FLOOR(RAND() *365) DAY)
FROM seq;

SET PROFILING=1;
Explain
SELECT *
FROM mydb.customersi c
JOIN mydb.ordersi o ON c.customer_id = o.customer_id
WHERE c.customer_id=12345;


CREATE INDEX idx_orders_customer_id ON mydb.ordersi(customer_id);

EXPLAIN
SELECT *
FROM mydb.customersi c
JOIN mydb.ordersi o ON c.customer_id = o.customer_id
WHERE c.customer_id=12345;

SHOW PROFILES;



