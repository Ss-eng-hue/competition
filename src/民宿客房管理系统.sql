/*
SQLyog v10.2 
MySQL - 5.7.35-log : Database - 民宿客房管理系统
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`民宿客房管理系统` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `民宿客房管理系统`;

/*Table structure for table `住房记录` */

DROP TABLE IF EXISTS `住房记录`;

CREATE TABLE `住房记录` (
  `房号` varchar(10) DEFAULT NULL,
  `姓名` varchar(20) DEFAULT NULL,
  `性别` varchar(5) DEFAULT NULL,
  `身份证号` varchar(20) NOT NULL,
  `联系方式` varchar(20) DEFAULT NULL,
  `入住时间` varchar(20) DEFAULT NULL,
  `退房时间` varchar(20) DEFAULT NULL,
  `房间类型` varchar(20) DEFAULT NULL,
  `住房天数` int(10) DEFAULT NULL,
  `消费` int(10) DEFAULT NULL,
  `籍贯` varchar(20) DEFAULT NULL,
  `前台` varchar(20) DEFAULT '13115925968',
  PRIMARY KEY (`身份证号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `住房记录` */

insert  into `住房记录`(`房号`,`姓名`,`性别`,`身份证号`,`联系方式`,`入住时间`,`退房时间`,`房间类型`,`住房天数`,`消费`,`籍贯`,`前台`) values ('1008','郑十','女','0000000000','10111111111','2021-11-27','2021-11-28','单人间',1,130,'天津市','13115925968'),('1003','刘一','女','1111111111','11111111111','2021-11-24','2021-11-26','大床房',2,360,'山西省','13115925968'),('1002','陈二','女','2222222222','12111111111','2021-11-24','2021-11-26','双人间',2,210,'云南省','13115925968'),('1002','张三','男','3333333333','13111111111','2021-11-20','2021-11-21','双人间',1,160,'福建省','13115925968'),('1001','李四','男','4444444444','14111111111','2021-11-21','2021-11-22','双人间',1,160,'福建省','13115925968'),('1004','王五','女','5555555555','15111111111','2021-11-25','2021-11-26','单人间',1,130,'黑龙江省','13115925968'),('1005','赵六','女','6666666666','16111111111','2021-11-24','2021-11-25','双人间',1,160,'甘肃省 ','13115925968'),('1005','孙七','男','7777777777','17111111111','2021-11-24','2021-11-25','双人间',1,160,'甘肃省 ','13115925968'),('1006','周八','男','8888888888','18111111111','2021-11-26','2021-11-27','豪华套间',1,210,'贵州省','13115925968'),('1007','吴九','女','9999999999','19111111111','2021-11-27','2021-11-28','商务套间',1,260,'青海省','13115925968');

/*Table structure for table `入住信息` */

DROP TABLE IF EXISTS `入住信息`;

CREATE TABLE `入住信息` (
  `入住时间` varchar(20) DEFAULT NULL,
  `房号` varchar(10) DEFAULT NULL,
  `退房时间` varchar(20) DEFAULT NULL,
  `身份证号` varbinary(20) NOT NULL,
  PRIMARY KEY (`身份证号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `入住信息` */

insert  into `入住信息`(`入住时间`,`房号`,`退房时间`,`身份证号`) values ('2021-11-27','1008','2021-11-28','0000000000'),('2021-11-24','1003','2021-11-26','1111111111'),('2021-11-24','1002','2021-11-26','2222222222'),('2021-11-20','1002','2021-11-21','3333333333'),('2021-11-21','1001','2021-11-22','4444444444'),('2021-11-25','1004','2021-11-26','5555555555'),('2021-11-24','1005','2021-11-25','6666666666'),('2021-11-24','1005','2021-11-25','7777777777'),('2021-11-26','1006','2021-11-27','8888888888'),('2021-11-27','1007','2021-11-28','9999999999');

/*Table structure for table `客户` */

DROP TABLE IF EXISTS `客户`;

CREATE TABLE `客户` (
  `姓名` varchar(20) NOT NULL,
  `性别` varchar(5) DEFAULT NULL,
  `身份证号` varchar(20) NOT NULL,
  `籍贯` varchar(10) DEFAULT NULL,
  `联系方式` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`身份证号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `客户` */

insert  into `客户`(`姓名`,`性别`,`身份证号`,`籍贯`,`联系方式`) values ('郑十','女','0000000000','天津市','10111111111'),('刘一','女','1111111111','山西省','11111111111'),('陈二','女','2222222222','云南省','12111111111'),('张三','男','3333333333','福建省','13111111111'),('李四','男','4444444444','福建省','14111111111'),('王五','女','5555555555','黑龙江省','15111111111'),('赵六','女','6666666666','甘肃省 ','16111111111'),('孙七','男','7777777777','甘肃省 ','17111111111'),('周八','男','8888888888','贵州省','18111111111'),('吴九','女','9999999999','青海省','19111111111');

/*Table structure for table `客房` */

DROP TABLE IF EXISTS `客房`;

CREATE TABLE `客房` (
  `房号` varchar(10) NOT NULL,
  `类型` varchar(10) DEFAULT NULL,
  `房价` int(10) DEFAULT NULL,
  PRIMARY KEY (`房号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `客房` */

insert  into `客房`(`房号`,`类型`,`房价`) values ('1001','单人间',130),('1002','单人间',130),('1003','大床房',180),('1004','双人间',160),('1005','双人间',160),('1006','大床房',180),('1007','豪华套间',210),('1008','商务套间',260),('1009','单人间',130),('1010','总统套房',360);

/*Table structure for table `管理员` */

DROP TABLE IF EXISTS `管理员`;

CREATE TABLE `管理员` (
  `序列` int(5) NOT NULL AUTO_INCREMENT,
  `账号` varchar(20) NOT NULL,
  `密码` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`账号`),
  KEY `序列` (`序列`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `管理员` */

insert  into `管理员`(`序列`,`账号`,`密码`) values (1,'admin','123456');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
