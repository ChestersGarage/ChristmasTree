#!/bin/bash

git commit -am "Edits"
git push

ssh pi@192.168.1.125 "cd ChristmasTree; git pull; python3 flickering_candles.py"
