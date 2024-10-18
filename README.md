# Data Cleaning and Transformation for Ethiopian Medical Businesses

## Project Overview
This project aims to build a data warehouse for storing and analyzing data on Ethiopian medical businesses. The data is collected from web scraping and Telegram channels, and object detection capabilities are integrated using YOLO (You Only Look Once). The goal is to enhance data analysis by storing cleaned, transformed, and standardized data, making it available for querying and reporting.

The data warehouse helps provide insights into trends, patterns, and correlations, which are critical for making informed business decisions in the Ethiopian medical sector.

## Project Structure

### Notebooks

#### Data_Cleaning_and_Transformation.ipynb
This notebook performs the following key operations:
- **Data Loading**: Loads JSON data on Ethiopian medical businesses from a local directory.
- **Data Cleaning**: 
  - **Remove Duplicates**: Ensures no redundant data.
  - **Handle Missing Values**: Fills missing content and drops rows missing essential information.
  - **Standardize Formats**: Ensures consistent formatting, especially for dates and text fields.
  - **Validation**: Validates cleaned data to ensure it meets expected standards.
- **Database Integration**: After cleaning, the data is stored in a PostgreSQL database using SQLAlchemy.
- **Image Resizing for YOLO**: Resizes images to 416x416 to ensure they are ready for object detection using YOLO.
- **Error Handling and Logging**: Tracks errors and logs progress in a log file (`logfile.log`).


## Setup Instructions

### Prerequisites
- **Python 3.x**
### Install Dependencies
Install the required libraries using:
```bash
pip install -r requirements.txt
