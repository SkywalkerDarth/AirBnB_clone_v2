-- this script prepares a MySQL server for the project
-- cretae the project development database with name hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user named: hbnb_dev with all privilages as hbnb_dev_db
-- with the password set to : hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privilages
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
