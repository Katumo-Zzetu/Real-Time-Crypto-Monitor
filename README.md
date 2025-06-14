# Real-Time-Crypto-Monitor
Extract, Transform, and Load Crypto Data and monitor using Grafana

# Crypto Real-Time Data Pipeline

## Overview
This repository provides two core scripts for **real-time cryptocurrency data processing**:
1. **Extraction script (`extract.py`)** – Collects crypto prices via **Coinbase WebSocket** and stores them in **PostgreSQL**.
2. **Transformation script (`transform.py`)** – Uses **Apache Spark** to clean and format data, preparing it for **Grafana visualization**.

## Features
✅ **Live crypto price updates** (BTC, ETH, LTC, and more).
✅ **PostgreSQL storage** for historical tracking.
✅ **Data cleaning with Apache Spark** for structured analytics.
✅ **Optimized output** for **Grafana dashboards**.

## Setup Instructions
### 1️⃣ Install Dependencies
Ensure Python and Spark are installed, then run:
```bash
pip install asyncio websockets psycopg2 pyspark
```

### 2️⃣ Configure PostgreSQL
#### Create the Database
```sql
CREATE DATABASE crypto_realtime;
```

#### Create the Table for Price Storage
```sql
CREATE TABLE crypto_prices (
    timestamp TIMESTAMP,
    symbol VARCHAR(10),
    price DECIMAL(15, 8)
);
```
Ensure your PostgreSQL server is running and accessible before executing the scripts.

### 3️⃣ Run the Scripts
#### Extract Real-Time Crypto Prices
Start the WebSocket script to fetch live price updates:
```bash
python extract.py
```

#### Transform the Data for Visualization
Process the stored data using Apache Spark for cleaning and formatting:
```bash
python transform.py
```

#### How to Run Your Code
* Ensure PostgreSQL is running and accessible.
* Modify the WebSocket subscription list to track additional cryptocurrencies.
* Configure Spark JAR dependencies properly before executing the transformation script.
```
