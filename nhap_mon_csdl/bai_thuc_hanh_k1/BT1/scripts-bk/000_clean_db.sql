-- Drop all foreign key constraints
DECLARE @sql NVARCHAR(MAX) = '';

-- Drop foreign keys
SELECT @sql += 'ALTER TABLE [' + s.name + '].[' + t.name + '] DROP CONSTRAINT [' + f.name + '];' + CHAR(13)
FROM sys.foreign_keys f
INNER JOIN sys.tables t ON f.parent_object_id = t.object_id
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id;

EXEC sp_executesql @sql;

-- Drop all tables
SET @sql = '';
SELECT @sql += 'DROP TABLE [' + s.name + '].[' + t.name + '];' + CHAR(13)
FROM sys.tables t
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id;

EXEC sp_executesql @sql;

-- Drop all views
SET @sql = '';
SELECT @sql += 'DROP VIEW [' + s.name + '].[' + v.name + '];' + CHAR(13)
FROM sys.views v
INNER JOIN sys.schemas s ON v.schema_id = s.schema_id;

EXEC sp_executesql @sql;

-- Drop all stored procedures
SET @sql = '';
SELECT @sql += 'DROP PROCEDURE [' + s.name + '].[' + p.name + '];' + CHAR(13)
FROM sys.procedures p
INNER JOIN sys.schemas s ON p.schema_id = s.schema_id;

EXEC sp_executesql @sql;

-- Drop all functions (optional)
SET @sql = '';
SELECT @sql += 'DROP FUNCTION [' + s.name + '].[' + o.name + '];' + CHAR(13)
FROM sys.objects o
INNER JOIN sys.schemas s ON o.schema_id = s.schema_id
WHERE o.type IN ('FN', 'IF', 'TF');  -- Scalar, inline, table-valued

EXEC sp_executesql @sql;

PRINT 'Database cleaned successfully.';
