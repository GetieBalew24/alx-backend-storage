-- SQL script to Create a table with unique users.
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email nvarchar(255) NOT NULL UNIQUE,
    name nvarchar(255),
    country nvarchar(4) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN')),
    PRIMARY KEY(id)
);