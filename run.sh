#!/bin/bash -i
SERVER_SCRIPT="/home/vagrant/notes/notes.py"
PID_FILE="/var/run/piet-us-notes/agent.pid"

python $SERVER_SCRIPT &> /dev/null &
echo `ps aux | grep [n]otes.py | awk '{print $2}'` > $PID_FILE
