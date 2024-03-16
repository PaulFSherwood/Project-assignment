INSERT INTO devices (device_name) VALUES ('hh-60');
INSERT INTO devices (device_name) VALUES ('767');
INSERT INTO devices (device_name) VALUES ('c172');

INSERT INTO mission_profiles (mission_profile_name) VALUES ('Gov\'t Led Tng - Currency');
INSERT INTO mission_profiles (mission_profile_name) VALUES ('61/CMT-1/F');
INSERT INTO mission_profiles (mission_profile_name) VALUES ('111/CPT-15/A');
INSERT INTO mission_profiles (mission_profile_name) VALUES ('61/CMT-2/F');


CALL GetAllMissionProfiles();

CALL GetAllDevices();

CALL GetInstructorUsers()
