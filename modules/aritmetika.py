import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)s:%(funcName)s:%(message)s")
file_handler.setFormatter(formatter)

def daugyba(a, b):
    try:
        res = a * b
    except Exception as e:
        # išmetam pranešimą kad įvyko klaida
        logger.error(f"Vykdant funkciją {daugyba.__name__}, įvyko klaida {e.__class__.__name__}: {e}")
        return None
    else:
        logger.info(f"Paleista funkcija {daugyba.__name__}: {a} * {b} = {res}")
        return res

print(daugyba(2, 2))
