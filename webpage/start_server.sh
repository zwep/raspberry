#!/bin/bash

# Port number to check and start the new process on
PORT_NUMBER=8000

# Command to start the new process
COMMAND="python3 /home/pi/code/raspberry/webpage/run.py"

# Check if a process is already using the port
EXISTING_PID=$(lsof -ti :$PORT_NUMBER)

# Terminate the existing process if a PID is found
if [ -n "$EXISTING_PID" ]; then
  echo "Terminating existing process with PID: $EXISTING_PID"
  kill $EXISTING_PID
fi

# Start the new process using nohup
nohup $COMMAND > ~/log/output.log 2>&1 &

echo "New process started on port $PORT_NUMBER"
