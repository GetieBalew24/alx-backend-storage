-- creates a stored procedure to ComputeAverageWeightedScoreForUser for
-- computeing and storeing the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$$$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE to_weight_mark INT DEFAULT 0;
    DECLARE t_weight INT DEFAULT 0;
    SELECT SUM(corrections.score * projects.weight)
        INTO to_weigh_mark
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
    SELECT SUM(projects.weight)
        INTO t_weight
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
    IF t_weight = 0 THEN
        UPDATE users
            SET users.average_score = 0
            WHERE users.id = user_id;
    ELSE
        UPDATE users
            SET users.average_score = t0_weight_mark / t_weight
            WHERE users.id = user_id;
    END IF;
END $$$$
DELIMITER ;