from loguru import logger
import mysql.connector


def read_from_mysql(config,query):
    try:
        connection=mysql.connector.connect(host=config["mysql_db"]["host"],
                                        user=config["mysql_db"]["user"],
                                        password=config["mysql_db"]["password"],
                                        database=config["mysql_db"]["database"])

        logger.info(f"The connection is successful {connection}")

        cursor=connection.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        logger.info(f"{result}")
        return result

    # insert_query = "INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)"
    # cursor.execute(insert_query, ('Aman', 'labour', 900))
    # connection.commit()
    except Exception as e:
        logger.info(f"error occured in mysql {e}")
        raise e
    finally:
        connection.close()
        cursor.close()

