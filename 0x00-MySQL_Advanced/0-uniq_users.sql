-- SQL script/statements that creates a table users.
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email nvarchar(255) NOT NULL UNIQUE,
    name nvarchar(255),
    PRIMARY KEY(id)
);