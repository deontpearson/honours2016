#!/bin/bash
# My first script

sshpass -p "#honeypotproject2016" scp honeypot@46.101.102.165:/home/honeypot/honeypot/server/data/logs/46-101-102-165_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "#honeypotproject2016" scp honeypot@46.101.102.165:/home/honeypot/honeypot/server/data/logs/46-101-102-165:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "#honeypotproject2016" scp honeypot@46.101.102.165:/home/honeypot/honeypot/server/data/logs/46-101-102-165:443_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs

sshpass -p "#honeypotproject2016" scp honeypot@104.236.100.177:/home/honeypot/honeypot/server/data/logs/104-236-100-177_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "#honeypotproject2016" scp honeypot@104.236.100.177:/home/honeypot/honeypot/server/data/logs/104-236-100-177:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "#honeypotproject2016" scp honeypot@104.236.100.177:/home/honeypot/honeypot/server/data/logs/104-236-100-177:443_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs

sshpass -p "#honeypotproject2016" scp honeypot@128.199.238.27:/home/honeypot/honeypot/server/data/logs/128-199-238-27_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "#honeypotproject2016" scp honeypot@128.199.238.27:/home/honeypot/honeypot/server/data/logs/128-199-238-27:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "#honeypotproject2016" scp honeypot@128.199.238.27:/home/honeypot/honeypot/server/data/logs/128-199-238-27:443_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs


sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-120_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-120:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs

sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-121_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-121:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs

sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-122_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-122:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs

sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-123_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-123:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs

sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-124_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
sshpass -p "deonrocks" scp deon@196.21.242.120:/home/deon/honeypot/server/data/logs/196-21-242-124:80_access.log /home/deontp/GitHub/honeypot/server/analysis/logs/pulled_logs
