-- SQL script that creates a table
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country VARCHAR(255) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN')),
  PRIMARY KEY (id)
);
