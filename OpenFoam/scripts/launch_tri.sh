#!/bin/bash

TYP=tri
for sigma in 5 10 15 20 25 30 35 40 45 50
do
	DIR=${TYP}_sigma${sigma}
	sbatch -J $DIR $DIR/run.sh
done
