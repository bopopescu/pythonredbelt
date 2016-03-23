-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: travels
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tagalongs`
--

DROP TABLE IF EXISTS `tagalongs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagalongs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trip_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_trip_id_idx` (`trip_id`),
  KEY `fk_user_id_idx` (`user_id`),
  CONSTRAINT `fk_trip_id` FOREIGN KEY (`trip_id`) REFERENCES `travels` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagalongs`
--

LOCK TABLES `tagalongs` WRITE;
/*!40000 ALTER TABLE `tagalongs` DISABLE KEYS */;
INSERT INTO `tagalongs` VALUES (7,13,2),(13,1,7),(14,10,6),(15,17,1),(16,18,1),(17,12,1),(18,16,1),(19,20,6);
/*!40000 ALTER TABLE `tagalongs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travels`
--

DROP TABLE IF EXISTS `travels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `travels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination` varchar(255) DEFAULT NULL,
  `depart` date DEFAULT NULL,
  `returndate` date DEFAULT NULL,
  `plan` varchar(255) DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_created_by_idx` (`created_by`),
  CONSTRAINT `fk_created_by` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travels`
--

LOCK TABLES `travels` WRITE;
/*!40000 ALTER TABLE `travels` DISABLE KEYS */;
INSERT INTO `travels` VALUES (1,'Monaco','0000-00-00','0000-00-00','Let\'s go to monaco',1),(10,'rome','2016-03-03','2016-03-26','to see the pytamids',1),(12,'new york city','2016-03-18','2016-03-19','i hear they have buildigs',6),(13,'just one please','2016-03-09','2016-04-15','her',6),(16,'Portland','2016-03-26','2016-09-23','Dream of the 90s',6),(17,'kentucky','2016-03-25','2016-03-31','to meet the heart land',2),(18,'munich','2016-03-05','2016-03-13','to learn yodeling',2),(19,'Alcatraz','2016-06-10','2016-03-25','its name is etymologically Arabic',1),(20,'The Center of the Earth','2016-03-04','2016-03-05','what a voyage!',1),(21,'meet the beatles','2016-03-26','2016-03-30','with us!',8),(22,'asf','2016-03-02','2016-03-26','afafffff',8);
/*!40000 ALTER TABLE `travels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `pw_hash` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Michael','marboga','$2b$12$r8E1L49Ff3JReARIi1Ybi.yCQZAxNbwlo2mEMNwXSl9FEXBpW6R3O'),(2,'Daniel','boardgamer','$2b$12$cNeM2oGwM0X/UaD5QbcniOFaLdjPBVwye/hVxgOIs3Sdx9NC/sQEi'),(3,'Daniel','boardgamer','$2b$12$1F8a1P8m2GUR94zulB5MPuz4hbb7ejjBrOLLjI2Vn1Y7VgaFXrprO'),(4,'jan','nanjan','$2b$12$UkgHEosKaAXMmSWXV6qnBe8OG4CVIS6DzFmyo6NvQCBwxdnX7kmtS'),(5,'mob','boss','$2b$12$0162hgjwc0w7h8wtadKhB.mBeQHL6cjlu9tnWCabZb.fUSGiqDQHa'),(6,'john','john','$2b$12$jco3TQS1CHTW6YGKP2bUD.fbFxOYqZ4op4uejchYMsbmuFbGYYJbG'),(7,'bob','bob','$2b$12$y2aECdUP7Nhfzm/lHTaOseAoO09s1khQ.peJhEtrMxpVs0bGVZAYO'),(8,'paul','paul','$2b$12$iEBt9gXvV1oyD1lIH3lTV.ugR5Ljsv1vZu8sNYKky6e7F6H3UOm/q');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-22 13:50:29
