# create a .py file adding the modules and paths from the config file to the template
import os
import sys
import yaml # PyYAML for logging config file
import re

# Globals
CONFIG = []
importString = ""
pathString = ""
specialPagesString = ""


dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
template = open(dir + '/tmp/template.py', 'r').read()

CONFIG = yaml.load(open(dir + '/modules/modules_config.yaml'))

for item in CONFIG.keys():
    tmp = CONFIG[item]
    regList = ''
    importString += "from %s import %s\n" % (tmp['path'].replace("/","."), item,)
    if tmp['method'] == 'GET':
        for a in tmp['reg_exp'].split(','):
            regList += a + ','
        pathString += "'%s' : (%s.%s,[%s])," % (tmp['key'], item, tmp['handler'], regList)
    if tmp['admin']:
        specialPagesString += ("'%s',") % (tmp['key'],)

template = template.replace("<ADMIN_PAGES>", specialPagesString)
template = template.replace("<IMPORTS>", importString)
template = template.replace("<PATHS>", pathString)

# creates directories for the honeypot
if not os.path.exists(dir + '/data'):
    os.makedirs(dir + '/data')

# write out the .py file with the implemented modules
output= open(dir + '/server.py', "w+")
output.write(template)
output.flush()
output.close()
