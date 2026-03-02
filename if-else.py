from loguru import logger


taxi_rate=18
bus_rate=15
train_rate=5
distance_you_want_to_travel=int(input("Enter the kilometer "))
transport_mode=str(input("Enter modes of transport:taxi, bus, train "))

if distance_you_want_to_travel>1 and distance_you_want_to_travel<20 and transport_mode=="taxi":
    price=distance_you_want_to_travel*taxi_rate
    logger.info(f"the taxi rate will be {price}")
elif distance_you_want_to_travel>1 and distance_you_want_to_travel<100 and transport_mode=="bus":
    price=distance_you_want_to_travel*bus_rate
    logger.info(f"the taxi rate will be {price}")
elif distance_you_want_to_travel>1 and distance_you_want_to_travel<300 and transport_mode=="train":
    price=distance_you_want_to_travel*train_rate
    logger.info(f"the taxi rate will be {price}")
else:
    logger.info("Thank you")
