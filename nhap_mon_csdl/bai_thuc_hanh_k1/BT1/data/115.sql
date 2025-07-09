-- CREATE TRIGGER trg_Update_DOANHSO
-- ON HOADON
-- AFTER INSERT, UPDATE, DELETE
-- AS
-- BEGIN
--     -- Cập nhật doanh số cho các khách hàng bị ảnh hưởng
--     UPDATE KHACHHANG
--     SET DOANHSO = (
--         SELECT SUM(TRIGIA)
--         FROM HOADON H
--         WHERE H.MAKH = KHACHHANG.MAKH
--     )
--     WHERE MAKH IN (
--         SELECT MAKH FROM inserted
--         UNION
--         SELECT MAKH FROM deleted
--     );
-- END;
-- GO

-- SELECT KH.MAKH, KH.HOTEN, KH.DOANHSO, (
--         SELECT SUM(H.TRIGIA)
--         FROM HOADON H
--         WHERE
--             H.MAKH = KH.MAKH
--     ) AS TONG_TINH_TOAN
-- FROM KHACHHANG KH;

PRINT '(115) Doanh so cua mot khach hang la tong tri gia cac hoa don ma khach hang thanh vien do da mua. => PENDING';