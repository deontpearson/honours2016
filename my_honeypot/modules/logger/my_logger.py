import logging.config # to use a config file for logging
import logging # to use the standard pyton logger
from datetime import datetime

def getMyLogger():
    "retunrs a log file to be used"
    logging.config.fileConfig('modules/logger/logging.conf') # uses an external logging file to get configuration information
    return logging.getLogger('request_logger') # sets log to be the request logger from the logging.conf file

def logRequest(log, args):
    """takes in a log object and a ditionary of arguments
    args = {'pid':primaryID, 'src': soruceAddress, 'date':datetime, 'method':method, 'resource': resource, 'http': httpVersion, 'code': responseCode}
    """
    temp = args
    temp['date'] = datetime.now()
    log.info('[%(pid)d] %(src)s - - [%(date)s] \"%(method)s %(resource)s %(http)s\" %(code)d'  % temp)
