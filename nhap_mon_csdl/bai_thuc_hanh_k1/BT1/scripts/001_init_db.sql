---TẠO DATABASE QLBH---
CREATE DATABASE QLBH_T4;
GO
---
USE QLBH_T4;
GO
--- TẠO BẢNG
CREATE TABLE KHACHHANG (
	MAKH	char(4) PRIMARY KEY,--Mã khách hàng	
	HOTEN	varchar(40),--Họ tên	
	DCHI	varchar(50),--Địa chỉ	
	SODT	varchar(20),--Số điện thọai	
	NGSINH	smalldatetime,--Ngày sinh	
	DOANHSO	money,--Tổng trị giá các hóa đơn khách hàng đã mua	
	NGDK	smalldatetime,--Ngày đăng ký thành viên	
)
GO
CREATE TABLE NHANVIEN(
	MANV	char(4) PRIMARY KEY,--Mã nhân viên	
	HOTEN	varchar(40),--Họ tên	
	SODT	varchar(20),--Số điện thoại
	NGVL	smalldatetime--Ngày vào làm	
)
GO
CREATE TABLE SANPHAM	(
	MASP	char(4) PRIMARY KEY,--Mã sản phẩm	
	TENSP	varchar(40),--Tên sản phẩm	
	DVT		varchar(20),--Đơn vị tính	
	NUOCSX	varchar(40),--Nước sản xuất	
	GIA		money --Giá bán	
)
GO
CREATE TABLE HOADON	(
	SOHD	int PRIMARY KEY,--Số hóa đơn	
	NGHD	smalldatetime,--Ngày mua hàng	
	MAKH	char(4) REFERENCES KHACHHANG(MAKH),--Mã khách hàng nào mua	
	MANV	char(4) REFERENCES NHANVIEN(MANV),--Nhân viên bán hàng	
	TRIGIA	money--Trị giá hóa đơn	
)
GO
CREATE TABLE CTHD	(
	SOHD	int REFERENCES HOADON(SOHD),--Số hóa đơn	
	MASP	char(4) REFERENCES SANPHAM(MASP),--Mã sản phẩm	
	SL		int,--Số lượng	
	PRIMARY KEY (SOHD, MASP)
)
---THÊM THUỘC TÍNH GHI CHÚ VARCHAR(20)
ALTER TABLE KHACHHANG ADD GHI_CHU VARCHAR(20)
---SỬA THUỘC TÍNH CÓ SẴN VARCHAR(5)
ALTER TABLE KHACHHANG ALTER COLUMN GHI_CHU VARCHAR(50)
ALTER TABLE KHACHHANG ALTER COLUMN MAKH VARCHAR(5)
--XOÁ CỘT
ALTER TABLE KHACHHANG DROP COLUMN GHI_CHU
--- RÀNG BUỘC TOÀN VẸN
--Giá bán của sản phẩm từ 500 đồng trở lên.
ALTER TABLE SANPHAM ADD CONSTRAINT CHK_GIA CHECK(GIA>=500)
INSERT INTO SANPHAM VALUES ('SP01','TEST','CAI','VN',1000) 
INSERT INTO SANPHAM VALUES ('SP02','TEST2','CAI','VN',600) 
SELECT * FROM SANPHAM
--SỐ ĐIỆN THOẠI KHÁCH HÀNG LÀ DUY NHẤT (KHÔNG ĐƯỢC TRÙNG LẮP)
ALTER TABLE NHANVIEN ADD CONSTRAINT UNQ_SDT UNIQUE(SODT)
ALTER TABLE NHANVIEN DROP CONSTRAINT UNQ_SDT 
---
ALTER TABLE KHACHHANG ADD CONSTRAINT UNQ_SDT UNIQUE(SODT)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT) VALUES ('KH01','NGUYEN VAN A','HCM','0987654321') 
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT) VALUES ('KH02','NGUYEN VAN B','HA NOI','0987654322') 
SELECT * FROM KHACHHANG
----INSERT DỮ LIỆU
--ĐỊNH NGHĨA KIỂU NGÀY TÔI NHẬP VÀO
SET DATEFORMAT DMY;
---
INSERT INTO NHANVIEN VALUES('NV01','Nguyen Nhu Nhut','927345678','13/4/2006');
INSERT INTO NHANVIEN VALUES('NV02','Le Thi Phi Yen','987567390','21/4/2006');
INSERT INTO NHANVIEN VALUES('NV03','Nguyen Van B','997047382','27/4/2006');
INSERT INTO NHANVIEN VALUES('NV04','Ngo Thanh Tuan','913758498','24/6/2006');
INSERT INTO NHANVIEN VALUES('NV05','Nguyen Thi Truc Thanh','918590387','20/7/2006');
--LẤY NGÀY HIỆN TẠI HỆ THỐNG
SELECT GETDATE()
--LẤY DỮ LIỆU BẢNG KHÁCH HÀNG RA XEM
SELECT * FROM KHACHHANG
-- XOÁ TOÀN BỘ DỮ LIỆU KHÁCH HÀNG
DELETE FROM KHACHHANG
--AI GIÚP TẠO RA CÂU LÊN INSERT
INSERT INTO KHACHHANG (MAKH, HOTEN, DCHI, SODT, NGSINH, DOANHSO, NGDK) VALUES
('KH01', N'Nguyen Van A', N'731 Tran Hung Dao, Q5, TPHCM', '08823451', '22/10/1960', 13000000, '22/07/2006'),
('KH02', N'Tran Ngoc Han', N'23/5 Nguyen Trai, Q5, TPHCM', '0908256478', '03/04/1974', 280000, '30/07/2006'),
('KH03', N'Tran Ngoc Linh', N'45 Nguyen Canh Chan, Q1, TPHCM', '0938776266', '12/06/1980', 3860000, '05/08/2006'),
('KH04', N'Tran Minh Long', N'50/34 Le Dai Hanh, Q10, TPHCM', '0917325476', '09/03/1965', 250000, '02/10/2006'),
('KH05', N'Le Nhat Minh', N'34 Truong Dinh, Q3, TPHCM', '08246108', '10/03/1950', 21000, '28/10/2006'),
('KH06', N'Le Hoai Thuong', N'227 Nguyen Van Cu, Q5, TPHCM', '08631738', '31/12/1981', 915000, '24/11/2006'),
('KH07', N'Nguyen Van Tam', N'32/3 Tran Binh Trong, Q5, TPHCM', '0916783565', '06/04/1971', 12500, '01/12/2006'),
('KH08', N'Phan Thi Thanh', N'45/2 An Duong Vuong, Q5, TPHCM', '0938435756', '10/11/1971', 365000, '13/12/2006'),
('KH09', N'Le Ha Vinh', N'873 Le Hong Phong, Q5, TPHCM', '08654763', '03/09/1979', 70000, '14/01/2007'),
('KH10', N'Ha Duy Lap', N'34/34B Nguyen Trai, Q1, TPHCM', '08768904', '02/05/1983', 67500, '16/01/2007');
---
INSERT INTO SANPHAM (MASP, TENSP, DVT, NUOCSX, GIA) VALUES
('BC01', N'But chi', N'cay', N'Singapore', 3000),
('BC02', N'But chi', N'cay', N'Singapore', 5000),
('BC03', N'But chi', N'cay', N'Viet Nam', 3500),
('BC04', N'But chi', N'hop', N'Viet Nam', 30000),
('BB01', N'But bi', N'cay', N'Viet Nam', 5000),
('BB02', N'But bi', N'cay', N'Trung Quoc', 7000),
('BB03', N'But bi', N'hop', N'Thai Lan', 100000),
('TV01', N'Tap 100 giay mong', N'quyen', N'Trung Quoc', 2500),
('TV02', N'Tap 200 giay mong', N'quyen', N'Trung Quoc', 4500),
('TV03', N'Tap 100 giay tot', N'quyen', N'Viet Nam', 3000),
('TV04', N'Tap 200 giay tot', N'quyen', N'Viet Nam', 5500),
('TV05', N'Tap 100 trang', N'chuc', N'Viet Nam', 23000),
('TV06', N'Tap 200 trang', N'chuc', N'Viet Nam', 53000),
('TV07', N'Tap 100 trang', N'chuc', N'Trung Quoc', 34000),
('ST01', N'So tay 500 trang', N'quyen', N'Trung Quoc', 40000),
('ST02', N'So tay loai 1', N'quyen', N'Viet Nam', 55000),
('ST03', N'So tay loai 2', N'quyen', N'Viet Nam', 51000),
('ST04', N'So tay', N'quyen', N'Thai Lan', 55000),
('ST05', N'So tay mong', N'quyen', N'Thai Lan', 20000),
('ST06', N'Phan viet bang', N'hop', N'Viet Nam', 5000),
('ST07', N'Phan khong bui', N'hop', N'Viet Nam', 7000),
('ST08', N'Bong bang', N'cai', N'Viet Nam', 1000),
('ST09', N'But long', N'cay', N'Viet Nam', 5000),
('ST10', N'But long', N'cay', N'Trung Quoc', 7000);
----
INSERT INTO HOADON (SOHD, NGHD, MAKH, MANV, TRIGIA) VALUES
('1001', '23/07/2006', 'KH01', 'NV01', 320000),
('1002', '12/08/2006', 'KH01', 'NV02', 840000),
('1003', '23/08/2006', 'KH02', 'NV01', 100000),
('1004', '01/09/2006', 'KH02', 'NV01', 180000),
('1005', '20/10/2006', 'KH01', 'NV02', 3800000),
('1006', '16/10/2006', 'KH01', 'NV03', 2430000),
('1007', '28/10/2006', 'KH03', 'NV03', 510000),
('1008', '28/10/2006', 'KH03', 'NV03', 440000),
('1009', '28/10/2006', 'KH03', 'NV04', 200000),
('1010', '01/11/2006', 'KH01', 'NV01', 5200000),
('1011', '04/11/2006', 'KH04', 'NV03', 250000),
('1012', '30/11/2006', 'KH05', 'NV03', 21000),
('1013', '12/12/2006', 'KH06', 'NV01', 5000),
('1014', '31/12/2006', 'KH03', 'NV02', 3150000),
('1015', '01/01/2007', 'KH06', 'NV01', 910000),
('1016', '01/01/2007', 'KH07', 'NV02', 12500),
('1017', '02/01/2007', 'KH08', 'NV03', 35000),
('1018', '13/01/2007', 'KH08', 'NV03', 330000),
('1019', '13/01/2007', 'KH01', 'NV03', 30000),
('1020', '14/01/2007', 'KH09', 'NV04', 70000),
('1021', '16/01/2007', 'KH10', 'NV03', 67500),
('1022', '16/01/2007', NULL, 'NV03', 7000),
('1023', '17/01/2007', NULL, 'NV01', 330000);
---BẢNG CTHD
INSERT INTO
    CTHD (SOHD, MASP, SL)
VALUES (1001, 'TV02', 10),
    (1001, 'ST01', 5),
    (1001, 'BC01', 5),
    (1001, 'BC02', 10),
    (1001, 'ST08', 10),
    (1002, 'BC04', 20),
    (1002, 'BB01', 20),
    (1002, 'BB02', 20),
    (1003, 'BB03', 10),
    (1004, 'TV01', 20),
    (1004, 'TV02', 10),
    (1004, 'TV03', 10),
    (1004, 'TV04', 10),
    (1005, 'TV05', 50),
    (1005, 'TV06', 50),
    (1006, 'TV07', 20),
    (1006, 'ST01', 30),
    (1006, 'ST02', 10),
    (1007, 'ST03', 10),
    (1008, 'ST04', 8),
    (1009, 'ST05', 10),
    (1010, 'TV07', 50),
    (1010, 'ST07', 50),
    (1010, 'ST08', 100),
    (1010, 'ST04', 50),
    (1010, 'TV03', 100),
    (1011, 'ST06', 50),
    (1012, 'ST07', 3),
    (1013, 'ST08', 5),
    (1014, 'BC02', 80),
    (1014, 'BB02', 100),
    (1014, 'BC04', 60),
    (1014, 'BB01', 50),
    (1015, 'BB02', 30),
    (1015, 'BB03', 7),
    (1016, 'TV01', 5),
    (1017, 'TV02', 1),
    (1017, 'TV03', 1),
    (1017, 'TV04', 6),
    (1018, 'ST04', 8),
    (1019, 'ST05', 1),
    (1019, 'ST06', 2),
    (1019, 'ST07', 10),
    (1020, 'ST08', 5),
    (1021, 'TV01', 7),
    (1021, 'TV02', 10),
    (1022, 'ST07', 1),
    (1023, 'ST04', 6);