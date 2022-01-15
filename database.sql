CREATE TABLE `userdata` (
	`id` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`name` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`encoding` BLOB NULL DEFAULT NULL,
	`status` INT(11) NOT NULL DEFAULT '0',
	`photo` TEXT NOT NULL COLLATE 'latin1_swedish_ci'
)
COLLATE='latin1_swedish_ci'
ENGINE=MyISAM
;

---
CREATE TABLE `cameras` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`name` TEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`main` TEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`sub` TEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`type` TEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`status` INT(11) NULL DEFAULT '0',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=MyISAM
AUTO_INCREMENT=10
;
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (1, 'camera 1', ' rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/101', ' rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/102', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (2, 'camera 2', ' rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/201', ' rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/202', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (3, 'camera 3', ' rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/301', ' rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/302', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (4, 'camera 4', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/401', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/402', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (5, 'camera 5', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/501', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/502', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (6, 'camera 6', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/601', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/602', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (7, 'camera 7', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/701', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/702', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (8, 'camera 8', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/801', 'rtsp://admin:wnet5000@66clinton.wnetworking.com:554/Streaming/Channels/802', 'in', 0);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (9, 'test', 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov', 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov', 'in', 1);
INSERT INTO `cameras` (`id`, `name`, `main`, `sub`, `type`, `status`) VALUES (10, 'webcam', '0', '0', 'in', 1);


---
