#!/bin/bash

git commit -am "Edits"
git push

ssh pi@192.168.1.125 "git pull -C /home/pi/ChristmasTree; killall python3; nohup python3 /home/pi/ChristmasTree/flickering_candles.py > /home/pi/flickering_candles.log 2>&1 &"
