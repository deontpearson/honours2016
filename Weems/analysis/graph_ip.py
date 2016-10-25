from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np
rcParams.update({'figure.autolayout': True})

names = ['sg','ny','fra','za1','za2','za3','za4','za5',]

for name in names:
    x = [] # count
    y = [] # IP
    count = 0
    width = 0.35
    with open('/home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/' + name + '.freq') as f:
        for line in f:
            t = line.split()
            if count == 5:
                break
            x.append(int(t[0]))
            y.append(t[1])
            count += 1
    fig, ax = plt.subplots()

    ind = np.arange(len(y))  # the x locations for the groups
    ax.barh(ind, x, align='center', alpha=0.5)
    plt.yticks(ind, y)
    plt.xlabel('Count')

    plt.gca().invert_yaxis()

    for i, v in enumerate(x):
        ax.text(v, i + 0.1, str(v), color='black', fontweight='bold', horizontalalignment='right')
    #plt.title('Top 5 Addresses for Asia')
    #plt.title('Top 5 IP Addresses for America')
    #plt.title('Top 5 IP Addresses for Europe')
    #plt.title('Top 5 IP Addresses for Africa')
    plt.grid()
    plt.savefig('/home/deontp/Dropbox/Rhodes/honours_2016/thesis/graphs/ip_' + name + '.png')
