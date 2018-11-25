import logging
from logging import Logger

# https://python-scripts.com/logging-python

# можно добавить filemode="w" для перезаписи файла
# Существует пять уровней логирования (в порядке возрастания): DEBUG,
# INFO, WARNING, ERROR и CRITICAL

# logging.basicConfig(filename="sample.log", level=logging.INFO, filemode="w")
#
# logging.debug("This is a debug message")  # не выводится так как установлен уровень INFO
# logging.info("Informational message")
# logging.error("An error has happened!")
#
# # Создание логгера с определенным именем
# logex = logging.getLogger("ex")
# try:
#     raise RuntimeError
# except RuntimeError:
#     logex.exception("Error!")


logger = logging.getLogger("Main logger")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(filename="sample.log",mode="w")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info("Some Info from main()")
logger.info("End of file")
