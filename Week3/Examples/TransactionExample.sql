USE mydb;
DROP TABLE IF EXISTS bankaccounts;
CREATE TABLE bankaccounts(
account_no varchar(20) PRIMARY KEY,
funds decimal(8,2)
);

INSERT INTO bankaccounts VALUES 
('ACC1',1000),
('ACC2',1000);

SELECT * FROM bankaccounts;

-- let's transfer 100 dollars from acc1 to acc2, we should make this a transaction to ensure we follow ACID properties

START transaction;
UPDATE bankaccounts SET funds = funds -100 WHERE account_no='ACC1';
UPDATE bankaccounts SET funds = funds +100 WHERE account_no='ACC2';
Commit;

SELECT * FROM bankaccounts;

-- we could INSERT in a transaction, so let's create some new bankaccounts

START Transaction;
INSERT INTO bankaccounts VALUES ('ACC3',10000);
SAVEPOINT sv;
INSERT INTO bankaccounts VALUES ('ACC4',900000);
rollback TO sv;
INSERT INTO bankaccounts VALUES ('ACC5',90000);
COMMIT;

SELECT * FROM Bankaccounts;


DROP PROCEDURE IF EXISTS transfer_funds;

DELIMITER //
CREATE procedure transfer_funds(
	IN from_acc VARCHAR(20),
    IN to_acc VARCHAR(20),
    IN amount DECIMAL (10,2)
    )
    
BEGIN 
	-- define current_balance as local variable in procedure
	DECLARE current_balance DECIMAL(10,2);
    
    START TRANSACTION;
    SELECT funds INTO current_balance
    FROM bankaccounts
    WHERE account_no = from_acc
    FOR UPDATE;
    -- FOR UPDATE locks the selected rows exclusively for your transaction,
    -- other transactions that try to update or delete that row will wait until your transactions commits
    -- or rolls back , this ensures no one can withdraw money from the same account at the same time and 
    -- cuase an overdraft or race condition
    
    -- check if sufficient funds
    IF current_balance >= amount THEN
		-- deduct from sender
        UPDATE bankaccounts
        SET funds = funds-amount
        WHERE account_no = from_acc;
        
        -- add to receiver
        UPDATE bankaccounts
        SET funds = funds+amount
        WHERE account_no = to_acc;
	ELSE
		-- NOT enough funds
        ROLLBACK;
	END IF;
END //

DELIMITER ;

CALL transfer_funds('ACC1','ACC2',200);
SELECT * FROM bankaccounts;

CALL transfer_funds('ACC1','ACC2',800);
SELECT * FROM bankaccounts;


