import gzip
import json
from pymongo import MongoClient

def read_gzipped_file(file_path):
    with gzip.open(file_path, 'rt') as file:
        for line in file:
            yield line.strip()

def transform_data(data):
    parsed_data = json.loads(data)
    # Perform your transformation logic here
    return parsed_data

def insert_data_to_mongodb(data, collection):
    collection.insert_one(data)

# Set your file path, database name, and collection name
file_path = 'your_file.gz'
database_name = 'your_database'
collection_name = 'your_collection'

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client[database_name]
collection = db[collection_name]

# Read the gzipped file line by line, transform the data, and insert it into MongoDB
for line in read_gzipped_file(file_path):
    transformed_data = transform_data(line)
    insert_data_to_mongodb(transformed_data, collection)


