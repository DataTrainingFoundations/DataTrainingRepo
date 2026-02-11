USE mydb;
DROP TABLE IF EXISTS Actors;
CREATE TABLE Actors (
a_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) UNIQUE NOT NULL,
age SMALLINT CHECK (age>=0),
worth INT CHECK (worth>=0)
);

INSERT INTO Actors(name,age, worth) VALUES
('Chris Evans', 50, 30000000),
('Scarlett Johansson', 40, 31000000),
('Elizabeth Olsen', 42, 32000000);

SELECT * FROM Actors;

DROP TABLE IF EXISTS Genre;
CREATE TABLE Genre (
g_id int auto_increment primary key,
name varchar(50) unique not null);

INSERT INTO Genre(name) VALUES
('Action'),
('Adventure'),
('Thriller'),
('Comedy'),
('Drama');

SELECT * FROM Genre;

DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(
m_id int auto_increment primary key,
title varchar(50) not null,
price float check(price>=0),
return_days int default 0,
genre_id int,
FOREIGN KEY(genre_id) REFERENCES Genre(g_id)
);


