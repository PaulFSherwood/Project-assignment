CREATE DATABASE  IF NOT EXISTS `flight_simulator_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `flight_simulator_db`;
-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: flight_simulator_db
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Inventory_Audit`
--

DROP TABLE IF EXISTS `Inventory_Audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Inventory_Audit` (
  `audit_id` int NOT NULL AUTO_INCREMENT,
  `stock_number` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `type` enum('Wall to Wall','Cycle','Spot') DEFAULT NULL,
  PRIMARY KEY (`audit_id`),
  KEY `stock_number` (`stock_number`),
  CONSTRAINT `Inventory_Audit_ibfk_1` FOREIGN KEY (`stock_number`) REFERENCES `Logistics` (`stock_number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventory_Audit`
--

LOCK TABLES `Inventory_Audit` WRITE;
/*!40000 ALTER TABLE `Inventory_Audit` DISABLE KEYS */;
/*!40000 ALTER TABLE `Inventory_Audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Logistics`
--

DROP TABLE IF EXISTS `Logistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Logistics` (
  `stock_number` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) DEFAULT NULL,
  `minimum_stock_number` int DEFAULT NULL,
  `stock_location` varchar(255) DEFAULT NULL,
  `cost_per_item` float DEFAULT NULL,
  `entered_by` int DEFAULT NULL,
  `unique_identifier` varchar(255) DEFAULT NULL,
  `notes` text,
  `repair_cost` float DEFAULT NULL,
  `vendor` varchar(255) DEFAULT NULL,
  `original_part_number` varchar(255) DEFAULT NULL,
  `serial_number` varchar(255) DEFAULT NULL,
  `national_stock_number` varchar(255) DEFAULT NULL,
  `location_type` enum('Electrical','Hydraulic') DEFAULT NULL,
  `preferred_repair_vendor` varchar(255) DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `stock_on_hand` int DEFAULT NULL,
  PRIMARY KEY (`stock_number`),
  KEY `entered_by` (`entered_by`),
  CONSTRAINT `Logistics_ibfk_1` FOREIGN KEY (`entered_by`) REFERENCES `Users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Logistics`
--

LOCK TABLES `Logistics` WRITE;
/*!40000 ALTER TABLE `Logistics` DISABLE KEYS */;
INSERT INTO `Logistics` VALUES (11,'ADI',10,'51c',200,3,'123-ABC','Sample Note 1',20,'Vendor1','1','456','789','Electrical','Vendor1','2023-01-01',1,30),(12,'MFD',10,'55a',250,3,'456-DEF','Sample Note 2',30,'Vendor2','2','789','012','Electrical','Vendor2','2023-01-02',2,20),(13,'HSI',10,'53c',150,3,'789-GHI','Sample Note 3',15,'Vendor3','3','012','345','Electrical','Vendor3','2023-01-03',3,50),(14,'Windscreen',10,'54b',300,3,'012-JKL','Sample Note 4',25,'Vendor4','4','345','678','Electrical','Vendor4','2023-01-04',4,30),(15,'Battery',100,'100a',20,3,'123-ABC','Sample Note 5',2,'Vendor1','5','456','789','Electrical','Vendor1','2023-01-05',1,50),(16,'Bandaids',100,'101b',5,3,'456-DEF','Sample Note 6',1,'Vendor2','6','789','012','Hydraulic','Vendor2','2023-01-06',2,30),(17,'Screws',100,'102c',10,3,'789-GHI','Sample Note 7',1.5,'Vendor3','7','012','345','Hydraulic','Vendor3','2023-01-07',3,1),(18,'Tire',4,'1d',400,3,'012-JKL','Sample Note 8',40,'Vendor4','8','345','678','Hydraulic','Vendor4','2023-01-08',4,5),(19,'Landing Gear',2,'2a',1000,3,'123-ABC','Sample Note 9',100,'Vendor1','9','456','789','Hydraulic','Vendor1','2023-01-09',1,2),(20,'Aircraft Shell',1,'3d',5000,3,'456-DEF','Sample Note 10',500,'Vendor2','10','789','012','Hydraulic','Vendor2','2023-01-10',2,1),(21,'ADI',10,'51c',200,3,'123-ABC','Sample Note 1',20,'Vendor1','123','456','789','Electrical','Vendor1','2023-01-01',1,22),(22,'MFD',10,'55a',250,3,'456-DEF','Sample Note 2',30,'Vendor2','456','789','012','Electrical','Vendor2','2023-01-02',2,22),(23,'HSI',10,'53c',150,3,'789-GHI','Sample Note 3',15,'Vendor3','789','012','345','Electrical','Vendor3','2023-01-03',3,23),(24,'Windscreen',10,'54b',300,3,'012-JKL','Sample Note 4',25,'Vendor4','012','345','678','Electrical','Vendor4','2023-01-04',4,10),(25,'Battery',100,'100a',20,3,'123-ABC','Sample Note 5',2,'Vendor1','123','456','789','Electrical','Vendor1','2023-01-05',1,101),(26,'Bandaids',100,'101b',5,3,'456-DEF','Sample Note 6',1,'Vendor2','456','789','012','Hydraulic','Vendor2','2023-01-06',2,101),(27,'Screws',100,'102c',10,3,'789-GHI','Sample Note 7',1.5,'Vendor3','789','012','345','Hydraulic','Vendor3','2023-01-07',3,101),(28,'Tire',50,'1d',400,3,'012-JKL','Sample Note 8',40,'Vendor4','012','345','678','Hydraulic','Vendor4','2023-01-08',4,50),(29,'Landing Gear',50,'2a',1000,3,'123-ABC','Sample Note 9',100,'Vendor1','123','456','789','Hydraulic','Vendor1','2023-01-09',1,50),(30,'Aircraft Shell',50,'3d',5000,3,'456-DEF','Sample Note 10',500,'Vendor2','456','789','012','Hydraulic','Vendor2','2023-01-10',2,50);
/*!40000 ALTER TABLE `Logistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maintenance_Schedule`
--

DROP TABLE IF EXISTS `Maintenance_Schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Maintenance_Schedule` (
  `schedule_id` int NOT NULL AUTO_INCREMENT,
  `simulator_id` int DEFAULT NULL,
  `next_maintenance_date` date DEFAULT NULL,
  PRIMARY KEY (`schedule_id`),
  KEY `simulator_id` (`simulator_id`),
  CONSTRAINT `Maintenance_Schedule_ibfk_1` FOREIGN KEY (`simulator_id`) REFERENCES `Simulators` (`simulator_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maintenance_Schedule`
--

LOCK TABLES `Maintenance_Schedule` WRITE;
/*!40000 ALTER TABLE `Maintenance_Schedule` DISABLE KEYS */;
INSERT INTO `Maintenance_Schedule` VALUES (1,1,'2023-06-19'),(2,2,'2026-06-09');
/*!40000 ALTER TABLE `Maintenance_Schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Missions`
--

DROP TABLE IF EXISTS `Missions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Missions` (
  `mission_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mission_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Missions`
--

LOCK TABLES `Missions` WRITE;
/*!40000 ALTER TABLE `Missions` DISABLE KEYS */;
INSERT INTO `Missions` VALUES (1,'Training Flight'),(2,'Test Flight'),(3,'Search and Rescue'),(4,'Aerial Survey'),(5,'Medical Evacuation'),(6,'Cargo Transport'),(7,'Aerial Firefighting'),(8,'Passenger Transport'),(9,'Photography and Filming'),(10,'Scientific Research');
/*!40000 ALTER TABLE `Missions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Parts`
--

DROP TABLE IF EXISTS `Parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Parts` (
  `part_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `cost` float DEFAULT NULL,
  `stock_number` int DEFAULT NULL,
  PRIMARY KEY (`part_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Parts`
--

LOCK TABLES `Parts` WRITE;
/*!40000 ALTER TABLE `Parts` DISABLE KEYS */;
INSERT INTO `Parts` VALUES (1,'ADI',100,123456),(2,'MFD',200,123457),(3,'ECU',150,123458),(4,'APU',300,123459),(5,'EFIS',250,123460),(6,'FMS',180,123461),(7,'TCAS',220,123462),(8,'RADAR',280,123463),(9,'TCM',190,123464),(10,'EGPWS',230,123465);
/*!40000 ALTER TABLE `Parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Preflight_Schedule`
--

DROP TABLE IF EXISTS `Preflight_Schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Preflight_Schedule` (
  `schedule_id` int NOT NULL AUTO_INCREMENT,
  `simulator_id` int DEFAULT NULL,
  `preflight_date` date DEFAULT NULL,
  PRIMARY KEY (`schedule_id`),
  KEY `simulator_id` (`simulator_id`),
  CONSTRAINT `Preflight_Schedule_ibfk_1` FOREIGN KEY (`simulator_id`) REFERENCES `Simulators` (`simulator_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Preflight_Schedule`
--

LOCK TABLES `Preflight_Schedule` WRITE;
/*!40000 ALTER TABLE `Preflight_Schedule` DISABLE KEYS */;
INSERT INTO `Preflight_Schedule` VALUES (1,1,'2023-06-13');
/*!40000 ALTER TABLE `Preflight_Schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Simulator_Subsystems`
--

DROP TABLE IF EXISTS `Simulator_Subsystems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Simulator_Subsystems` (
  `id` int NOT NULL AUTO_INCREMENT,
  `simulator_id` int DEFAULT NULL,
  `subsystem_id` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `simulator_id` (`simulator_id`),
  KEY `subsystem_id` (`subsystem_id`),
  CONSTRAINT `Simulator_Subsystems_ibfk_1` FOREIGN KEY (`simulator_id`) REFERENCES `Simulators` (`simulator_id`),
  CONSTRAINT `Simulator_Subsystems_ibfk_2` FOREIGN KEY (`subsystem_id`) REFERENCES `Subsystems` (`subsystem_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Simulator_Subsystems`
--

LOCK TABLES `Simulator_Subsystems` WRITE;
/*!40000 ALTER TABLE `Simulator_Subsystems` DISABLE KEYS */;
INSERT INTO `Simulator_Subsystems` VALUES (1,1,1,'Active'),(2,1,2,'Active'),(3,2,1,'Active'),(4,2,2,'Active');
/*!40000 ALTER TABLE `Simulator_Subsystems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Simulators`
--

DROP TABLE IF EXISTS `Simulators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Simulators` (
  `simulator_id` int NOT NULL AUTO_INCREMENT,
  `model` varchar(255) DEFAULT NULL,
  `date_installed` date DEFAULT NULL,
  `last_maintenance_date` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`simulator_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Simulators`
--

LOCK TABLES `Simulators` WRITE;
/*!40000 ALTER TABLE `Simulators` DISABLE KEYS */;
INSERT INTO `Simulators` VALUES (1,'737','2023-06-12','2023-06-12','Active'),(2,'747','2023-06-12','2023-06-12','Active'),(3,'Simulator Model 1','2023-01-01','2023-01-01','Active'),(4,'Simulator Model 2','2023-02-01','2023-02-01','Active'),(5,'Simulator Model 3','2023-03-01','2023-03-01','Active'),(6,'Simulator Model 4','2023-04-01','2023-04-01','Active'),(7,'Simulator Model 5','2023-05-01','2023-05-01','Active'),(8,'Simulator Model 6','2023-06-01','2023-06-01','Active');
/*!40000 ALTER TABLE `Simulators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Subsystems`
--

DROP TABLE IF EXISTS `Subsystems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Subsystems` (
  `subsystem_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`subsystem_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Subsystems`
--

LOCK TABLES `Subsystems` WRITE;
/*!40000 ALTER TABLE `Subsystems` DISABLE KEYS */;
INSERT INTO `Subsystems` VALUES (1,'Hydraulics'),(2,'Electrical'),(3,'Avionics'),(4,'Fuel Systems'),(5,'Propulsion'),(6,'Air Conditioning'),(7,'Environmental Control Systems'),(8,'Landing Gear'),(9,'Navigation Systems'),(10,'Communication Systems');
/*!40000 ALTER TABLE `Subsystems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `is_manager` tinyint(1) DEFAULT '0',
  `is_mantenance` tinyint(1) DEFAULT '0',
  `is_logistics` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Anderson','1234',1,0,0),(2,'Bailey','1234',0,1,0),(3,'Carter','1234',0,0,1),(4,'Davis','1234',1,0,0),(5,'Edwards','1234',0,1,0),(6,'Foster','1234',0,0,1),(7,'Gray','1234',1,0,0),(8,'Hughes','1234',0,1,0),(9,'Jenkins','1234',0,0,1),(10,'King','1234',1,0,0);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkOrder_Missions`
--

DROP TABLE IF EXISTS `WorkOrder_Missions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WorkOrder_Missions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jcn` int DEFAULT NULL,
  `mission_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mission_id` (`mission_id`),
  CONSTRAINT `WorkOrder_Missions_ibfk_2` FOREIGN KEY (`mission_id`) REFERENCES `Missions` (`mission_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkOrder_Missions`
--

LOCK TABLES `WorkOrder_Missions` WRITE;
/*!40000 ALTER TABLE `WorkOrder_Missions` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkOrder_Missions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkOrder_Parts`
--

DROP TABLE IF EXISTS `WorkOrder_Parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WorkOrder_Parts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jcn` bigint DEFAULT NULL,
  `part_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `action` enum('added','removed') NOT NULL,
  `action_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jcn` (`jcn`),
  KEY `part_id` (`part_id`),
  CONSTRAINT `WorkOrder_Parts_ibfk_2` FOREIGN KEY (`part_id`) REFERENCES `Parts` (`part_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkOrder_Parts`
--

LOCK TABLES `WorkOrder_Parts` WRITE;
/*!40000 ALTER TABLE `WorkOrder_Parts` DISABLE KEYS */;
INSERT INTO `WorkOrder_Parts` VALUES (1,20230613003,1,10,'added','2023-06-14'),(2,20230525003,2,5,'added','2023-05-26'),(3,20230315001,3,8,'added','2023-03-16');
/*!40000 ALTER TABLE `WorkOrder_Parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorkOrders`
--

DROP TABLE IF EXISTS `WorkOrders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WorkOrders` (
  `jcn` bigint NOT NULL,
  `simulator_id` int DEFAULT NULL,
  `subsystem_id` int DEFAULT NULL,
  `creation_date` date DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  `total_time` float DEFAULT NULL,
  `creation_reason` text,
  `correction_note` text,
  `parts_added_removed` text,
  `sign_off_date` date DEFAULT NULL,
  `signed_off_by` int DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `reported_by_name` varchar(255) DEFAULT NULL,
  `notes` text,
  `hours` float DEFAULT NULL,
  `disposition` enum('AWM','AWT','AWE') DEFAULT 'AWM',
  PRIMARY KEY (`jcn`),
  KEY `simulator_id` (`simulator_id`),
  KEY `subsystem_id` (`subsystem_id`),
  KEY `signed_off_by` (`signed_off_by`),
  CONSTRAINT `WorkOrders_ibfk_1` FOREIGN KEY (`simulator_id`) REFERENCES `Simulators` (`simulator_id`),
  CONSTRAINT `WorkOrders_ibfk_2` FOREIGN KEY (`subsystem_id`) REFERENCES `Simulator_Subsystems` (`id`),
  CONSTRAINT `WorkOrders_ibfk_3` FOREIGN KEY (`signed_off_by`) REFERENCES `Users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorkOrders`
--

LOCK TABLES `WorkOrders` WRITE;
/*!40000 ALTER TABLE `WorkOrders` DISABLE KEYS */;
INSERT INTO `WorkOrders` VALUES (20230213001,1,1,'2023-06-12','2023-06-12',1,'Initial work order','Test was completed','Part1','2023-06-12',2,3,'bob','note 1',1,'AWM'),(20230315001,2,2,'2023-01-01','2023-01-02',2,'Scheduled work order','Work order completed','Part2','2023-01-03',3,2,'cory','No additional notes',2,'AWM'),(20230315002,3,3,'2023-02-01','2023-02-02',3,'Emergency work order','Work order completed','Part3','2023-02-03',4,1,'daisy','replaced emergency',3,'AWT'),(20230401001,4,4,'2023-03-01','2023-03-02',4,'Regular work order','Work order completed','Part4','2023-03-03',5,3,'emma','No additional notes',4,'AWE'),(20230409001,5,1,'2023-04-01','2023-04-02',1.5,'Unscheduled work order','Work order completed','Part5','2023-04-03',6,2,'frank','No additional notes',1.5,'AWM'),(20230525001,6,2,'2023-05-01','2023-05-02',2.5,'Scheduled work order','Work order completed','Part6','2023-05-03',2,3,'gene','No additional notes',2.5,'AWT'),(20230525002,1,3,'2023-06-01','2023-06-02',3.5,'Emergency work order','Work order completed','Part7','2023-06-03',3,1,'john','No additional notes',3.5,'AWE'),(20230525003,2,4,'2023-07-01','2023-07-02',4.5,'Regular work order','Work order completed','Part8','2023-07-03',4,2,'kyle','No additional notes',4.5,'AWM'),(20230613001,3,1,'2023-08-01','2023-08-02',1.75,'Unscheduled work order','Work order completed','Part9','2023-08-03',5,3,'lucy','No additional notes',1.75,'AWT'),(20230613002,4,2,'2023-09-01','2023-09-02',2.75,'Scheduled work order','Work order completed','Part10','2023-09-03',6,3,'jean','No additional notes',2.75,'AWE'),(20230613003,5,3,'2023-06-12','2023-06-12',3.75,'Emergency work order','Work order completed','Part11','2023-10-03',2,2,'daisy','No additional notes',3.75,'AWM');
/*!40000 ALTER TABLE `WorkOrders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Write_Up_Templates`
--

DROP TABLE IF EXISTS `Write_Up_Templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Write_Up_Templates` (
  `template_id` int NOT NULL AUTO_INCREMENT,
  `description` text,
  PRIMARY KEY (`template_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Write_Up_Templates`
--

LOCK TABLES `Write_Up_Templates` WRITE;
/*!40000 ALTER TABLE `Write_Up_Templates` DISABLE KEYS */;
INSERT INTO `Write_Up_Templates` VALUES (1,'Template1'),(2,'Template2');
/*!40000 ALTER TABLE `Write_Up_Templates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'flight_simulator_db'
--

--
-- Dumping routines for database 'flight_simulator_db'
--
/*!50003 DROP PROCEDURE IF EXISTS `GetInventoryData` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`sherwood`@`localhost` PROCEDURE `GetInventoryData`()
BEGIN
    SELECT l.stock_on_hand, l.item_name, l.minimum_stock_number, l.stock_location, l.cost_per_item, u.username
    FROM Logistics l
    JOIN Users u ON l.entered_by = u.user_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetTechSummary` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`sherwood`@`localhost` PROCEDURE `GetTechSummary`()
BEGIN
    SELECT 
        Users.username as tech,
        SUM(WorkOrders.hours) as total_hours,
        SUM(Logistics.cost_per_item * WorkOrder_Parts.quantity) as total_cost
    FROM 
        WorkOrder_Parts
    JOIN
        WorkOrders ON WorkOrder_Parts.jcn = WorkOrders.jcn
    JOIN
        Logistics ON WorkOrder_Parts.part_id = Logistics.original_part_number
    JOIN
        Users ON WorkOrders.signed_off_by = Users.user_id
    WHERE 
        WorkOrder_Parts.action_date >= CURDATE() - INTERVAL 7 DAY
        AND WorkOrder_Parts.action = 'added'
    GROUP BY 
        Users.username;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `show_parts_data` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`sherwood`@`localhost` PROCEDURE `show_parts_data`()
BEGIN
    SELECT item_name, cost_per_item, due_date, priority 
    FROM Logistics 
    ORDER BY due_date DESC 
    LIMIT 5;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-20 22:27:01
