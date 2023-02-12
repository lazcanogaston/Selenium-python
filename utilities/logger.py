import logging

class Logger():
    
    # to use next method -> in tests, use StringIO logger (log in memory)
    # import io
    # logStringio = io.StringIO()

    def _init_logger(log_stringio_obj, logger_name):
        #creates or open the log 
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        #give format to each line of the log time - level - message
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        #initialize the handler
        io_log_handler = logging.StreamHandler(log_stringio_obj)
        #give the format to the handler
        io_log_handler.setFormatter(formatter)
        #attach the handler to the logger instance
        logger.addHandler(io_log_handler)
        return logger

    def _init_logger_txt(fileName):
        logger = logging.getLogger('name_%s' % fileName)  #1
        logger.setLevel(logging.INFO)  #2
        handler = logging.FileHandler("C:\\Selenium-python\\logs\\"+ fileName +".log") #3
        handler.setLevel(logging.INFO)  #4
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s') #5
        handler.setFormatter(formatter)  #6
        logger.addHandler(handler)  #7
        return logger

    def fileChecker(stringIo, keyword):
        found = 0
        datafile = stringIo.getvalue() #gets the log
        for line in str(datafile).splitlines(): #convert file in string and split it into lines
            if keyword in line:
                found = found +1     
        return found

    def fileChecker_txt(fileName, keyword):
        found = 0
        with open("C:\\Selenium-python\\logs"+ fileName +".log") as f:
            datafile = f.readlines()
        for line in datafile:
            if keyword in line:
                found = found +1
        return found