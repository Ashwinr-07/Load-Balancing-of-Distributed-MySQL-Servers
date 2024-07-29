
# MySQL Load Balancing 

## Overview

This project demonstrates an efficient implementation of load balancing for distributed MySQL databases using NGINX, Docker, and MySQL replication. It aims to optimize database performance, enhance reliability, and improve scalability in high-demand environments.

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies](#technologies)
3. [Architecture](#architecture)
4. [Setup and Installation](#setup-and-installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Performance Testing](#performance-testing)
8. [Conclusion](#conclusion)

## Introduction

Load balancing is crucial for maintaining optimal performance in database systems under high load. This project showcases a practical implementation of MySQL load balancing, utilizing NGINX as a load balancer and Docker for containerization, combined with MySQL's master-slave replication.

## Technologies

- MySQL 8.0
- NGINX
- Docker and Docker Compose
- Python (for testing scripts)

## Architecture

The system consists of:
- 1 MySQL master node
- 2 MySQL slave nodes
- 3 NGINX load balancer

  <img width="608" alt="image" src="https://github.com/user-attachments/assets/3b520386-4d9d-4a7b-bd99-3740c37181a5">


This setup allows for efficient distribution of read queries across all nodes while directing write operations to the master node.

## Setup and Installation

1. Ensure Docker and Docker Compose are installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/Ashwinr-07/Load-Balancing-of-Distributed-MySQL-Servers.git
   ```
3. Navigate to the project directory:
   ```
   cd Load-Balancing-of-Distributed-MySQL-Servers
   ```
4. Launch the containers:
   ```
   docker-compose up -d
   ```

## Configuration

Key configuration files:
- `docker-compose.yaml`: Defines the container setup
- `nginx.conf`: NGINX load balancer configuration
- `master.cnf`: MySQL master node configuration
- `slave1.cnf` and `slave2.cnf`: MySQL slave nodes configuration

## Usage

1. Initialize the master database:
   ```
   docker exec -it mysql-master mysql -uroot -p<password>
   ```
   Execute the following SQL commands to set up the initial database and table:

   ```
   sql
   CREATE DATABASE <DB_NAME>;
   USE <DB_NAME>;
   CREATE TABLE <TABLE_NAME> (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(50)
   );
   INSERT INTO <TABLE_NAME> (name) VALUES ('user1'), ('user2'), ('user3');
   ```

2. Set up replication on the master node:
   ```
   sql
   CREATE USER 'repl'@'%' IDENTIFIED WITH mysql_native_password BY '<replication_password>';
   GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
   FLUSH PRIVILEGES;
   SHOW MASTER STATUS;
   ```
   Note down the Log File name and Position from the output of \`SHOW MASTER STATUS\`.

3. Configure replication on slave nodes:
   ```
   docker exec -it mysql-slave1 mysql -uroot -p<password>
   docker exec -it mysql-slave2 mysql -uroot -p<password>
   ```
   On each slave, execute the following commands:

   ```
   sql
   STOP SLAVE;
   RESET SLAVE ALL;
   CHANGE MASTER TO
     MASTER_HOST='mysql-master',
     MASTER_USER='repl',
     MASTER_PASSWORD='<replication_password>',
     MASTER_LOG_FILE='<log_file_name>',
     MASTER_LOG_POS=<log_position>;
   START SLAVE;
   SHOW SLAVE STATUS\G
   ```
   Replace `<log_file_name>` and `<log_position>` with the values noted from the master node.

4. Verify replication:
   On each slave, run:
   ```
   sql
   SHOW DATABASES;
   USE <DB_NAME>;
   SHOW TABLES;
   SELECT * FROM <TABLE_NAME>;
   ```
   You should see the same data as on the master node.

## Performance Testing

Two Python scripts are provided for testing:
- `insert_data.py`: Generates and inserts sample data into the master database.
- `read_data.py`: Performs read operations through the load balancer to demonstrate query distribution.




## Conclusion

This MySQL load balancing demonstrates a robust solution for enhancing database performance and scalability. By leveraging NGINX, Docker, and MySQL replication, it provides a practical approach to handling increased database loads in various high-demand scenarios.

