-- SQL script to creates a stored procedure ComputeAverageWeightedScoreForUser t
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER ##
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE total_average INT DEFAULT 0;
    SELECT SUM(corrections.score * projects.weight) INTO total_score FROM corrections
            INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id;
    SELECT SUM(projects.weight) INTO total_average FROM corrections INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
    IF total_average = 0 THEN UPDATE users SET users.average_score = 0 WHERE users.id = user_id;
    ELSE
        UPDATE users SET users.average_score = total__score / total_average WHERE users.id = user_id;
    END IF;
END ##
DELIMITER ;