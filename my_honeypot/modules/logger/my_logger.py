import logging.config # to use a config file for logging
import logging # to use the standard pyton logger
import datetime

STATS = {}
ADDRESS_COUNTER = {}

def loadStats():
    "retrievs stats from a file name stats.info"
    global STATS
    tempList = open('./data/stats.info', 'r').read().split('\n')
    for i in tempList:
        if i != '':
            temp = i.split('=')
            STATS[temp[0]] = temp[1]

def saveStats():
    "saves the stats from dictionary to a file in data/stats.info"
    with open('./data/stats.info', 'w') as f:
        for l in STATS:
            f.write('%s=%d\n' % (l,STATS[l]))

def getMyLogger(loggerName):
    "retunrs a log file to be used"
    logging.config.fileConfig('modules/logger/logging.conf') # uses an external logging file to get configuration information
    loadStats()
    return logging.getLogger(loggerName) # sets log to be the request logger from the logging.conf file

def logRequest(log, args):
    """takes in a log object and a ditionary of arguments
    args = {'pid':primaryID, 'src': soruceAddress, 'date':datetime, 'method':method, 'resource': resource, 'http': httpVersion, 'code': responseCode}
    """
    global STATS, ADDRESS_COUNTER
    temp = args
    format = '%d %b %H:%M:%S %Y'
    today = datetime.datetime.today()
    temp['date'] = today.strftime(format)
    temp['pid'] = int(STATS['REQUESTS'])
    log.info('[%(pid)d] %(src)s - - [%(date)s] \"%(method)s %(resource)s %(http)s\" %(code)d'  % temp)
    STATS['REQUESTS'] = int(STATS['REQUESTS']) + 1
    saveStats()
