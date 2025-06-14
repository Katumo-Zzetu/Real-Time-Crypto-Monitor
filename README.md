# Real-Time-Crypto-Monitor
Extract, Transform, and Load  Crypto Data and monitor  using Grafana


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
