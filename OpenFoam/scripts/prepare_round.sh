#!/bin/bash

TYP=round
FROM=templates/$TYP
for sigma in 5 10 15 20 25 30 35 40 45 50
do
	TEST=${TYP}_sigma${sigma}
	TO=results/$TEST
	mkdir -p $TO
	mkdir -p $TO/constant
	touch $TO/$TEST.foam
	ln -s ../../$FROM/0 $TO/0
	ln -s ../../../$FROM/constant/polyMesh $TO/constant/polyMesh
	cp $FROM/constant/* $TO/constant/
	cp -r $FROM/system $TO/system
	sed -i "s/75/${sigma}/g" $TO/constant/phaseProperties
	cp templates/run.sh $TO
	sed -i "s/qwerty/$TEST/g" $TO/run.sh
	cp templates/save_anim*.py $TO
	sed -i "s/qwerty/$TEST/g" $TO/save_anim2d.py
	sed -i "s/qwerty/$TEST/g" $TO/save_anim3d.py
	mkdir -p $TO/anim2d
	mkdir -p $TO/anim3d
done
