-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               5.7.29 - MySQL Community Server (GPL)
-- Операционная система:         Win64
-- HeidiSQL Версия:              11.0.0.5958
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Дамп структуры базы данных arzgaz_imp
CREATE DATABASE IF NOT EXISTS `arzgaz_imp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `arzgaz_imp`;

-- Дамп структуры для таблица arzgaz_imp.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.auth_group: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.auth_group_permissions: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.auth_permission: ~28 rows (приблизительно)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add Договор', 1, 'add_dogovor'),
	(2, 'Can change Договор', 1, 'change_dogovor'),
	(3, 'Can delete Договор', 1, 'delete_dogovor'),
	(4, 'Can view Договор', 1, 'view_dogovor'),
	(5, 'Can add log entry', 2, 'add_logentry'),
	(6, 'Can change log entry', 2, 'change_logentry'),
	(7, 'Can delete log entry', 2, 'delete_logentry'),
	(8, 'Can view log entry', 2, 'view_logentry'),
	(9, 'Can add permission', 3, 'add_permission'),
	(10, 'Can change permission', 3, 'change_permission'),
	(11, 'Can delete permission', 3, 'delete_permission'),
	(12, 'Can view permission', 3, 'view_permission'),
	(13, 'Can add group', 4, 'add_group'),
	(14, 'Can change group', 4, 'change_group'),
	(15, 'Can delete group', 4, 'delete_group'),
	(16, 'Can view group', 4, 'view_group'),
	(17, 'Can add user', 5, 'add_user'),
	(18, 'Can change user', 5, 'change_user'),
	(19, 'Can delete user', 5, 'delete_user'),
	(20, 'Can view user', 5, 'view_user'),
	(21, 'Can add content type', 6, 'add_contenttype'),
	(22, 'Can change content type', 6, 'change_contenttype'),
	(23, 'Can delete content type', 6, 'delete_contenttype'),
	(24, 'Can view content type', 6, 'view_contenttype'),
	(25, 'Can add session', 7, 'add_session'),
	(26, 'Can change session', 7, 'change_session'),
	(27, 'Can delete session', 7, 'delete_session'),
	(28, 'Can view session', 7, 'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.auth_user: ~14 rows (приблизительно)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$216000$HzHkMmcGnI0c$tHNHaIvdgUjDBFFClBr4yRUMVnzVdueRtrmr9QV8ttk=', '2021-04-24 15:23:41.314055', 1, 'admin', '', '', '', 1, 1, '2021-02-17 16:45:31.430110'),
	(3, 'pbkdf2_sha256$216000$7ZbkPLLS50gU$xUVm74wtyqTQamtsCdyBIBI/od2wsgyIJjy1Z+8zhJs=', NULL, 0, 'paradox', '', '', '', 0, 1, '2021-04-24 15:24:31.872345'),
	(4, 'pbkdf2_sha256$216000$1Jbteu60MFzi$ACd7ZXYnvuKHnlNgaAMmgSYRqKSqwZiUIe4nfu9kZ0o=', NULL, 0, 'paradoxsev', '', '', '', 0, 1, '2021-04-24 15:25:05.152804'),
	(5, 'pbkdf2_sha256$216000$g1hqqEZarTFv$t5tDoTl2B5Ik3WfU+cDiH29iPKTRVguXJzZjxleinwA=', '2021-04-24 15:37:50.944727', 0, 'sevastopolskaya', '', '', '', 0, 1, '2021-04-24 15:32:31.114728'),
	(6, 'pbkdf2_sha256$216000$bfeYKVLQKNKr$my6qRAGgbgcfh1jq4dbx2r6nq5iDUWH8Exf3VeZY7Qc=', NULL, 0, 'sekretov', '', '', '', 0, 1, '2021-04-24 15:32:53.474902'),
	(7, 'pbkdf2_sha256$216000$xR0SP9snr7ws$ehJEK6IG1Kx3MaPFi0RaCBhiYss4sZk1/PatKeU+nGs=', NULL, 0, 'ashmarina', '', '', '', 0, 1, '2021-04-24 15:33:39.619014'),
	(8, 'pbkdf2_sha256$216000$VsbwfCiROY10$SfZ8SYNjqrSYn03rTOmPxPmMQrjkhoV9AZNB8/5YkD4=', NULL, 0, 'pronin', '', '', '', 0, 1, '2021-04-24 15:33:54.339193'),
	(9, 'pbkdf2_sha256$216000$nKvJQtRkcr4x$9vOrt6uLB3Hau/++mWTGTfhQhaKsOXOGBWHkaxSdrEA=', NULL, 0, 'fizikova', '', '', '', 0, 1, '2021-04-24 15:34:06.222641'),
	(10, 'pbkdf2_sha256$216000$8asYfhbmAtqQ$U/tADf2WnSRIj+2X5x/QB+eyBjfPqQD0lj4j2EuI2Ds=', NULL, 0, 'pisarevskaya', '', '', '', 0, 1, '2021-04-24 15:34:17.883178'),
	(11, 'pbkdf2_sha256$216000$10hGmSeMHLrA$ATVYoaKY5GT+ameThEAyCZ7/KNOT9hOT7KVZxVYsFRc=', NULL, 0, 'tomilina', '', '', '', 0, 1, '2021-04-24 15:34:28.736333'),
	(12, 'pbkdf2_sha256$216000$HdcgfbEKa1JQ$Fbc4bOr/1L0BRmm4bg10JB5JEKXnobfnkiP6zLoDiOo=', NULL, 0, 'alyapiva', '', '', '', 0, 1, '2021-04-24 15:35:16.082000'),
	(13, 'pbkdf2_sha256$216000$gSIEoYaPFrzC$5rKYakHAb8k2uwdv7LwaRFO30ihD14yB2CPtIaqlesc=', NULL, 0, 'konovalova', '', '', '', 0, 1, '2021-04-24 15:35:50.076257'),
	(14, 'pbkdf2_sha256$216000$4V0L5SjQBzIJ$cKYOfkvA2vJmVqvu0a/RSm5h8nOy0somV/WjLS5uNTs=', NULL, 0, 'zubenko', '', '', '', 0, 1, '2021-04-24 15:36:08.076010'),
	(15, 'pbkdf2_sha256$216000$67Yuiyg4eKvA$mH0IksIDPEvlxGkkMqx1pHrWj1vMjJZPRVEKUxwKJuc=', NULL, 0, 'savina', '', '', '', 0, 1, '2021-04-24 15:36:21.313359');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.auth_user_groups: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.auth_user_user_permissions: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.django_admin_log: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.django_content_type: ~11 rows (приблизительно)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(2, 'admin', 'logentry'),
	(4, 'auth', 'group'),
	(3, 'auth', 'permission'),
	(5, 'auth', 'user'),
	(6, 'contenttypes', 'contenttype'),
	(1, 'dogovor', 'dogovor'),
	(9, 'dogovor', 'notification'),
	(11, 'dogovor', 'order'),
	(8, 'dogovor', 'payment'),
	(10, 'dogovor', 'worker'),
	(7, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.django_migrations: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.django_session: ~10 rows (приблизительно)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('6kxa4ikskt6zs69uk8ikvlyut1dlpefo', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lZzXn:j3uyabvt0mpooDMBYrOq9krdw3Ux-XyFd0MQxE2X2Fs', '2021-05-07 20:24:43.521058'),
	('aao4frfedvgfmy8q9xnop8g0yun7rp54', 'e30:1lD0oE:wXTMtXsGXAMxbkG8NVwDEqdUHAsk3vAE5K7M71nseSw', '2021-03-05 11:06:42.463619'),
	('glsnc1xbwgryhhhbuvjbcgl24sgu3hp1', 'e30:1lD0nI:-FHtYePvm_jvke3bhbPagfkevcaaotxkpewwxVxsyhk', '2021-03-05 11:05:44.339218'),
	('hyv0offx8r7dkiw4pqa35norv5tdgvn1', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lD0u4:0QxMfPaS8RSCIwnMjJnwOfhGX5P51jLhlV1EocFAMgY', '2021-03-05 11:12:44.462789'),
	('liepero5v4is09l768mj9n33d5fyqhty', '.eJxVjEEOwiAQRe_C2hAKBRmX7j0DGZhBqgaS0q6Md7dNutDtf-_9twi4LiWsnecwkbgIK06_W8T05LoDemC9N5laXeYpyl2RB-3y1ohf18P9OyjYy1ZnQ-TzCJ55BMygkQcHVhGwSTr5c1TGAilUkCgrrb1nl5mdH_QWOfH5Av05OC8:1laHXi:lkGa86shYXyjuRiFtYVyuJoKnC-oeuql7LpzgRHyZfI', '2021-05-08 15:37:50.947787'),
	('nu2swbnokr2menhjsptlwcwso03krpaf', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lWuZD:I5A3ccVwSGfo46vb8oZk2Sr9-ZnsOCC8LV_bd0Ff_-M', '2021-04-29 08:29:27.930988'),
	('ovev4mr0dyhth62930peuio2npa97trf', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lWuZm:QgHWTq4vvmRBu2KlcKqcEKh7EJMwXHPvdcGlebB-_Yk', '2021-04-29 08:30:02.060901'),
	('qp4emnyyqdbgn6kswqg67p4r5mp5l1s2', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lP2yF:1w-babAbzO40bOCRr7T3b2WXq3jNFLj74EhziH0kS9Y', '2021-04-07 15:50:47.164005'),
	('rccd1bq2jmw39a2f265ossmqr81k66ue', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lWGqT:IwJL0DTpY_wP0UNY35k4GkkxVvaYVhURZ41QdwKWsVQ', '2021-04-27 14:04:37.222923'),
	('wbmleeg6m8mncoxolvncpncmeq3cdr1e', '.eJxVjEEOwiAQRe_C2pABWoZx6b5nIAOMtmpKUtqV8e7apAvd_vfef6nI2zrGrckSp6LOyqjT75Y4P2TeQbnzfKs613ldpqR3RR-06aEWeV4O9-9g5DZ-60weAtrUgRjPxiTohUtGf0UomQjBEgawvTckDjrnySMChJKsYyH1_gC77zaI:1lJZW3:jTfP6T02wcactijlybO8xhDneUIWWG7-JYUAVqLz6Ks', '2021-03-23 13:23:03.832642');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.dogovor_dogovor
CREATE TABLE IF NOT EXISTS `dogovor_dogovor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `number` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `tel1` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `tel2` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `tel3` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fiz` tinyint(1) NOT NULL,
  `address_city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address_street` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address_house` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address_kv` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `equip` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sum` int(11) NOT NULL,
  `discount` int(11) NOT NULL DEFAULT '0',
  `amount` int(11) NOT NULL,
  `comment` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_old` int(11) DEFAULT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `created_by_id` int(11) NOT NULL,
  `create_time` datetime(6),
  `update_time` datetime(6),
  PRIMARY KEY (`id`),
  KEY `dogovor_dogovor_created_by_id_47c8f1ea_fk_auth_user_id` (`created_by_id`),
  CONSTRAINT `dogovor_dogovor_created_by_id_47c8f1ea_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.dogovor_dogovor: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `dogovor_dogovor` DISABLE KEYS */;
/*!40000 ALTER TABLE `dogovor_dogovor` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.dogovor_notification
CREATE TABLE IF NOT EXISTS `dogovor_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notify_type` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dogovor_id_id` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `send_time_1` datetime(6) DEFAULT NULL,
  `success_1` tinyint(1) NOT NULL DEFAULT '0',
  `send_time_2` datetime(6) DEFAULT NULL,
  `success_2` tinyint(1) NOT NULL DEFAULT '0',
  `comment` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dogovor_notification_dogovor_id_id_2f170a25_fk_dogovor_d` (`dogovor_id_id`),
  CONSTRAINT `dogovor_notification_dogovor_id_id_2f170a25_fk_dogovor_d` FOREIGN KEY (`dogovor_id_id`) REFERENCES `dogovor_dogovor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.dogovor_notification: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `dogovor_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `dogovor_notification` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.dogovor_order
CREATE TABLE IF NOT EXISTS `dogovor_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tel` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `job` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `comment` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `completed` tinyint(1) NOT NULL,
  `dogovor_id_id` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dogovor_order_dogovor_id_id_0dc00793_fk_dogovor_dogovor_id` (`dogovor_id_id`),
  KEY `dogovor_order_worker_id_ad6422d8_fk_dogovor_worker_id` (`worker_id`),
  CONSTRAINT `dogovor_order_dogovor_id_id_0dc00793_fk_dogovor_dogovor_id` FOREIGN KEY (`dogovor_id_id`) REFERENCES `dogovor_dogovor` (`id`),
  CONSTRAINT `dogovor_order_worker_id_ad6422d8_fk_dogovor_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `dogovor_worker` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.dogovor_order: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `dogovor_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `dogovor_order` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.dogovor_payment
CREATE TABLE IF NOT EXISTS `dogovor_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pay_type` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  `amount` int(11) NOT NULL,
  `pay_place` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dogovor_id_id` int(11) NOT NULL,
  `comment` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT '',
  `create_time` datetime(6),
  `created_by_id` int(11) NOT NULL,
  `update_time` datetime(6),
  PRIMARY KEY (`id`),
  KEY `dogovor_payment_dogovor_id_id_d3451f72_fk_dogovor_dogovor_id` (`dogovor_id_id`),
  KEY `dogovor_payment_created_by_id_b024a3f2_fk_auth_user_id` (`created_by_id`),
  CONSTRAINT `dogovor_payment_created_by_id_b024a3f2_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `dogovor_payment_dogovor_id_id_d3451f72_fk_dogovor_dogovor_id` FOREIGN KEY (`dogovor_id_id`) REFERENCES `dogovor_dogovor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.dogovor_payment: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `dogovor_payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `dogovor_payment` ENABLE KEYS */;

-- Дамп структуры для таблица arzgaz_imp.dogovor_worker
CREATE TABLE IF NOT EXISTS `dogovor_worker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `func` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дамп данных таблицы arzgaz_imp.dogovor_worker: ~16 rows (приблизительно)
/*!40000 ALTER TABLE `dogovor_worker` DISABLE KEYS */;
INSERT INTO `dogovor_worker` (`id`, `name`, `func`, `description`) VALUES
	(1, 'Тарасов', 'обходчик', NULL),
	(2, 'Автаева', 'обходчик', NULL),
	(3, 'Акимова', 'обходчик', NULL),
	(4, 'Анфимова', 'обходчик', NULL),
	(5, 'Авдеев', 'обходчик', NULL),
	(6, 'Акулов', 'обходчик', NULL),
	(7, 'Бурцев', 'обходчик', NULL),
	(8, 'Ванюшин', 'обходчик', NULL),
	(9, 'Грачева', 'обходчик', NULL),
	(10, 'Горбунов', 'обходчик', NULL),
	(11, 'Голубев', 'обходчик', NULL),
	(12, 'Гринина', 'обходчик', NULL),
	(13, 'Гусев', 'обходчик', NULL),
	(14, 'Зюзин', 'обходчик', NULL),
	(15, 'Капранов', 'обходчик', NULL),
	(16, 'Каравашкин', 'обходчик', NULL),
	(17, 'Квадеев', 'обходчик', NULL),
	(18, 'Князев', 'обходчик', NULL),
	(19, 'Кротова', 'обходчик', NULL),
	(20, 'Ковалев', 'обходчик', NULL),
	(21, 'Козлов', 'обходчик', NULL),
	(22, 'Конев', 'обходчик', NULL),
	(23, 'Кочнев', 'обходчик', NULL),
	(24, 'Кучин', 'обходчик', NULL),
	(25, 'Куксин', 'обходчик', NULL),
	(26, 'Лаптев', 'обходчик', NULL),
	(27, 'Лашин', 'обходчик', NULL),
	(28, 'Малафейкин', 'обходчик', NULL),
	(29, 'Маслов', 'обходчик', NULL),
	(30, 'Морозова', 'обходчик', NULL),
	(31, 'Мякин', 'обходчик', NULL),
	(32, 'Марин', 'обходчик', NULL),
	(33, 'Недорезов', 'обходчик', NULL),
	(34, 'Олейник', 'обходчик', NULL),
	(35, 'Олихвер', 'обходчик', NULL),
	(36, 'Орешин', 'обходчик', NULL),
	(37, 'Перевезенцев', 'обходчик', NULL),
	(38, 'Перетрутов', 'обходчик', NULL),
	(39, 'Прибыткина', 'обходчик', NULL),
	(40, 'Русин', 'обходчик', NULL),
	(41, 'Русакова', 'обходчик', NULL),
	(42, 'Секретов', 'обходчик', NULL),
	(43, 'Соганов', 'обходчик', NULL),
	(44, 'Спирина', 'обходчик', NULL),
	(45, 'Сысоев', 'обходчик', NULL),
	(46, 'Швецов', 'обходчик', NULL),
	(47, 'Ширкин', 'обходчик', NULL),
	(48, 'Шляндина', 'обходчик', NULL),
	(49, 'Ежков', 'обходчик', NULL),
	(50, 'Юматов', 'обходчик', NULL),
	(51, 'Шорохов', 'обходчик', NULL),
	(52, 'Слесарь', 'слесарь', NULL);
/*!40000 ALTER TABLE `dogovor_worker` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
