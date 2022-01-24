-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.31 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for face
DROP DATABASE IF EXISTS `face`;
CREATE DATABASE IF NOT EXISTS `face` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `face`;

-- Dumping structure for table face.attendance
DROP TABLE IF EXISTS `attendance`;
CREATE TABLE IF NOT EXISTS `attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` text,
  `cam_id` int(11) DEFAULT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=98 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table face.cameras
DROP TABLE IF EXISTS `cameras`;
CREATE TABLE IF NOT EXISTS `cameras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `main` text,
  `sub` text,
  `type` text,
  `status` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for procedure face.getAttendance
DROP PROCEDURE IF EXISTS `getAttendance`;
DELIMITER //
CREATE PROCEDURE `getAttendance`(
	IN `cid` INT
)
BEGIN
SELECT c.`type`,u.name, a.*,CONVERT(DATE_FORMAT(a.time,'%Y-%m-%d-%H:%i'),DATETIME) AS minutes FROM attendance a 
INNER JOIN userdata u ON u.id = a.uid
INNER JOIN cameras c ON c.id=a.cam_id
WHERE a.cam_id=cid
group BY minutes;

END//
DELIMITER ;

-- Dumping structure for table face.userdata
DROP TABLE IF EXISTS `userdata`;
CREATE TABLE IF NOT EXISTS `userdata` (
  `id` tinytext,
  `name` tinytext,
  `encoding` blob,
  `status` int(11) NOT NULL DEFAULT '0',
  `photo` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
