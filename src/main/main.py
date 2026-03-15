from src.main.databases.mysqlconnector import *


import configparser
config=configparser.ConfigParser()
config.read(r"C:\Users\Aman\Desktop\Learning\python_learning\src\resource\config_file.ini")

def main():
    query="select name from labours_table"
    final_result=read_from_mysql(config,query)
    logger.info(f"{final_result}")

if __name__=="__main__":
    main()