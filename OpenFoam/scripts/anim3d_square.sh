#!/bin/bash

#set -x

source scripts/config.sh # <-- should define PARAVIEW_DIR
iTYP=square
for sigma in 5 10 15 20 25 30 35 40 45 50
do
	TO=${TYP}_sigma${sigma}
	time ${PARAVIEW_DIR}/bin/pvpython-real results/$TO/save_anim3d.py
	#zip results/anim2d/${TYP}.zip results/$TO/anim2d/*.png
done
