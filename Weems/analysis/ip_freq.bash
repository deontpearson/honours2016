#!/bin/bash
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/fra.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/fra.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/ny.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/ny.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/sg.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/sg.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/za1.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/za1.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/za2.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/za2.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/za3.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/za3.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/za4.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/za4.freq
awk '{print $1}' /home/deontp/GitHub/honeypot/server/analysis/logs/za5.log | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/ip_freq/za5.freq
