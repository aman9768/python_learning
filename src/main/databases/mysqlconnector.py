from loguru import logger
import mysql.connector


class MySqlConnection:
    def __init__(self,config):
        self.config=config
        self.connection=None
    
    def connect(self):
        try:
            self.connection=mysql.connector.connect(host=self.config["mysql_db"]["host"],
                                            user=self.config["mysql_db"]["user"],
                                            password=self.config["mysql_db"]["password"],
                                            database=self.config["mysql_db"]["database"])
            logger.info("mysql connection successful")
        except Exception as e:
            logger.info(f"error occured, {e}") 
            raise e   
    
    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info("mysql connection closed")

class MySqlCrudOperation:
    def __init__(self,mysql_connection):
        self.connection=mysql_connection
        
    def read_from_mysql(self,query):
        try:
            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            logger.info(f"{result}")
            return result
        except Exception as e:
            logger.info(f"error occured in mysql query run {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
                logger.info("cursor closed")
    def insert_from_mysql(self,query,parameter):
        try:
            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            return result
        except Exception as e:
            logger.info(f"error occured {e}")
            raise e
        finally:
            self.connection.commit()
    
            




