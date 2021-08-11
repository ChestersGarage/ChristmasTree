#!/bin/bash

SCENE=$1

if [[ -z $SCENE ]]; then
    echo "No scene specified, using default (flickering_candles)"
    SCENE="flickering_candles"
fi

git commit -am "Improving things..."
git push

ssh pi@192.168.1.125 "git -C /home/pi/ChristmasTree pull; killall -q python3; nohup python3 /home/pi/ChristmasTree/${SCENE}.py > /home/pi/${SCENE}.log 2>&1 &; nohup python3 /home/pi/ChristmasTree/tree_star.py > /home/pi/tree_star.log 2>&1 &"
