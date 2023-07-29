import os
from box.exceptions import BoxValueError
import yaml
from wineQuality import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any,Optional
import csv
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

@ensure_annotations
def read_yaml(path_to_file:Path)-> ConfigBox :

    """ this function reads yaml file 
    Args:
      path_to_file

    Raises :  
    ValueError if file  empty 

    returns:
      ConfigBox : ConfigBox type

    """

    try :

        with open(path_to_file, 'r') as f:
            yaml_f = yaml.safe_load(f)

            logger.info(f"yaml file: {path_to_file} loaded successfully")

            return ConfigBox(yaml_f)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    



@ensure_annotations
def create_directories(path_to_directories:list , verbose=True):


    for path in path_to_directories:
        os.makedirs(path , exist_ok= True)
    if verbose:
        logger.info(f"creating directory at : {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path_to_json) :

    with open(path_to_json) as f : 
        json_file = json.load(path_to_json)

    logger.info(f"jason file loaded successfully from  {path_to_json}")


    return ConfigBox(json_file)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"



@ensure_annotations
def dump_data_to_mongodb(csv_file_path: Path) -> None:
    """
    Dump data from a CSV file into MongoDB.

    Args:
        csv_file_path (Path): Path to the CSV file containing the data.

    Returns:
        None: The function does not return anything.

    Raises:
        Exception: If there is an error while inserting data into MongoDB.
    """
    # MongoDB connection details from environment variables
    mongo_uri: Optional[str] = os.environ.get("MONGO_URI")
    mongo_db_name: Optional[str] = os.environ.get("MONGO_DB_NAME")
    mongo_collection_name: Optional[str] = os.environ.get("MONGO_COLLECTION_NAME")

    # Connect to MongoDB using the provided URI
    client = MongoClient(mongo_uri)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]

    try:
        # Read data from CSV file and insert into the collection
        with open(csv_file_path, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            result = collection.insert_many(csv_reader)
            print(f"Successfully inserted {len(result.inserted_ids)} documents into MongoDB.")
    except Exception as e:
        print(f"Error while inserting data into MongoDB: {e}")
    finally:
        client.close()




def get_data_from_mongodb() -> pd.DataFrame:
    """
    Retrieve data from MongoDB.

    Returns:
        pd.DataFrame: A DataFrame containing the retrieved data.

    Raises:
        Exception: If there is an error while retrieving data from MongoDB.
    """
    # MongoDB connection details from environment variables
    mongo_uri: Optional[str] = os.environ.get("MONGO_URI")
    mongo_db_name: Optional[str] = os.environ.get("MONGO_DB_NAME")
    mongo_collection_name: Optional[str] = os.environ.get("MONGO_COLLECTION_NAME")

    # Connect to MongoDB using the provided URI
    client = MongoClient(mongo_uri)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]

    try:
        # Retrieve data from MongoDB and convert to DataFrame
        data = list(collection.find())

        df = pd.DataFrame(data)

        if '_id' in df.columns:
            df.drop('_id', axis=1, inplace=True)
        return df
    except Exception as e:
        print(f"Error while retrieving data from MongoDB: {e}")
    finally:
        client.close()