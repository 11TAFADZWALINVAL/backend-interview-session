

if db_id('backendsql') is null -- Create a new database called 'backendsql'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = 'backendsql'

)
CREATE DATABASE backendsql
GO
-- Create a new table called 'Area' in schema 'backendsql'
-- Drop the table if it already exists
IF OBJECT_ID('backendsql.Area', 'U') IS NOT NULL
DROP TABLE backendsql.Area
GO
-- Create the table in the specified schema
CREATE TABLE Area
(
    AreaId INT NOT NULL PRIMARY KEY, -- primary key column
   AreaName [NVARCHAR](50) NOT NULL,
   Province [NVARCHAR](50) NOT NULL,
   District [NVARCHAR](50) NOT NULL,
   City [NVARCHAR](50) NOT NULL,
   ShopId [NVARCHAR](50) NOT NULL,
    
    
);
GO


--sql duerry to insert the area into the db

-- Insert rows into table 'Area'
INSERT INTO Area
( -- columns to insert data into
 [AreaId], [AreaName], [Province],[District],[City],[ShopId]
)
VALUES
( -- first row: values for the columns in the list above
 newid(), 'CBD', 'HARARE','HARARE CENTRAL','HARARE',newid()
)
-- add more rows here
GO