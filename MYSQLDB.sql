-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.21 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table dream_green.geo_localiser
DROP TABLE IF EXISTS `geo_localiser`;
CREATE TABLE IF NOT EXISTS `geo_localiser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `NOM_COM` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0',
  `INSEE_COM` int NOT NULL DEFAULT '0',
  `INSEE_DEP` int NOT NULL DEFAULT '0',
  `NOM_DEP` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0',
  `INSEE_REG` int NOT NULL DEFAULT '0',
  `Population_legale` int NOT NULL DEFAULT '0',
  `access_digital_interfaces` decimal(10,2) NOT NULL DEFAULT '0.00',
  `access_to_information` decimal(10,2) NOT NULL DEFAULT '0.00',
  `global_access` decimal(10,2) NOT NULL DEFAULT '0.00',
  `administative_skills` decimal(10,2) NOT NULL DEFAULT '0.00',
  `digital_school_skills` decimal(10,2) NOT NULL DEFAULT '0.00',
  `global_competences` decimal(10,2) NOT NULL DEFAULT '0.00',
  `score_global` decimal(10,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`id`),
  KEY `NOM_COM` (`NOM_COM`),
  KEY `INSEE_COM` (`INSEE_COM`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- Dumping data for table dream_green.geo_localiser: ~0 rows (approximately)
/*!40000 ALTER TABLE `geo_localiser` DISABLE KEYS */;
INSERT INTO `geo_localiser` (`id`, `NOM_COM`, `INSEE_COM`, `INSEE_DEP`, `NOM_DEP`, `INSEE_REG`, `Population_legale`, `access_digital_interfaces`, `access_to_information`, `global_access`, `administative_skills`, `digital_school_skills`, `global_competences`, `score_global`) VALUES
	(1, 'Ayguesvives', 31004, 31, 'HAUTE-GARONNE\r\n', 76, 2641, 36.85, 108.82, 67.70, 69.87, 55.18, 62.53, 65.82),
	(2, 'Aureville\r\n', 31025, 31, 'HAUTE-GARONNE\r\n', 76, 875, 28.86, 96.59, 57.89, 56.77, 50.07, 53.42, 56.26),
	(3, 'Auzeville-Tolosane\r\n', 31035, 31, 'HAUTE-GARONNE\r\n', 76, 4161, 26.49, 146.18, 77.78, 141.36, 53.89, 97.63, 85.00),
	(4, 'Auzielle\r\n', 31036, 31, 'HAUTE-GARONNE\r\n', 76, 1446, 34.38, 111.67, 67.51, 72.89, 60.12, 66.50, 67.14),
	(5, 'Baziège\r\n', 31048, 31, 'HAUTE-GARONNE\r\n', 76, 3338, 31.65, 54.88, 41.61, 70.30, 78.95, 74.63, 53.61),
	(6, 'Belberaud\r\n', 31057, 31, 'HAUTE-GARONNE\r\n', 76, 1502, 36.01, 34.13, 35.20, 79.00, 67.00, 73.00, 48.95),
	(7, 'Belbèze-de-Lauragais\r\n', 31058, 31, 'HAUTE-GARONNE\r\n', 76, 121, 34.43, 76.04, 52.26, 55.42, 67.13, 61.28, 55.54),
	(8, 'Castanet-Tolosan\r\n', 31113, 31, 'HAUTE-GARONNE\r\n', 76, 12963, 34.40, 112.04, 67.67, 93.99, 65.56, 79.77, 72.07),
	(9, 'Clermont-le-Fort\r\n', 31148, 31, 'HAUTE-GARONNE\r\n', 76, 512, 33.81, 118.93, 70.29, 101.33, 76.52, 88.93, 77.07),
	(10, 'Corronsac\r\n', 31151, 31, 'HAUTE-GARONNE\r\n', 76, 800, 33.37, 97.20, 60.72, 69.29, 48.48, 58.89, 60.06);
/*!40000 ALTER TABLE `geo_localiser` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
