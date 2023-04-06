--  SQL script to creates a function SafeDiv that divides the first by the second number. 
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER ####
CREATE FUNCTION SafeDiv
 (a INT, 
  b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE total_result FLOAT DEFAULT 0;
    IF b != 0 THEN
        SET total_result = a / b;
    END IF;
    RETURN total_result;
END ####
DELIMITER ;