ALTER TABLE KHACHHANG
ADD CONSTRAINT CK_NGDK_NGSINH CHECK (NGDK > NGSINH);

PRINT '(110) Ngay khach hang dang ky la khach hang thanh vien phai lon hon ngay sinh cua nguoi do. => DONE';