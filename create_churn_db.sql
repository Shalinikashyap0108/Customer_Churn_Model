-- Create Database
CREATE DATABASE IF NOT EXISTS churn_db;
USE churn_db;

-- Create Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    gender VARCHAR(10),
    age INT,
    tenure INT,
    balance FLOAT,
    products_number INT,
    has_credit_card TINYINT,
    is_active_member TINYINT,
    estimated_salary FLOAT,
    churn TINYINT
);

-- Insert Random Data (500 Rows)
DELIMITER //
CREATE PROCEDURE insert_customers()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 500 DO
        INSERT INTO customers (gender, age, tenure, balance, products_number, has_credit_card, is_active_member, estimated_salary, churn)
        VALUES (
            ELT(FLOOR(1 + (RAND() * 2)), 'Male', 'Female'),
            FLOOR(18 + (RAND() * 50)), 
            FLOOR(1 + (RAND() * 10)),
            ROUND(RAND() * 100000, 2),
            FLOOR(1 + (RAND() * 4)),
            FLOOR(RAND() * 2),
            FLOOR(RAND() * 2),
            ROUND(RAND() * 150000, 2),
            FLOOR(RAND() * 2)
        );
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

CALL insert_customers();
DROP PROCEDURE insert_customers;
SELECT COUNT(*) FROM churn_db.customers;
