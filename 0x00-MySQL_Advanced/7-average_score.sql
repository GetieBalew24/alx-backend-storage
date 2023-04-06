-- SQL script to creates a stored procedure ComputeAverageScoreForUser. 
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$$$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INTEGER)
BEGIN
    DECLARE total_mark INT DEFAULT 0;
    DECLARE total_user INT DEFAULT 0;
    SELECT SUM(score) INTO total_mark FROM corrections WHERE corrections.user_id = user_id;
    SELECT COUNT(*) INTO total_user FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users SET users.average_score = IF(total_user = 0, 0, total_mark / total_user) WHERE users.id = user_id;
END $$$$
DELIMITER ;