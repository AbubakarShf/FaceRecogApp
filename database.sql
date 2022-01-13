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
