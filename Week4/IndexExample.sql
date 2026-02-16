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
        
		
    