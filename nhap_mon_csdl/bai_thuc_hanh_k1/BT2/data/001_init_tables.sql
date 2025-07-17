PRINT 'Creating tables...';

CREATE TABLE KHOA (
    MAKHOA varchar(4) PRIMARY KEY,
    TENKHOA varchar(40),
    NGTLAP smalldatetime,
    TRGKHOA char(4)
);

CREATE TABLE MONHOC (
    MAMH varchar(10) PRIMARY KEY,
    TENMH varchar(40),
    TCLT tinyint,
    TCTH tinyint,
    MAKHOA varchar(4),
);

CREATE TABLE DIEUKIEN (
    MAMH varchar(10),
    MAMH_TRUOC varchar(10)
);

CREATE TABLE GIAOVIEN (
    MAGV char(4) PRIMARY KEY,
    HOTEN varchar(40),
    HOCVI varchar(10),
    HOCHAM varchar(10),
    GIOITINH varchar(3),
    NGSINH smalldatetime,
    NGVL smalldatetime,
    HESO numeric(4, 2),
    MUCLUONG money,
    MAKHOA varchar(4)
);

CREATE TABLE LOP (
    MALOP char(3) PRIMARY KEY,
    TENLOP varchar(40),
    TRGLOP char(5),
    SISO tinyint,
    MAGVCN char(4)
);

CREATE TABLE HOCVIEN (
    MAHV char(5) PRIMARY KEY,
    HO varchar(40),
    TEN varchar(10),
    NGSINH smalldatetime,
    GIOITINH varchar(3),
    NOISINH varchar(40),
    MALOP char(3)
);

CREATE TABLE GIANGDAY (
    MALOP char(3),
    MAMH varchar(10),
    MAGV char(4),
    HOCKY tinyint,
    NAM smallint,
    TUNGAY,
    DENNGAY smalldatetime
);

CREATE TABLE KETQUATHI (
    MAHV char(5),
    MAMH varchar(10),
    LANTHI tinyint,
    NGTHI smalldatetime,
    DIEM numeric(4, 2),
    KQUA varchar(10)
);