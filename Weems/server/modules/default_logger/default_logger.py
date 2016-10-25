import logging.config # to use a config file for logging
import logging # to use the standard pyton logger
import datetime
import pytz # this is used to enable us to get the timezone information when outputting the date to access logs
from pytz import timezone # so that we can change the time zone of pytz
import os, sys
import yaml # PyYAML for logging config file

STATS = {}
REQUEST = None
ALOG = None
RLOG = None
dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
LOCAL_TIME = timezone('Africa/Johannesburg') # see for info on what this does http://pytz.sourceforge.net/
DATE_TIME = None
LOGGING_CONFIG = None
STATS_FILE = None

def loadStats():
    "retrievs stats from a file name stats.dat"
    if os.path.isfile(dir + '/data/' + STATS_FILE):
        for i in open(dir + '/data/' + STATS_FILE, 'r').read().split('\n'):
            if i != '':
                temp = i.split('=')
                STATS[temp[0]] = temp[1]

def saveStats():
    "saves the stats from dictionary to stats.dat"
    with open(dir + '/data/' + STATS_FILE, 'w') as f:
        for l in STATS:
            f.write('%s=%d\n' % (l,int(STATS[l])))

def getLogger(loggerName, logName):
    "retunrs a log file to be used"
    global LOGGING_CONFIG
    if not os.path.exists(dir + '/data/logs'):
        os.makedirs(dir + '/data/logs')
    if LOGGING_CONFIG == None:
        LOGGING_CONFIG = yaml.load(open(dir + '/modules/default_logger/logging_config.yaml'))# gets the config settings from external YAML file
    LOGGING_CONFIG['handlers'][loggerName]['filename'] = dir + '/data/logs/' + logName # sets the log file path at runtime based on directory
    logging.config.dictConfig(LOGGING_CONFIG) # uses an external logging file to get configuration information
    return logging.getLogger(loggerName) # sets log to be the request logger from the logging.conf file


def logPostRequest():
    fname = '%s_%s.out' % (DATE_TIME.strftime('%Y%m%d_%H%M%S'), str(STATS['REQUESTS']))
    if STATS == {}:
        loadStats()
    if 'POST_REQUESTS' in STATS.keys():
        STATS['POST_REQUESTS'] = int(STATS['POST_REQUESTS']) + 1
    else:
        STATS['POST_REQUESTS'] = 1
    if not os.path.exists(dir + '/data/logs/post'):
        os.makedirs(dir + '/data/logs/post')
    with  open(dir + '/data/logs/post/' + fname, 'w') as f:
        f.write('%s\nArgs:\n%s\nForm:\n%s\nData:\n%s\nFile:\n%s\n' % (REQUEST.headers, REQUEST.args, REQUEST.form, REQUEST.get_data(),REQUEST.files,) )
    saveStats()

def logRequest(): # keep track of the requests that come in and the number of requests that have been recieved
    "logs the requests to the webpage as well as the request counter"
    if STATS == {}:
        loadStats()
    if 'REQUESTS' in STATS.keys():
        STATS['REQUESTS'] = int(STATS['REQUESTS']) + 1
    else:
        STATS['REQUESTS'] = 1
    args = {'src':REQUEST.remote_addr, 'pid':STATS['REQUESTS'], 'headers':REQUEST.headers}
    RLOG.info('[%(pid)s] %(src)s \n%(headers)s'  % args)
    saveStats()

def logCLF ():#(logFile, request): # log files in common log format as per appache logs
    " logs a request in the appache common log format"
    res = ''.join(REQUEST.path)
    if bool(REQUEST.args):
        res += '?'
        for key in REQUEST.args:
            if not res.endswith('?'):
                res += '&'
            res += key + '=' + REQUEST.args[key]
    format = '%d/%b/%Y:%H:%M:%S %z' # see http://strftime.org/ for date time placeholder

    args = {'src': REQUEST.remote_addr,
        'method': REQUEST.method,
        'resource': res,
        'http': REQUEST.environ['SERVER_PROTOCOL'],
        'code': '-',
        'rfc':'-',
        'userid':'-',
        'size':'-',
        'date': DATE_TIME.strftime(format)} # logs every request that comes into the server
    ALOG.info('%(src)s %(rfc)s %(userid)s [%(date)s] \"%(method)s %(resource)s %(http)s\" %(code)s %(size)s'  % args)

def loggingHandler(request, host, port ):
    instanceID = '%s:%d' % (host, port)
    global REQUEST, ALOG, RLOG, DATE_TIME, STATS_FILE # must use global when assiging a value to a global variable
    DATE_TIME = datetime.datetime.today().replace(tzinfo=LOCAL_TIME)
    REQUEST = request
    STATS_FILE = '%s_stats.dat' % (instanceID.replace('.','-'),)
    al = '%s_access.log' % (instanceID.replace('.','-'),)
    rl = '%s_request.log' % (instanceID.replace('.','-'),)
    if ALOG == None:
        ALOG = getLogger('access_log', al)
    if RLOG == None:
        RLOG = getLogger('request_log', rl)
    #if PLOG == None:
    #    PLOG = getLogger('post_log', pl)
    logCLF()
    logRequest()
    if REQUEST.method == 'POST':
        logPostRequest() # log the post request information to see what POST's are coming in.
