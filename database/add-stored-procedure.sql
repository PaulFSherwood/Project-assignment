USE flight_simulator_db;

CREATE TABLE mission_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    MissionProfile ENUM('profile1', 'profile2', 'profile3') NOT NULL,
    device ENUM('device1', 'device2', 'device3') NOT NULL
);

DELIMITER  $$
CREATE PROCEDURE GetAllMissionProfiles()
BEGIN
    SELECT MissionProfile FROM mission_info GROUP BY MissionProfile;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetAllDevices()
BEGIN
    SELECT device FROM mission_info GROUP BY device;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetMaintenanceUsers()
BEGIN
    SELECT * FROM users WHERE role = 'MAINTENANCE';
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetInstructorUsers()
BEGIN
    SELECT * FROM users WHERE role = 'INSTRUCTOR';
END $$
DELIMITER ;