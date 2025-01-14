from dataclasses import dataclass
import pymongo
import os 


@dataclass

class EnviromentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

