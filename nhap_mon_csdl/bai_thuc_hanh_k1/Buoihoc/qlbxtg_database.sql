CREATE DATABASE QLBXMTG;

USE QLBXMTG;

CREATE TABLE KHACHHANG (
    MAKH char(4) PRIMARY KEY,
    TENKH varchar(40),
    NGAYSINH smalldatetime,
    DIACHI varchar(50),
    CMND varchar(20),
)

CREATE TABLE LOAIXE (
    MALX char(4) PRIMARY KEY,
    TENLX varchar(20),
    CONGNGHE varchar(20)
)

CREATE TABLE XEMAY (
    MAXM char(4) PRIMARY KEY,
    TENXM varchar(20),
    MALX char(4) REFERENCES LOAIXE (MALX),
    NAMSX int,
    TRONGLUONG int,
    GIA money
)

CREATE TABLE LOAIHINHTRAGOP (
    MALH char(4) PRIMARY KEY,
    TENLH varchar(20),
    PHANTRAMTT float,
    KYHAN int,
    LAIXUAT float,
    PHITHUHO float,
)

CREATE TABLE TRAGOP (
    MATG char(4) PRIMARY KEY,
    MAXM char(4) REFERENCES XEMAY (MAXM),
    MAKH char(4) REFERENCES KHACHHANG (MAKH),
    NGAYMUA smalldatetime,
    SOTIENTT float,
    MALH char(4) REFERENCES LOAIHINHTRAGOP (MALH),
)
