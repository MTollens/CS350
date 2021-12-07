-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recipebuddy
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `private` tinyint(1) NOT NULL,
  `measurement_system` varchar(32) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES ('DerickFrito','1357',1,'Metric'),('horickmj','2468',0,'Imperial'),('Matty','54321',0,'Metric'),('maxcolt','12345',1,'Imperial');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appliance`
--

DROP TABLE IF EXISTS `appliance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appliance` (
  `name` varchar(32) NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appliance`
--

LOCK TABLES `appliance` WRITE;
/*!40000 ALTER TABLE `appliance` DISABLE KEYS */;
INSERT INTO `appliance` VALUES ('Blender','Mixer'),('Bowl','Dish'),('Cutting Board',NULL),('Fork','Utensil'),('Hot Mitt',NULL),('Knife','Utensil'),('Ladle','Utensil'),('Pan','Dish'),('Plate','Dish'),('Pot','Dish'),('Spoon','Utensil'),('Stand Mixer','Mixer');
/*!40000 ALTER TABLE `appliance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient` (
  `name` varchar(32) NOT NULL,
  `unit` varchar(32) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES ('Basil','leaf(s)',NULL),('Beef','gram(s)','Protein'),('Bell Pepper','pepper(s)','Vegetable'),('Black Pepper','ml(s)','Spice'),('Broccoli','crown(s)','Vegetable'),('Butter','gram(s)','Dairy'),('Carrot','carrot(s)','Vegetable'),('Cheese','ml(s)','Dairy'),('Chicken','gram(s)','Protein'),('Egg','egg(s)','Protein'),('Flour','ml(s)',NULL),('Garlic','clove(s)','Vegetable'),('Lemon','lemon(s)','Fruit'),('Milk','ml(s)','Dairy'),('Noodles','gram(s)',NULL),('Onion','onion(s)','Vegetable'),('Rice','ml(s)',NULL),('Salt','ml(s)','Spice'),('Sugar','ml(s)','Spice'),('Tomato','tomato(es)','Fruit');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pantry`
--

DROP TABLE IF EXISTS `pantry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pantry` (
  `username` varchar(32) NOT NULL,
  `ingredients` varchar(3200) DEFAULT NULL,
  `appliances` varchar(3200) DEFAULT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `pantry_ibfk_1` FOREIGN KEY (`username`) REFERENCES `account` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pantry`
--

LOCK TABLES `pantry` WRITE;
/*!40000 ALTER TABLE `pantry` DISABLE KEYS */;
/*!40000 ALTER TABLE `pantry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `name` varchar(32) NOT NULL,
  `creator` varchar(32) NOT NULL,
  `ingredients` varchar(3200) NOT NULL,
  `appliances` varchar(3200) NOT NULL,
  `instructions` varchar(3200) NOT NULL,
  `serving_size` int NOT NULL,
  `prep_time` time NOT NULL,
  `tags` varchar(3200) DEFAULT NULL,
  `times_executed` int NOT NULL,
  PRIMARY KEY (`name`,`creator`),
  KEY `creator` (`creator`),
  CONSTRAINT `recipe_ibfk_1` FOREIGN KEY (`creator`) REFERENCES `account` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `username` varchar(32) NOT NULL,
  `recipe_name` varchar(32) NOT NULL,
  `rating` int NOT NULL,
  `comment` varchar(3200) DEFAULT NULL,
  PRIMARY KEY (`username`,`recipe_name`),
  KEY `recipe_name` (`recipe_name`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`username`) REFERENCES `account` (`username`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`recipe_name`) REFERENCES `recipe` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-07 11:55:36
