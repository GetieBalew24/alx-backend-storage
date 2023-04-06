-- SQL script that creates a table users.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    email nvarchar(255) NOT NULL UNIQUE,
    name nvarchar(255),
    PRIMARY KEY(id)
);