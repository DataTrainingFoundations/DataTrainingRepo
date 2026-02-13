USE mydb;

DROP TABLE IF Exists actor_movie;
DROP TABLE IF exists Movies;
DROP TABLE IF exists Genre;
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

-- DROP TABLE IF EXISTS Genre;
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

-- DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(
m_id int auto_increment primary key,
title varchar(50) not null,
price float check(price>=0),
return_days int default 0,
genre_id int,
FOREIGN KEY(genre_id) REFERENCES Genre(g_id) on delete set null
);

INSERT INTO Movies (title,price,return_days,genre_id) VALUES
('The Avengers',7.5, default, 1),
('Captain America: Civil War',8, default, 1);

SELECT * FROM Movies;

-- DELETE FROM movies WHERE m_id=1;

-- DELETE FROM Genre WHERE g_id=1;

CREATE TABLE actor_movie (
actor_id int,
FOREIGN KEY (actor_id) references Actors(a_id) on delete cascade,
movie_id int,
foreign key(movie_id) references movies(m_id) on delete cascade,
primary key(actor_id,movie_id)
);

INSERT INTO actor_movie(actor_id,movie_id) VALUES
(1,1),
(1,2)
;

SELECT * FROM actor_movie;

DELETE FROM actors WHERE a_id=1;

SELECT * FROM Movies;
SELECT * FROM actor_movie;
SELECT * FROM Actors;

DESCRIBE actor_movie;
