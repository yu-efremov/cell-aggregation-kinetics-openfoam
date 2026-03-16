#!/bin/bash

#set -x

source scripts/config.sh # <-- should define PARAVIEW_DIR
TYP=tri
for sigma in 5 10 15 20 25 30 35 40 45 50
do
	TO=${TYP}_sigma${sigma}
	time ${PARAVIEW_DIR}/bin/pvpython-real results/$TO/save_anim2d.py
	#zip results/anim2d/${TYP}.zip results/$TO/anim2d/*.png
	# example of rendering command
	# ffmpeg -r 12 -i results/$TO/anim2d/$TO.%04d.png results/$TO/anim2d/$TO.avi
done
