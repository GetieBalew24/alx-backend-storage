-- SQL script that creates a table users.
-- With these attributes:
--- id, integer, never null, auto increment and primary key
--- email, string (255 characters), never null and unique
--- name, string (255 characters)
 CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email NVARCHAR(255) NOT NULL UNIQUE,
  name NVARCHAR(255)
);