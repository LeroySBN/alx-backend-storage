-- SQL script that creates a table
DROP TABLE IF EXISTS users;
CREATE TABLE users IF NOT EXISTS (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (id)
);
