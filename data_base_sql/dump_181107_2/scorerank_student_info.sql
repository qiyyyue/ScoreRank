-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: scorerank
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_info` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `phone_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `continent` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `country` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `city` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `student_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `CI` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `student_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `student_id_UNIQUE` (`student_id`),
  UNIQUE KEY `student_number_UNIQUE` (`student_number`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES (1,'Edith','123456',NULL,NULL,'Europe','UK','Aberdeen','10001','1995-10-01','The Confucius Institute of the University of Aberdeen','Edith'),(2,'Emma','123456',NULL,NULL,'Europe','UK','Aberdeen','10002','1995-10-01','The Confucius Institute of the University of Aberdeen','Emma'),(3,'Jessie','123456',NULL,NULL,'Europe','UK','Aberdeen','10003','1995-10-01','The Confucius Institute of the University of Aberdeen','Jessie'),(4,'Abby','123456',NULL,NULL,'Europe','UK','Aberdeen','10004','1995-10-01','The Confucius Institute of the University of Aberdeen','Abby'),(5,'Anne','123456',NULL,NULL,'Europe','UK','Aberdeen','10005','1995-10-01','The Confucius Institute of the University of Aberdeen','Anne'),(6,'Bella','123456',NULL,NULL,'Europe','UK','Aberdeen','10006','1995-10-01','The Confucius Institute of the University of Aberdeen','Bella'),(7,'Colin','123456',NULL,NULL,'Europe','UK','Aberdeen','10007','1995-10-01','The Confucius Institute of the University of Aberdeen','Colin'),(8,'Amy','123456',NULL,NULL,'Europe','UK','Aberdeen','10008','1995-10-01','The Confucius Institute of the University of Aberdeen','Amy'),(9,'Sarah','123456',NULL,NULL,'Europe','UK','Aberdeen','10009','1995-10-01','The Confucius Institute of the University of Aberdeen','Sarah'),(10,'Kate','123456',NULL,NULL,'Europe','UK','Aberdeen','10010','1995-10-01','The Confucius Institute of the University of Aberdeen','Kate'),(11,'Ashley','123456',NULL,NULL,'Europe','UK','Aberdeen','10011','1995-10-01','The Confucius Institute of the University of Aberdeen','Ashley'),(12,'Larissa','123456',NULL,NULL,'Europe','UK','Aberdeen','10012','1995-10-01','The Confucius Institute of the University of Aberdeen','Larissa'),(13,'Carson','123456',NULL,NULL,'Europe','UK','Edinburgh','10013','1995-10-01','The Confucius Institute of the University of Aberdeen','Carson'),(14,'Bailey','123456',NULL,NULL,'Europe','UK','Edinburgh','10014','1995-10-01','The Confucius Institute of the University of Aberdeen','Bailey'),(15,'Bryan','123456',NULL,NULL,'Europe','UK','Edinburgh','10015','1995-10-01','The Confucius Institute of the University of Aberdeen','Bryan'),(16,'Edward','123456',NULL,NULL,'Europe','UK','Edinburgh','10016','1995-10-01','The Confucius Institute of the University of Aberdeen','Edward'),(17,'Jaden','123456',NULL,NULL,'Europe','UK','Edinburgh','10017','1995-10-01','The Confucius Institute of the University of Aberdeen','Jaden'),(18,'Diego','123456',NULL,NULL,'Europe','UK','Edinburgh','10018','1995-10-01','The Confucius Institute of the University of Aberdeen','Diego');
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-07 14:00:58
