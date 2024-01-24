## Creating the MySQL server user and Database:
```
-- Creates the MySQL server user holberton_user
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost'
IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant permission to show replica status
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Grant permision on select
GRANT SELECT ON *.* TO 'holberton_user'@'localhost';

-- Creating Database tyrell_corp
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;

USE tyrell_corp;

-- Creating a table called nexus6 in tyrell_corp db
CREATE TABLE IF NOT EXISTS `nexus6` (`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(256));

-- Inserting records
INSERT INTO `nexus6`(`name`) VALUES("Leon"),("Bello Ibrahim");
```

## Setting up a MySQL replica involves configuring one MySQL server as a replication slave of another MySQL server (the master). 
Below are the general steps to set up a MySQL replication on Ubuntu. 
having two Ubuntu servers, one as the master and the other as the slave.

Before you proceed, make sure that `UFW` is allowing connections on port `3306` (default MySQL port) otherwise replication will not work.

To confirm `ufw` is not blocking port `3306` run this command below:
```
sudo ufw status
```
Output:
```
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
8080                       ALLOW       Anywhere
3306                       ALLOW       Anywhere
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
443/tcp (v6)               ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
8080 (v6)                  ALLOW       Anywhere (v6)
3306 (v6)                  ALLOW       Anywhere (v6)
```
Review the output for a rule that allows incoming connections on port 3306. It should look like the above.

To allow the `ufw` run the command:
```
sudo ufw allow 3306
```
then reload `UFW`:
```
sudo ufw reload
```
Verify MySQL Service:
 Additionally, ensure that your MySQL service is running and listening on port 3306. You can check this using the following command:
```
sudo netstat -plnt | grep 3306
```
Output:
```
tcp6       0      0 :::3306                 :::*                    LISTEN      178396/mysqld
```

Once everything is in order you can begin the steps below:
###  On the Master Server:
1. Open the MySQL configuration file on the master server(to enable binary logging):
```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```
Add the following lines to enable binary logging:
```
server-id            = 1
log_bin              = /var/log/mysql/mysql-bin.log

# name of database to replicate
binlog_do_db    = tyrell_corp
```
Restart the mysql server:
```
sudo service mysql restart
```
2. Create a Replication User (Connect to MySQL and create a user specifically for replication):
``` 
mysql -u root -p
```
```
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_pwd';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replica_pwd';
GRANT SELECT ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
```
3. Get the Binary Log Coordinates (While still in the MySQL shell, note the current binary log file and position):
```
SHOW MASTER STATUS;
```
Similar to this:
```
+------------------+----------+--------------------+------------------+
| File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB |
+------------------+----------+--------------------+------------------+
| mysql-bin.000009 |      107 | tyrell_corp        |                  |
+------------------+----------+--------------------+------------------+
1 row in set (0.00 sec)
```

### On the Slave Server:
1. Open the MySQL configuration file (to enable binary logging and set Server ID):
```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```
Add the following lines:
```
server-id            = 2
relay-log            = /var/log/mysql/mysql-relay-bin.log

# name of database to replicate
binlog_do_db    = tyrell_corp
```
Restart the MySQL Server:
```
sudo service mysql restart
```
2. Connect to MySQL on the slave (Configure Replication):
```
mysql -u root -p
```
Run the following SQL commands:
```
CHANGE MASTER TO
    MASTER_HOST='master_IP_address',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='replica_pwd',
    MASTER_LOG_FILE = 'mysql-bin.000009',
    MASTER_LOG_POS = 107;

    START SLAVE;
```
Replace `master_IP_address`, `replica_user`, `replica_pwd`, `mysql-bin.000009`, and `107` with the appropriate values.

3. Check Replication Status (verify that replication is running without errors):
```
SHOW SLAVE STATUS\G;
```
Look for the `Slave_IO_Running` and `Slave_SQL_Running` values. If both are `Yes`, replication is working.


In order to remove replication user:
```
STOP SLAVE;
RESET SLAVE;
```
Optional command to drop replica user on the slave

```
DROP USER 'replication_user'@'%';
```

## Steps to changes the  MySQL password

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


AUTHOR: Bello Ibrahim
