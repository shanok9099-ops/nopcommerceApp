import logging

# class LogGen:
#     @staticmethod
#     def loggen():
#      logging.basicConfig(filename=".\\Logs\\automation.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%H:%M:%S')
#      logger = logging.getLogger()
#      logger.setLevel(logging.INFO)
#      return logger
class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        filehandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
