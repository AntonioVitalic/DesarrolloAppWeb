-- MySQL dump 10.13  Distrib 8.0.22, for osx10.16 (x86_64)
--
-- Host: localhost    Database: ejemplo
-- ------------------------------------------------------
-- Server version	8.0.11

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
-- Table structure for table `visitas`
--

DROP TABLE IF EXISTS `visitas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitas` (
  `pais` varchar(2) NOT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitas`
--

LOCK TABLES `visitas` WRITE;
/*!40000 ALTER TABLE `visitas` DISABLE KEYS */;
INSERT INTO `visitas` VALUES ('ad',7),('ae',2),('af',14),('ag',2),('am',1),('an',2),('ar',1970),('at',25),('au',86),('bb',1),('be',51),('bg',59),('bm',24),('bo',25),('br',327),('bs',11),('by',1),('bz',3),('ca',138),('cg',2),('ch',334),('cl',5821),('cn',372),('co',198),('cr',12),('cx',17),('cy',6),('cz',36),('de',653),('dk',73),('do',9),('ec',37),('ee',46),('eg',1),('es',539),('eu',6),('fi',20),('fk',2),('fr',479),('gb',492),('ge',4),('gi',5),('gq',1),('gt',5),('hk',23),('hn',12),('hu',6),('ie',39),('il',15),('im',1),('in',11),('it',90),('je',1),('jp',43),('kh',1),('kp',1),('kr',10),('ky',4),('kz',1),('lb',2),('li',6),('lk',2),('lt',5),('lu',55),('lv',5),('ma',1),('mc',1),('mt',161),('mu',1),('mx',279),('my',1),('na',1),('ne',2),('nl',325),('no',38),('nz',21),('pa',17),('pe',220),('pl',11),('pt',10),('py',6),('ro',16),('ru',35),('sa',1),('se',144),('sg',170),('si',2),('sk',9),('sn',3),('sv',3),('sz',8),('td',19),('th',1),('tr',5),('ua',2),('uk',169),('us',3003),('uy',174),('ve',102),('vg',12),('vn',1),('za',40),('zm',2),('zw',1);
/*!40000 ALTER TABLE `visitas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-09 10:44:22
