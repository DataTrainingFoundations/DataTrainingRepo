SET SESSION cte_max_recursion_depth=100000;
DROP TABLE IF EXISTS mydb.employeesi;
CREATE TABLE mydb.employeesi (
	id INT PRIMARY KEY auto_increment,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    SALARY INT
    );
    
    INSERT INTO mydb.employeesi (first_name,last_name,department, salary)
    WITH RECURSIVE seq AS (
		SELECT 1 AS n
        UNION ALL
        SELECT n+1 FROM seq WHERE n<100000
	)    
    SELECT 
		CONCAT('First',n),
        CONCAT('Last',n),
        CASE
			WHEN n % 5 = 0 THEN 'IT'
            WHEN n % 5 = 1 THEN 'HR'
            WHEN n % 5 = 2 THEN 'SALES'
            WHEN n % 5 = 3 THEN 'FINANCE'
            ELSE 'MARKETING'
		END,
        FLOOR(RAND() * 100000)
   FROM seq;     
   
   
        
-- USE mydb;
-- WITH RECURSIVE seq2 AS (
-- 		SELECT 1 AS n
--         UNION ALL
--         SELECT n+1 FROM seq2 WHERE n<100000
-- 	)
-- SELECT * FROM seq2;
    
-- lets run the query without an index


-- EXPLAIN ANALYZE
-- SELECT * FROM mydb.employeesi WHERE department = 'IT';

-- EXPLAIN
-- SELECT * FROM mydb.employeesi WHERE department = 'IT';

SET PROFILING = 1;

SELECT * FROM mydb.employeesi
WHERE last_name='LAST99999';

SELECT * FROM mydb.employeesi
WHERE last_name='LAST99999';

CREATE INDEX idx_lastname ON mydb.employeesi(last_name);
SELECT * FROM mydb.employeesi
WHERE last_name='LAST99999';

SHOW PROFILES;

