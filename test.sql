-- Active: 1717176177273@@127.0.0.1@3306@testdb
use testdb;

SELECT * from customer;

SELECT * from student;


CREATE TABLE IF NOT EXISTS `teacher`(
    `id` INTEGER AUTO_INCREMENT,
    `name` VARCHAR(35) NOT NULL,
    `major` VARCHAR(15) NOT NULL,
    `school` VARCHAR(20),
    `university` VARCHAR(20),
    CONSTRAINT teacher_pk PRIMARY KEY (`id`)
);

SHOW TABLES;

SHOW DATABASEs;