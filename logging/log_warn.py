import logging

logging.basicConfig(level=logging.DEBUG,format='%(name)s = %(levelname)s => %(message)s')
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s  %(message)s',datefmt="%d-%b-%y")

logging.debug("This is Debugging")
logging.warning("this is warning")

a = 15
b = 0

try:
    c = a/b
except Exception as e:
    # logging.error("Error occured",exc_info=True)
    logging.error("Error occured",exc_info=False)
    print(e)
    print(type(e))

    logging.exception("Error Exception occured")