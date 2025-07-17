-- SELECT * FROM CTHD WHERE SL < 1;

ALTER TABLE CTHD ADD CONSTRAINT CK_CTHD_SL CHECK (SL >= 1);

PRINT '(109) Moi lan mua hang, khach hang phai mua it nhat 1 san pham. => DONE';