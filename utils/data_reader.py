import json
import csv
import openpyxl
from pathlib import Path

def read_json_data(file_path:str):
    """
    read json test data for API and UI automation
    """
    try:
        
        project_root = Path(__file__).resolve().parent.parent

        json_file = project_root / file_path

        print(f"Reading JSON file: {json_file}")

        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except Exception as e:
        print(f"Error occurred while retrieving JSON data: {e}")
        raise

