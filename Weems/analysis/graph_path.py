import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import re
rcParams.update({'figure.autolayout': True})

names = ['sg','ny','fra','za1','za2','za3','za4','za5',]
cases = [
r'GET /HNAP1/ HTTP/1\.1',
r'POST /command\.php HTTP/1\.0',
r'GET /cgi/common\.cgi HTTP/1\.0',
r'GET /phpMyAdmin/scripts/setup\.php HTTP/1\.1',
r'GET /if youve had a dose of a freaky ghost HTTP/1\.1',
r'GET /cgi-bin/test-cgi HTTP/1\.1',
r'GET /w00tw00t\.at\.ISC\.SANS\.DFind:\) HTTP/1\.1',
]

cc = [
'GET /HNAP1/ HTTP/1.1',
'POST /command.php HTTP/1.0',
'GET /cgi/common.cgi HTTP/1.0',
'GET /phpMyAdmin/scripts/setup.php HTTP/1.1',
'GET /if youve had a dose of a freaky ghost HTTP/1.1',
'GET /cgi-bin/test-cgi HTTP/1.1',
'GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1',
]

res = {}
r = {}

for n in names:
    r[n] = []
    for c in cc:
        r[n].append([0,c])

for name in names:
    x = [] # count
    y = [] # IP
    width = 0.35
    with open('/home/deontp/GitHub/honeypot/server/analysis/logs/path_freq/' + name + '.freq') as f:
        for line in f:
            if any(re.compile(r, re.I).search(line) for r in cases):
                t = line.strip().split()
                for i in r[name]:
                    #print t
                    obj = re.search(r'\d+(.*)', line.strip())
                    if obj:
                        x = obj.group(1).strip()
                        if i[1] == x:
                            a = line.strip().split()
                            i[0] = int(a[0])


raw_data = { 'instances': ['sg','ny','fra','za1','za2','za3','za4','za5',],
    'GET /HNAP1/ HTTP/1.1': [12,0,1,7,8,7,8,0],
    'POST /command.php HTTP/1.0': [7,5,7,7,10,9,9,0],
    'GET /cgi/common.cgi HTTP/1.0': [7,5,7,7,10,9,9,0],
    'GET /phpMyAdmin/scripts/setup.php HTTP/1.1': [0,0,2,5,15,3,2,0],
    'GET /if youve had a dose of a freaky ghost HTTP/1.1': [1,1,1,1,1,1,1,1],
    'GET /cgi-bin/test-cgi HTTP/1.1': [1,1,1,1,1,1,1,1],
    'GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1': [1,1,1,1,1,1,1,1],
}

rd = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'pre_score': [4, 24, 31, 2, 3],
        'mid_score': [25, 94, 57, 62, 70],
        'post_score': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = [
'instances',
'GET /HNAP1/ HTTP/1.1',
'POST /command.php HTTP/1.0',
'GET /cgi/common.cgi HTTP/1.0',
'GET /phpMyAdmin/scripts/setup.php HTTP/1.1',
'GET /if youve had a dose of a freaky ghost HTTP/1.1',
'GET /cgi-bin/test-cgi HTTP/1.1',
'GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1',])
df
# Setting the positions and width for the bars
pos = list(range(len(df['GET /HNAP1/ HTTP/1.1'])))
width = 0.25

# Plotting the bars
fig, ax = plt.subplots()

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos,df['GET /HNAP1/ HTTP/1.1'],width,alpha=0.5,color='#EE3224',label=df['instances'][0])
# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],df['POST /command.php HTTP/1.0'],width,alpha=0.5,color='#F78F1E',label=df['instances'][1])
# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],df['GET /cgi/common.cgi HTTP/1.0'],width,alpha=0.5,color='#FFC222',label=df['instances'][2])
# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],df['GET /phpMyAdmin/scripts/setup.php HTTP/1.1'],width,alpha=0.5,color='#F78F1E',label=df['instances'][1])
# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos],df['GET /if youve had a dose of a freaky ghost HTTP/1.1'],width,alpha=0.5,color='#FFC222',label=df['instances'][2])
# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*5 for p in pos],df['GET /cgi-bin/test-cgi HTTP/1.1'],width,alpha=0.5,color='#FFC222',label=df['instances'][2])
# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*6 for p in pos],df['GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1'],width,alpha=0.5,color='#FFC222',label=df['instances'][2])

# Set the y axis label
ax.set_ylabel('Score')

# Set the chart's title
ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['instances'])

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['GET /HNAP1/ HTTP/1.1'] + df['POST /command.php HTTP/1.0'] + df['GET /cgi/common.cgi HTTP/1.0']+ df['GET /phpMyAdmin/scripts/setup.php HTTP/1.1']+ df['GET /if youve had a dose of a freaky ghost HTTP/1.1']+ df['GET /cgi-bin/test-cgi HTTP/1.1']+ df['GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1'], loc='upper left'])] )

# Adding the legend and showing the plot
plt.legend([
'GET /HNAP1/ HTTP/1.1',
'POST /command.php HTTP/1.0',
'GET /cgi/common.cgi HTTP/1.0',
'GET /phpMyAdmin/scripts/setup.php HTTP/1.1',
'GET /if youve had a dose of a freaky ghost HTTP/1.1',
'GET /cgi-bin/test-cgi HTTP/1.1',
'GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1',], loc='upper left')
plt.grid()
plt.show()
