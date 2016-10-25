#!/bin/bash
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/sg_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/sg_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/sg_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/sg_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/sg_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/sg.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/ny_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/ny_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/ny_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/ny_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/ny_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/ny.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/fra_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/fra_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/fra_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/fra_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/fra_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za1_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za1_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za1_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za1_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za1_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/fra_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za1.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za2_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za2_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za2_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za2_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za2_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za2.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za3_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za3_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za3_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za3_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za3_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za3.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za4_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za4_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_2.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za4_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_3.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za4_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_4.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za4_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_2.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_3.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_4.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4_5.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za4.uniq

awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za5_1 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_1.uniq
awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za5_2 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_2.uniq
#awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za5_3 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_3.uniq
#awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za5_4 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_4.uniq
#awk '{print $1 " " $6 " "  $7 }' /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/za5_5 | sort | uniq -c | sort -n -r > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_5.uniq

cat /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_1.uniq /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5_2.uniq > /home/deontp/GitHub/honeypot/server/analysis/logs/top_5/unique/za5.uniq
