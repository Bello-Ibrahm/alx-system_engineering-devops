# Steps to changing MySQL password

1. Stop the MySQL service:
```
sudo service mysql stop   # Ubuntu/Debian
sudo systemctl stop mysql # CentOS/RHEL
```

2. Start MySQL in safe mode with privilege bypass:
```
sudo mysqld_safe --skip-grant-tables
```
3. Connect to MySQL:
```
mysql -u root
```
4. Updating the root password:
```
USE mysql;
UPDATE user SET authentication_string=PASSWORD('your_new_password') WHERE User='root';
FLUSH PRIVILEGES;
```
If you get this error:
```
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '('5555') where user='root'' at line 1
```
Try this:
```
USE mysql;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_password';
FLUSH PRIVILEGES;
```
Replace 'your_new_password' with your desired password.

5. Exit the MySQL prompt:
```
quit;
```
6. Start the MySQL service:
```
sudo service mysql start   # Ubuntu/Debian
sudo systemctl start mysql # CentOS/RHEL
```

# Creating and Granting permissions for `holberton_user` User.

```
-- Creates the MySQL server user holberton_user
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost'
IDENTIFIED BY 'projectcorrection280hbtn';

-- To grant all privileges uncomment below
-- GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';

-- Grant permission to show databases
-- GRANT SHOW DATABASES ON *.* TO 'holberton_user'@'localhost';

-- Grant permission to show replica status
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Grant permision on select for all database/tables
GRANT SELECT ON *.* TO 'holberton_user'@'localhost';

-- To remove all privileges uncomment below
-- REVOKE ALL PRIVILEGES ON *.* FROM 'holberton_user'@'localhost';
```


```
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;

USE tyrell_corp;

-- Creates a table called first_table in my current DBU
CREATE TABLE IF NOT EXISTS `nexus6` (`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(256));

INSERT INTO `nexus6`(`name`) VALUES("Leon");
```

Creating and granting permission for the user `replica_user`, with the host name set to %, and can have whatever password.
```
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_pwd';

GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replica_pwd';

-- Binlog Access:
-- GRANT SHOW VIEW ON *.* TO 'replication_user'@'%';

-- Read-Only Access:
-- GRANT SELECT ON *.* TO 'replication_user'@'%';

-- Database-specific Replication:
-- GRANT REPLICATION SLAVE ON your_database.* TO 'replication_user'@'%';

```

