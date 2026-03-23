from src.main.databases.mysqlconnector import *


import configparser
config=configparser.ConfigParser()
config.read(r"C:\Users\Aman\Desktop\Learning\python_learning\src\resource\config_file.ini")

def main():
    mysql_db_connection=MySqlConnection(config)
    mysql_db_connection.connect()
    
    crud_operation_obj=MySqlCrudOperation(mysql_db_connection.connection)
    final_result=crud_operation_obj.read_from_mysql("select * from labours_table")
    logger.info(f"{final_result}")
    mysql_db_connection.close()
     
  

if __name__=="__main__":
    main()