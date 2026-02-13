-- Function must return a single value
-- Must contain a RETURN statemenet

DROP TABLE IF EXISTS mydb.accounts;
CREATE TABLE mydb.accounts (
	account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    balance DECIMAL (12,2) NOT NULL,
    overdraft_limit DECIMAL (12,2) NOT NULL DEFAULT 0.00
    );
    
INSERT INTO mydb.accounts (customer_name, balance, overdraft_limit)
VALUES
('Alice Johnson', 1500.00, 500.00),
('Bob Smith', 200.00, 0.00),
('Charlie Brown', 1000.00, 200.00);

DROP FUNCTION IF EXISTS mydb.CanWithdraw;
DELIMITER //


CREATE FUNCTION mydb.CanWithdraw(
	p_account_id INT,
    p_amount DECIMAL (12,2)
)

RETURNS VARCHAR(100)
DETERMINISTIC
-- could say NON DETERMINISTIC if same input yields different outputs, i.e. random number generation used
READS SQL DATA 
-- Reads from tables (SELECT)
-- could also say CONTAINS SQL DATA 
-- Uses SQL, but does not read/write table data
-- could also say MODIFIES SQL DATA i.e. inserts, updates, deletes
-- NO SQL would say function does not use SQL at all
BEGIN
	
	DECLARE current_balance DECIMAL(12,2);
    DECLARE overdraft DECIMAL(12,2);
    
    SELECT balance, overdraft_limit
    INTO current_balance, overdraft
    FROM accounts
    WHERE account_id = p_account_id;

	IF current_balance + overdraft >= p_amount THEN
		RETURN 'Approved';
	ELSE
		RETURN 'Declined - Insufficient Funds';
	END IF;
    
END //

DELIMITER ;

SELECT mydb.CanWithdraw(1,1700.00);

-- TRIGGERS in mysql can only be created to fire on INSERT, UPDATE, DELETE (DML)

DROP TABLE IF EXISTS mydb.employees;
CREATE TABLE mydb.employees (
	employee_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	department VARCHAR(100) NOT NULL,
	salary DECIMAL(12,2) NOT NULL,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
-- automatically set current time when row is updated with ON UPDATE CURRENT_TIMESTAMP

DROP TABLE IF EXISTS mydb.salary_audit;
CREATE TABLE mydb.salary_audit(
	audit_id INT PRIMARY KEY AUTO_INCREMENT,
	employee_id INT,
	old_salary DECIMAL (12,2),
	new_salary DECIMAL (12,2),
	changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	changed_by VARCHAR(100)
);

DELIMITER //

CREATE TRIGGER mydb.before_salary_update
BEFORE UPDATE ON employees
-- could replace BEFORE with AFTER if wanted trigger to run after row is changes
-- UPDATE could be replaced with DELETE OR INSERT
FOR EACH ROW

BEGIN
-- Only lof if salary actually changes
	IF OLD.salary <> NEW.salary THEN 
		INSERT INTO salary_audit (
			employee_id,
            old_salary,
            new_salary,
            changed_by
		)
        VALUES (
			OLD.employee_id,
            OLD.salary,
            NEW.salary,
            CURRENT_USER()
            );
	END IF;
    
END //

DELIMITER ;

INSERT INTO mydb.employees (name,department, salary)
VALUES ('Alice','Engineering',90000.00),('Bob','Accounting',70000);

SELECT * FROM mydb.employees;
SELECT * FROM mydb.salary_audit;

UPDATE mydb.employees
SET salary= 95000.00
WHERE employee_id =1;

SELECT * FROM mydb.employees;
SELECT * FROM mydb.salary_audit;




