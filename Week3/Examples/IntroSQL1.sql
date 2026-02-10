DROP DATABASE IF EXISTS mydb;
CREATE DATABASE mydb;
USE mydb;
-- comments 
SHOW TABLES;
SHOW DATABASES;
-- ----------------------------------------------------------
DROP TABLE IF EXISTS Persons ;
-- CREATE TABLE Persons(
-- PersonID INT AUTO_INCREMENT,
-- LastName VARCHAR(255),
-- Address varchar(255),
-- City varchar(255),
-- PRIMARY KEY (PersonID)
-- );

CREATE TABLE Persons(
PersonID SERIAL,
LastName VARCHAR(255),
Address VARCHAR(255),
City VARCHAR(255),
PRIMARY KEY (PersonID)
);

SHOW TABLES;
INSERT INTO Persons (LastName, Address, City) 
VALUES ('Ola','Hansen','Atlanta');

SELECT * FROM Persons;

-- DROP City Column
ALTER TABLE Persons 
DROP COLUMN Address, 
DROP COLUMN City,
ADD COLUMN FirstName VARCHAR(255), 
ADD COLUMN Age INT;

UPDATE Persons 
SET Age = 30, LastName = 'Hansen', FirstName='Ola'
WHERE PersonID =1;

SELECT * FROM Persons WHERE PersonID=1;
DESCRIBE Persons;

INSERT INTO Persons (PersonID,LastName,FirstName,Age)
VALUES (2,'Svendson','Tove',23),
(3,'Pettersen','Kari',20);

SELECT * FROM Persons;

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
	OrderID INT AUTO_INCREMENT ,
    OrderNumber INT NOT NULL,
    PID BIGINT UNSIGNED,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PID) REFERENCES Persons(PersonID)
	);

INSERT INTO Orders (OrderNumber,PID)
VALUES (77895,3),
(44678,3),
(22456,2),
(24562,1);

SELECT * FROM Orders;

DESCRIBE Orders;

DROP TABLE IF EXISTS Customers;
CREATE TABLE Customers(
	CustomerID INT SERIAL DEFAULT VALUE,
    CustomerName VARCHAR(255),
    ContactName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255),
    PostalCode VARCHAR(255),
    Country VARCHAR(255),
    PRIMARY KEY (CustomerID)
    );
		
INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country)
VALUES ('Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin','12209','Germany');

INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country)
VALUES ('Ana Trujillo','Emparedados','Avda. de la Constitución','México D.F.','05021','Mexico');

INSERT INTO Customers (CUstomerName,COntactName,ADdress,CIty,POstalCode,COuntry)
VALUES ('Antonio Moreno','Taquería','ANtonio Moreno Mataderos','MÉxico D.F.','05023','MeXico');

INSERT INTO CUStomers (CusTomerName,ConTactName,AddRess,CitY,PosTalCode,CouNtry)
VALUES ('AROund the Horn','ThOmas Hardy','120 Hanover Sq.','LoNdon','WA1 1DP','UK');

INSERT INTO CUStomers (CusTomerName,ConTactName,AddRess,CitY,PosTalCode,CouNtry)
VALUES ('BERglunds snabbköp','ChrIstina','BerGuvsvägen 8','LuleÅ','S-958 22','SwedeN');

DESCRIBE CUSTOMers;
SELECT * FROM CUSTOMERS;

SELECT DISTINCT COUNTRy FROM CuSTOMers;

-- if wanted the first customer, by id, per country
SELECT * FROM Customers AS c
WHERE CustomerID = (
	SELECT MIN(CustomerID)
    FROM Customers
    WHERE Country = c.Country);
    
-- or this works too

SELECT * FROM Customers AS c
WHERE CustomerID IN (
	SELECT MIN(CustomerID)
    FROM Customers
    WHERE Country = c.Country);
    
SELECT COUNT(DISTINCT Country) FROM Customers;

SELECT * FROM Customers WHERE Country = "Mexico";

INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country)
VALUES ('Frankfurt Tech Supplies','Hans Muller','Friedrichstrasse 120','Frankfurt','10117','Germany');

SELECT * FROM Customers WHERE Country = "Germany" AND City = "Berlin";

SELECT * FROM Customers WHERE City = "Berlin" OR City = "Frankfurt";








