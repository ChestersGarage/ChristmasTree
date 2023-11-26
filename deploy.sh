#!/bin/bash

SCENE=$1

#if [[ -z $SCENE ]]; then
#    echo "No scene specified, using default (flickering_candles)"
#    SCENE="flickering_candles"
#fi

git commit -am "Improving things..."
git push

rsync -axv /Users/mchester/projects/ChristmasTree pi@192.168.1.125:/home/pi/ChristmasTree; \
ssh pi@192.168.1.125 "killall -9q python3; sudo killall -9q fcserver-rpi; \
 nohup sudo /root/fcserver-rpi /home/pi/ChristmasTree/server.json >> /home/pi/fcserver.log 2>&1 &
 nohup python3 /home/pi/ChristmasTree/christmas_tree.py /home/pi/ChristmasTree/config.json >> /home/pi/christmas_tree.log 2>&1 &"


#ssh pi@192.168.1.125 "nohup python3 /home/pi/ChristmasTree/${SCENE}.py > /home/pi/${SCENE}.log 2>&1 &"
