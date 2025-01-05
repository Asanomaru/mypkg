#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
if [ $? -ne 0 ]; then
    echo "Build failed"
    exit 1
fi

source install/setup.bash

LOG_FILE=/tmp/mypkg.log

echo "Running calendar_notifier and saving logs to $LOG_FILE"
timeout 20 bash -c "ros2 run mypkg calendar_notifier > $LOG_FILE 2>&1"

echo "Checking log file..."
if [ -s $LOG_FILE ]; then
    echo "Log file is not empty. Checking content..."
    cat $LOG_FILE | grep -i "Published calendar notification."
    if [ $? -eq 0 ]; then
        echo "Test passed: Notification message detected."
        exit 0
    else
        echo "Test failed: No notification message found in logs."
        exit 1
    fi
else
    echo "Log file is empty or not created."
    exit 1
fi

