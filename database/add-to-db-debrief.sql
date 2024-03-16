USE flight_simulator_db;

CREATE TABLE debrief (
    DebriefID INT AUTO_INCREMENT PRIMARY KEY,
    ActualStartTime TIME,
    ActualStopTime TIME,
    Hours TIME,  -- Assuming this is manually entered, but it could also be calculated
    MissionStatus ENUM('complete', 'incomplete'),
    MDT INT,
    MIRT VARCHAR(255),  -- Adjust size as needed
    ScheduledStartTime TIME,
    ScheduledStopTime TIME,
    ScheduledHours TIME AS (TIMEDIFF(ScheduledStopTime, ScheduledStartTime)),  -- Calculated field
    Debriefer VARCHAR(255),  -- Will be populated dynamically
    Instructor VARCHAR(255),  -- Will be populated dynamically
    Device ENUM('hh-60', '767', 'c172'),  -- Add more as needed
    Date DATE,
    JCN BIGINT,  -- Assuming varchar, but can be an ENUM if you have a fixed set of JCNS
    MissionProfile ENUM('type1', 'type2')  -- Populate with your mission types
);

DROP PROCEDURE IF EXISTS CheckJCNExists;

DELIMITER $$

CREATE PROCEDURE CheckJCNExists(IN jcnToCheck VARCHAR(255), OUT jcnExists TINYINT)
BEGIN
    SELECT EXISTS(SELECT 1 FROM work_orders WHERE jcn = jcnToCheck) INTO jcnExists;
END$$

DELIMITER ;

ALTER TABLE debrief MODIFY COLUMN DebriefID BIGINT;

ALTER TABLE debrief MODIFY COLUMN MissionProfile ENUM('Gov''t Led Tng - Currency', '61/CMT-1/F', '111/CPT-15/A', '61/CMT-2/F');


