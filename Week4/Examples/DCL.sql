CREATE DATABASE test;
USE test;
CREATE TABLE Users(id int, name varchar(255));
INSERT INTO Users(id, name) VALUES (1,"jim");
SELECT * FROM Users;

CREATE USER 'yassine'@'%' IDENTIFIED BY 'password';
SHOW GRANTS FOR 'yassine'@'%';

GRANT SELECT ON test.* TO 'yassine'@'%';

CREATE USER 'armin'@'%' IDENTIFIED BY 'password1234';

GRANT SELECT, UPDATE, DELETE on test.* TO 'armin'@'%';

FLUSH PRIVILEGES;

SHOW GRANTS;

SELECT * FROM mysql.user;

-- SELECT * FROM information_schema.table_privileges
-- WHERE table_schema = 'mysql'
-- AND table_name = 'Users'
-- ORDER BY grantee;

SELECT * FROM information_schema.table_privileges;

GRANT ALL PRIVILEGES ON test.* to 'yassine'@'%';
GRANT ALL PRIVILEGES ON test.* to 'yassine'@'%' with GRANT OPTION;

SELECT user, host FROM mysql.user;

SHOW GRANTS FOR 'yassine'@'%';

