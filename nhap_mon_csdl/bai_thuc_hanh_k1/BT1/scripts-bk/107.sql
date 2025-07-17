-- SELECT *
-- FROM SANPHAM
-- WHERE
--     DVT NOT IN(
--         'cay',
--         'hop',
--         'cai',
--         'quyen',
--         'chuc'
--     );

ALTER TABLE SANPHAM
ADD CONSTRAINT CK_SANPHAM_DVT CHECK (
    DVT IN (
        'cay',
        'hop',
        'cai',
        'quyen',
        'chuc'
    )
);

PRINT '(107) Don vi tinh cua san pham chi co the la ("cay","hop","cai","quyen","chuc") => DONE';