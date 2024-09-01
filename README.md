# Cars Details Database

This repository contains the SQL dump of the `cars_details` database. The data was sourced from Kaggle and is structured according to an Entity-Relationship Diagram (ERD) included in the repository. The database is managed using PostgreSQL.
## Dataset URL
[Used Cars Details Dataset (kaggle.com)](https://www.kaggle.com/datasets/rakkesharv/used-cars-detailed-dataset)

## Entity-Relationship Diagram
[ERD diagram](https://ibb.co/k4jdVHB)


## Prerequisites

Before you begin, ensure you have the following installed:
- PostgreSQL (Version 12.0 or newer recommended)
- pgAdmin 4 (or another PostgreSQL client)
- Python 3.8 or newer
- pip (Python package installer)

## Installation Guide

### 1. Clone the Repository

Start by cloning this repository to your local machine using:

```bash
git clone https://github.com/TuringCollegeSubmissions/martstelm-DE1.v2.2.5.git
cd martstelm-DE1.v2.2.5
```
### 2. Set Up Python Environment
Install the necessary Python packages using pip:
```bash
pip install sqlalchemy
```

### 3. Create database

Then, create a new database in PostgreSQL:
```sql
CREATE DATABASE cars_details;
```
### 4. Configure Environment Variables
Create a .env file in the src directory of your project and add the following environment variables to configure your database connection:

```bash
cd src/
```
```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
```
### 5. Run application
Copy csv file into src folder and run python application
```bash
python main.py
```
Or if you want just dump sql file, you can find it in repository and insert like this:
```bash
psql -U [USERNAME] -d cars_details -f path_to_your_sql_dump_file.sql
```
### 6. Verify the Import
To verify that the data has been imported successfully, you can run the following SQL query:
```sql
SELECT * 
FROM public.all_car_data
LIMIT 10;
```
## Usage

You can now use pgAdmin or any other PostgreSQL client to connect to the `cars_details` database and run queries, generate reports, or perform analysis.

