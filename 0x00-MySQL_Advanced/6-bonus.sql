-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
delimiter //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    
    -- Check if project exists in the projects table
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;
    
    -- If project does not exist, create a new project
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Insert the new correction for the student
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
    
    -- Update the average_score of the student in the users table
    UPDATE users
    SET average_score = (
        SELECT AVG(score)
        FROM corrections
        WHERE user_id = user_id
    )
    WHERE id = user_id;
    
END //

delimiter ;
