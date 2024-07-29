# MySQL Load Balancing using NGINX

## Overview

This is an efficient implementation of load balancing for distributed MySQL databases using NGINX, Docker, and MySQL replication. It aims to optimize database performance, enhance reliability, and improve scalability in high-demand environments.

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies](#technologies)
3. [Architecture](#architecture)
4. [Setup and Installation](#setup-and-installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Performance Testing](#performance-testing)
8. [Use Cases](#use-cases)
9. [Learning Outcomes](#learning-outcomes)
10. [Conclusion](#conclusion)

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
- 1 NGINX load balancer

This setup allows for efficient distribution of read queries across all nodes while directing write operations to the master node.

## Setup and Installation

1. Ensure Docker and Docker Compose are installed on your system.
2. Clone the repository:
