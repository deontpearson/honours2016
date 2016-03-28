import logging.config # to use a config file for logging
import logging # to use the standard pyton logger

def getMyLogger():
    "retunrs a log file to be used"
    logging.config.fileConfig('modules/logger/logging.conf') # uses an external logging file to get configuration information
    return logging.getLogger('request_logger') # sets log to be the request logger from the logging.conf file

def logRequest(log, args):
    "takes in a log object and a ditionary of arguments"
    log.info('[%(pid)d] %(src)s - - [%(date)s] \"%(method)s\"'  % args)
