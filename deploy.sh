#!/bin/bash

SCENE=$1
HOSTNAME="christmastree.home"

#if [[ -z $SCENE ]]; then
#    echo "No scene specified, using default (flickering_candles)"
#    SCENE="flickering_candles"
#fi

#git commit -am "Improving things..."
#git push

rsync -axv ./* pi@christmastree.home:/home/pi/ChristmasTree/
ssh pi@${HOSTNAME} "killall -9q python3; sudo killall -9q fcserver-rpi"
ssh pi@${HOSTNAME} "nohup sudo /root/fcserver-rpi /home/pi/ChristmasTree/server.json >> /home/pi/fcserver.log 2>&1 &"
ssh pi@${HOSTNAME} "nohup python3 /home/pi/ChristmasTree/christmas_tree.py /home/pi/ChristmasTree/config.json >> /home/pi/christmas_tree.log 2>&1 &"

#ssh pi@${HOSTNAME} "nohup python3 /home/pi/ChristmasTree/${SCENE}.py > /home/pi/${SCENE}.log 2>&1 &"
