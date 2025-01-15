from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("a=1/0 execution and will create an error")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)
    

if __name__=="__main__":

    file_path = r"C:\Users\kaust\sensorLive\sensor_live\aps_failure_training_set1.csv"
    database_name="aps"
    collection_name="sensor"
    dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)

    

    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)