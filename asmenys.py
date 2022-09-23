import logging
import dalyba

# logging.basicConfig(
#     filename="asmenys.log", 
#     level=logging.INFO, 
#     format="%(asctime)s:%(levelname)s:%(module)s:%(lineno)s:%(funcName)s:%(message)s"
# )

# susikuriam savo loggerį, kurį pavadinam paleistos programos pavadinimu
logger = logging.getLogger(__name__)
# susikuriam file handlerį, kuris žinutes rašys į nurodytą failą
file_handler = logging.FileHandler('asmenys.log')
# loggeriui priskiriam file handlerį
logger.addHandler(file_handler)
# nurodom, kokio lygio žinutes loggeris apdoros
logger.setLevel(logging.DEBUG)
# nusirodom žinučių formatą
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)s:%(funcName)s:%(message)s")
# file handleriui priskiriam formatą
file_handler.setFormatter(formatter)
# susikuriam stream handlerį, kuris žinutes spausdins į terminalą
stream_handler = logging.StreamHandler()
# priskiriam stream handleriui formatą (tą patį, kurį buvom priskyrę ir file handleriui)
stream_handler.setFormatter(formatter)
# loggeriui priskiriam stream handlerį, panašiai kaip ir buvom priskyrę file handlerį
logger.addHandler(stream_handler)

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logger.info(f"Sukurtas klasės {self.__class__.__name__} objektas {vardas} {pavarde}")

ingrida = Asmuo("Ingrida", "Vaitkuvienė")
darius = Asmuo("Darius", "Vasionis")
deimante = Asmuo("Deimantė", "Jasaitytė")

print(dalyba.daugyba(2, 5))
