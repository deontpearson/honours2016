#!/bin/bash

#./log_pull.bash
./merge_logs.bash
./ip_freq.bash
./path_freq.bash
python graph_ip.py
#python graph_path.py
