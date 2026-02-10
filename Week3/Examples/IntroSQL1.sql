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

SELECT * FROM Customers WHERE NOT Country = "UK" AND NOT Country = "sweden" ORDER BY Country, CustomerName LIMIT 3;



-- -----------------------------------------------------------
CREATE TABLE OrderDetails(
	OrderDetailID int NOT NULL,
	OrderID int,
	ProductID int,
	Quantity int,
	PRIMARY KEY(OrderDetailID)
);


INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (1,10248,11,12);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (2,10248,42,10);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (3,10248,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (4,10249,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (5,10249,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (6,10250,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (7,10250,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (8,10250,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (9,10251,72,5);

INSERT INTO OrderDetails(OrderDetailID, OrderID,ProductID, Quantity)
VALUES (10,10251,72,5);
---------------------------------------------------------------------------------------------
DROP TABLE IF EXISTS Products;
CREATE TABLE Products(
	ProductID int NOT NULL,
	ProductName varchar(255),
	SupplierID int,
	CategoryID int,
	Unit varchar(255),
	Price float,
	Primary Key(ProductID)
);
INSERT INTO Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES (1,'Chais',1,1,'10 boxes x 20 bags',18);

INSERT INTO Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES (2,'Chang',1,1,'24 12 oz bottles',19);

INSERT INTO Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES (3,'Aniseed Syrup',1,2,'12 - 550 ml bottles',10);

INSERT INTO Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES (4,'Chef Anton`s Cajun Seasoning',2,2,'48 - 6 oz jars',22);

INSERT INTO Products(ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES (5,'Chef Anton`s Gumbo Mix',2,2,'36 boxes',21.35);
---------------------------------------------------------------------------------------------------
CREATE TABLE Suppliers(
	SupplierID int NOT NULL,
	SupplierName varchar(255),
	ContactName varchar(255),
	Address varchar(255),
	City varchar(255),
	PostalCode varchar(255),
	Country varchar(255),
	PRIMARY KEY(SupplierID)
);


INSERT INTO Suppliers (SupplierID, SupplierName, ContactName, Address,City, PostalCode, Country)
VALUES (1,'Exotic Liquid','Charlotte Cooper','49 Gilbert St.','London','EC1 4SD','UK');

INSERT INTO Suppliers (SupplierID, SupplierName, ContactName, Address,City, PostalCode, Country)
VALUES (2,'New Orleans Cajun Delights','Shelley Burke','P.O. Box 78934','New Orleans','70117','USA');

INSERT INTO Suppliers (SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country)
VALUES (3,'Grandma Kelly`s Homestead','Regina Murphy','07 Oxford Rd.','Ann Arbor','48104','USA');

-- ------------------------------------------------------------------------------
SELECT * FROM Products;
SELECT MIN(PRICE) AS SmallestPrice FROM Products; 
SELECT * FROM Products order by PRICE LIMIT 3;

SELECT * FROM Customers WHERE substring_index(CustomerName, " ", 1) LIKE 'a___%';
SELECT * FROM Customers WHERE substring_index(CustomerName, " ", -1) LIKE 'F___%';

 
SELECT * FROM Customers WHERE CustomerName LIKE 'a%';
SELECT * FROM Customers WHERE CustomerName LIKE '%or%';

-- selects all customers with a CustomerName that starts with "a" and are at least 3 characters in length:
SELECT * FROM customers WHERE CustomerName LIKE 'a__%';

SELECT * FROM Customers WHERE CustomerName LIKE 'a%o';

SELECT * FROM Customers WHERE City RLIKE '^[bmf]';
-- city begins with b,m, or f and then anything inbetween and ends with n or t
SELECT * FROM Customers WHERE City RLIKE '^[bmf].*[nt]$';

-- IN 
SELECT * FROM Customers WHERE Country IN ('Germany','France','UK');
SELECT * FROM Products WHERE Price BETWEEN 10 and 20 ORDER BY Price;

SELECT City FROM Customers UNION SELECT City FROM Suppliers ORDER BY City;

-- UNION ALL permits duplicates
SELECT City FROM Customers UNION ALL SELECT City FROM Suppliers ORDER BY City;

SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country;
SELECT COUNT(CustomerID) AS cnt, Country FROM Customers AS c GROUP BY Country HAVING cnt >1 ;

SELECT * FROM Products;
SELECT * FROM Suppliers;

-- works with cross join but not the most efficient here
SELECT ProductName FROM Products, Suppliers WHERE Products.SupplierID=Suppliers.supplierID AND Price<20;

-- use inner join instead
SELECT p.ProductName FROM Products p JOIN Suppliers s 
ON p.SupplierID = s.SupplierID
WHERE price<20;

-- cross join
SELECT * FROM Products, Suppliers;

SELECT OrderID, Quantity,
CASE 
	WHEN Quantity > 5 THEN 'The quantity is greater than 5'
    WHEN Quantity = 5 THEN 'The quantity is 5'
    ELSE 'The quantity is under 5'
END AS QuantityText
FROM OrderDetails;

-- stored procedures 

Delimiter //
DROP PROCEDURE IF EXISTS GetCustomersByCountry ;
CREATE PROCEDURE GetCustomersByCountry(IN countryName VARCHAR(50))
BEGIN
	-- SELECT customers from a specific country
	SELECT CustomerID, CustomerName, Country, City
    FROM Customers
    WHERE Country = CountryName
    ORDER BY CustomerName;
    
    -- lets also return the total count of customers from that country
    SELECT COUNT(*) AS TotalCustomers
    FROM Customers
    WHERE Country = countryName;
      
END //
Delimiter ;

CALL GetCustomersByCountry('Germany');

DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee(
`Name` varchar(255), 
Age int , 
Department varchar(255), 
Salary float);

SELECT * FROM Employee;
INSERT INTO Employee Values ("Jon",20,"Sales",40000),("James",25,"Sales",20000),("Jake",35,"Delivery",30000),("Luke",40,"Delivery",1000000);

-- example of a window function
SELECT `Name`, Age, Department, Salary, AVG(SALARY) OVER(PARTITION BY Department) AS Avg_Salary FROM Employee;

-- could do it with self join instead:
SELECT e1.`Name`, e1.Age, e1.Department, e1.Salary, AVG(e2.SALARY) AS Avg_Salary 
FROM employee e1
JOIN employee e2
ON e1.Department = e2.department
GROUP BY e1.Name,e1.Department, e1.Age, e1.Salary;


-- recall the orders and persons table
SELECT * FROM Persons;
SELECT * FROM Orders;
































