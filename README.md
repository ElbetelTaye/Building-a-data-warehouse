# Data Cleaning and Transformation for Ethiopian Medical Businesses

## Project Overview

This project focuses on creating a data warehouse to store and analyze information on Ethiopian medical businesses. The data is sourced through web scraping and Telegram channels, with integrated YOLO (You Only Look Once) object detection capabilities to enhance data analysis. The warehouse enables better insights into business trends, patterns, and correlations, facilitating informed decision-making.

## Notebooks

### data_preprocessing.ipynb
This notebook handles the following tasks:
- **Data Loading**: Loads JSON files containing Ethiopian medical business data from a specified directory.
- **Data Cleaning**:
  - Removes duplicate entries.
  - Fills in missing values where possible and drops rows missing essential data.
  - Standardizes formats, ensuring consistency, especially in date and text fields.
  - Validates cleaned data to meet quality standards.
- **Database Integration**: Stores cleaned data in a PostgreSQL database using SQLAlchemy.
- **Image Resizing for YOLO**: Resizes images for YOLO object detection.
- **Error Handling and Logging**: Tracks errors and logs progress in `data_cleaning_task2.log`.

### object_detection_yolo.ipynb
- **Data Validation**: Checks the paths for training images, labels, and `data.yaml` configuration to ensure they are set correctly.
- **Training Setup**: Configures YOLOv5 training parameters, such as `epochs`, `batch_size`, and `img_size`.
- **YOLOv5 Training Execution**: Runs YOLOv5 training using a subprocess with the necessary dataset paths and configuration.
- **Model Weight Management**: Saves the best and final weights from training as `labeled_yolov5_model.pt`.
- **Database Integration**: Saves object detection results in the warehouse database.

## Setup Instructions

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## DBT Integration

DBT (Data Build Tool) is used to manage data transformations and ensure a structured data pipeline. This integration ensures high-quality, maintainable SQL code for transforming the data.

### Key DBT Operations:
- **Data Modeling**: Aggregates data from multiple sources, including cleaned Ethiopian medical business data, while defining relationships between tables.
- **Transformations**: Transforms raw data into structured formats for analysis. This includes removing duplicates, handling missing data, and standardizing formats.
- **Materializations**: Models are materialized as tables in PostgreSQL, ensuring efficient querying and analysis. Data is updated with each run to maintain freshness.
- **Version Control and Documentation**: DBT's version control tracks changes to the models, while built-in documentation ensures clarity in the transformation process.

Run the following command to execute DBT models and update the data warehouse:

```bash
dbt run
```

## Logging

Logs are saved in `logfile.log`, `process.log` and `yolo_training.log`, detailing the processing steps, errors encountered, and other relevant information.

## FastAPI CRUD Application

A FastAPI app is provided to expose data collected from YOLOv5 object detection, with a PostgreSQL database as the backend.

### Features:
- Full CRUD (Create, Read, Update, Delete) API for detection data.
- PostgreSQL integration using SQLAlchemy.
- Pydantic schemas for data validation.

### Steps:

1. **Clone the Repository**:

```bash
git clone https://github.com/ElbetelTaye/Building-a-data-warehouse.git
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **Configure Database**: Update `database.py` with your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://<username>:<password>@<host>:<port>/<database_name>"
```

4. **Run the API**:

```bash
uvicorn App.main:app --reload
```

### API Endpoints:

- `GET /items/`: Retrieve all items.
- `GET /items/{id}`: Retrieve an item by ID.
- `POST /items/`: Create a new item.
- `PUT /items/{id}`: Update an item.
- `DELETE /items/{id}`: Delete an item.

## Docker Setup

1. **Create Dockerfile**:

```bash
docker build -t fastapi-app .
```

2. **Run Docker Container**:

```bash
docker run -d -p 8000:8000 fastapi-app
```