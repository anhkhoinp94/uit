-- SELECT H.*
-- FROM HOADON H
--     JOIN NHANVIEN N ON H.MANV = N.MANV
-- WHERE
--     H.NGHD < N.NGVL;

-- CREATE TRIGGER trg_Check_NGHD_vs_NGVL
-- ON HOADON
-- AFTER INSERT, UPDATE
-- AS
-- BEGIN
--     IF EXISTS (
--         SELECT 1
--         FROM HOADON H
--         JOIN NHANVIEN N ON H.MANV = N.MANV
--         WHERE H.NGHD < N.NGVL
--               AND EXISTS (
--                   SELECT 1 FROM inserted i
--                   WHERE i.SOHD = H.SOHD
--               )
--     )
--     BEGIN
--         RAISERROR ('Ngày bán hàng (NGHD) không được trước ngày nhân viên vào làm (NGVL).', 16, 1);
--         ROLLBACK TRANSACTION;
--     END
-- END;
-- GO

PRINT '(112) Ngay ban hang (NGHD) cua mot nhan vien phai lon hon hoac bang ngay nhan vien do vao lam. => PENDING';