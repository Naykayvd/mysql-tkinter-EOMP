-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: lifechoices_online
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `name` varchar(30) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `IDnumber` int NOT NULL,
  `phonenumber` int NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nextofkin`
--

DROP TABLE IF EXISTS `nextofkin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nextofkin` (
  `nextofkin_name` varchar(30) NOT NULL,
  `nextofkin_phonenumber` int NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`nextofkin_name`),
  KEY `name` (`name`),
  CONSTRAINT `nextofkin_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nextofkin`
--

LOCK TABLES `nextofkin` WRITE;
/*!40000 ALTER TABLE `nextofkin` DISABLE KEYS */;
INSERT INTO `nextofkin` VALUES ('Greg',789583900,'Simon'),('john',833452367,'Nahum'),('Petrol',988765543,'Vin'),('Rico',124555677,'Abdur-Razaaq'),('Sarah',452367555,'Jason'),('Uthmaan',813636778,'Ghiyaath'),('Victor',894555334,'Brent-Lee');
/*!40000 ALTER TABLE `nextofkin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `name` varchar(30) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `idnumber` varchar(13) NOT NULL,
  `phonenumber` int NOT NULL,
  `time_in` timestamp NULL DEFAULT NULL,
  `time_out` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Abdur-Razaaq','Jardien','0008045538082',671565179,'0000-00-00 00:00:00','0000-00-00 00:00:00'),('Brent-Lee','Johnson','0202285068088',621532382,'0000-00-00 00:00:00','0000-00-00 00:00:00'),('Ghiyaath','Williams','0012235091084',641239715,'0000-00-00 00:00:00','0000-00-00 00:00:00'),('Jason','Calvert','9804075027082',762562346,'0000-00-00 00:00:00','0000-00-00 00:00:00'),('Nahum','Van Diemen','9810215221089',723955815,'0000-00-00 00:00:00','0000-00-00 00:00:00'),('Simon','Smith','9646731094786',749875882,NULL,NULL),('Vin','Diesel','6578787865123',987654321,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-28 16:53:48
