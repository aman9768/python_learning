from loguru import logger
import configparser

config=configparser.ConfigParser()

config.read(r"C:\Users\Aman\Desktop\Learning\python_learning\config_file.ini")
# brick_cose=config.get("raw_materials","bar")
# logger.info(f"{brick_cost}")
# logger.info(f"{users}")

def total_no_of_tiles(length,breadth):
    no_of_tiles=length*breadth
    return no_of_tiles

def total_cost_of_tiles(config):
    tiles_cost=int(config.get("raw_materials","tiles"))
    total_no_of_tiles1=tiles_cost*total_no_of_tiles(12,12)
    return total_no_of_tiles1

final_cost=total_cost_of_tiles(config)
logger.info(f"The final cost is {final_cost}")