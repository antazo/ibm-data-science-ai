-- EXERCISE 1: USING JOINS

-- Question 1:
-- Write and execute a SQL query to list the school names, community names 
-- and average attendance for communities with a hardship index of 98.

SELECT
	PS.NAME_OF_SCHOOL, PS.COMMUNITY_AREA_NAME, PS.AVERAGE_STUDENT_ATTENDANCE
FROM
	chicago_public_schools PS
LEFT JOIN
	chicago_socioeconomic_data SD
ON
	PS.COMMUNITY_AREA_NUMBER = SD.COMMUNITY_AREA_NUMBER
WHERE
	SD.HARDSHIP_INDEX = "98";

-- Question 2
-- Write and execute a SQL query to list all crimes that took place at a school.
-- Include case number, crime type and community name.

SELECT
	C.CASE_NUMBER, C.PRIMARY_TYPE, SD.COMMUNITY_AREA_NAME
FROM
	chicago_crime C
LEFT JOIN
	chicago_socioeconomic_data SD
ON C.COMMUNITY_AREA_NUMBER = SD.COMMUNITY_AREA_NUMBER
WHERE
	C.LOCATION_DESCRIPTION LIKE '%SCHOOL%';

-- EXERCISE 2: CREATING A VIEW

-- Question 1
-- Write and execute a SQL statement to create a view showing the columns listed in the 
-- following table, with new column names as shown in the second column.

CREATE VIEW view_Public_Schools AS
SELECT
	PS.NAME_OF_SCHOOL AS School_Name,
    PS.Safety_Icon AS Safety_Rating,
	PS.Family_Involvement_Icon AS Family_Rating,
	PS.Environment_Icon AS Environment_Rating,
	PS.Instruction_Icon AS Instruction_Rating,
	PS.Leaders_Icon AS Leaders_Rating,
	PS.Teachers_Icon AS Teachers_Rating
FROM
	chicago_public_schools PS;

-- Write and execute a SQL statement that returns all of the columns from the view.

SELECT * FROM view_Public_Schools;

-- Write and execute a SQL statement that returns just the school name and leaders rating from the view.

SELECT School_Name, Leaders_Rating FROM view_Public_Schools;

-- EXERCISE 3: CREATING A STORED PROCEDURE

-- Question 1
-- Write the structure of a query to create or replace a stored procedure called
-- UPDATE_LEADERS_SCORE that takes a in_School_ID parameter as an integer and a
-- in_Leader_Score parameter as an integer.

DROP PROCEDURE IF EXISTS UPDATE_LEADERS_SCORE;

DELIMITER //
CREATE PROCEDURE UPDATE_LEADERS_SCORE (IN in_School_ID INT, IN in_Leader_Score INT)
BEGIN
END //
DELIMITER ;

-- Question 2
-- Inside your stored procedure, write a SQL statement to update the Leaders_Score field
-- in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID to the
-- value in the in_Leader_Score parameter.

DROP PROCEDURE IF EXISTS UPDATE_LEADERS_SCORE;

DELIMITER //
CREATE PROCEDURE UPDATE_LEADERS_SCORE (IN in_School_ID INT, IN in_Leader_Score INT)
BEGIN
    UPDATE
        chicago_public_schools
    SET
        Leaders_Score = in_Leader_Score
    WHERE
        School_ID = in_School_ID;
END //
DELIMITER ;

-- Question 3
-- Inside your stored procedure, write a SQL IF statement to update the Leaders_Icon field
-- in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID using the
-- following information:

-- Score lower limit    Score upper limit   Icon
-- 80                   99                  Very strong
-- 60                   79                  Strong
-- 40                   59                  Average
-- 20                   39                  Weak
-- 0                    19                  Very weak

DROP PROCEDURE IF EXISTS UPDATE_LEADERS_SCORE;

DELIMITER //
CREATE PROCEDURE UPDATE_LEADERS_SCORE (IN in_School_ID INT, IN in_Leader_Score INT)
BEGIN
    UPDATE chicago_public_schools
    SET Leaders_Score = in_Leader_Score
    WHERE School_ID = in_School_ID;

	IF in_Leader_Score > 0 AND in_Leader_Score < 20 THEN
        -- update icon for 0-19
		UPDATE chicago_public_schools
		SET Leaders_Icon = 'Very_weak'
		WHERE School_ID = in_School_ID;

	ELSEIF in_Leader_Score < 40 THEN
        -- update icon for 20-39
		UPDATE chicago_public_schools
		SET Leaders_Icon = 'Weak'
		WHERE School_ID = in_School_ID;

    ELSEIF in_Leader_Score < 60 THEN
        -- update icon for 40-59
		UPDATE chicago_public_schools
		SET Leaders_Icon = 'Average'
		WHERE School_ID = in_School_ID;

    ELSEIF in_Leader_Score < 80 THEN
        -- update icon for 60-79
		UPDATE chicago_public_schools
		SET Leaders_Icon = 'Strong'
		WHERE School_ID = in_School_ID;

    ELSEIF in_Leader_Score < 100 THEN
        -- update icon for 80-99
		UPDATE chicago_public_schools
		SET Leaders_Icon = 'Very_strong'
		WHERE School_ID = in_School_ID;

    -- EXERCISE 4: USING TRANSACTIONS

    -- Question 1
    -- Update your stored procedure definition. Add a generic ELSE clause to the IF statement
    -- that rolls back the current work if the score did not fit any of the preceding categories.
	ELSE ROLLBACK WORK;

    -- Question 2
    -- Update your stored procedure definition again. Add a statement to commit the current
    -- unit of work at the end of the procedure.
	COMMIT WORK;

    END IF;
END //
DELIMITER ;

-- Question 4
-- Run your code to create the stored procedure.
-- Write a query to call the stored procedure, passing a valid school ID and a leader score
-- of 50, to check that the procedure works as expected.

SELECT School_ID, Leaders_Icon, Leaders_Score FROM chicago_public_schools;
CALL UPDATE_LEADERS_SCORE(610131, 80);
CALL UPDATE_LEADERS_SCORE(610334, 111);
CALL UPDATE_LEADERS_SCORE(610320, 69);
