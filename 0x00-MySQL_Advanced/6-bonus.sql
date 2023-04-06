-- SQL script that creates a stored procedure AddBonus
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$$$
CREATE PROCEDURE AddBonus (user_id INTEGER, project_name nvarchar(255), score float)
BEGIN
    DECLARE pro_count INTEGER DEFAULT 0;
    DECLARE project_id INTEGER DEFAULT 0;
    SELECT COUNT(id)
        INTO pro_count FROM projects WHERE name = project_name;
    IF pro_count = 0 THEN
        INSERT INTO projects(name) VALUES(project_name);
    END IF;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, project_id, score);
END $$$$
DELIMITER ;