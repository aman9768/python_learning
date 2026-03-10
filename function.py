#function where we caluclate the discount price of a product
from loguru import logger
def discount_price(*price,discount=0.05):
    total=0
    for amount in price:
        total+=amount
    
    amount_to_be_paid=total-(total*discount)
    return amount_to_be_paid

final_discouted_price=discount_price(50,40,30,97)
logger.info(final_discouted_price)

