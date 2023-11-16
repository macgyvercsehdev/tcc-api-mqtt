from pymongo import MongoClient  # Importing the MongoClient class from the pymongo module

from decouple import config  # Importing the config function from the decouple module

import certifi  # Importing the certifi module

ca = certifi.where()  # Retrieving the path of the CA certificate file using certifi

client = MongoClient( # Creating a new MongoClient instance
    config('MONGO_URL'),  # Passing the MONGO_URL value from the environment variables to connect to the MongoDB server
    tlsCAFile=ca  # Setting the CA certificate file path for TLS connection
)

db = client.get_database()  # Getting the default database from the MongoClient instance