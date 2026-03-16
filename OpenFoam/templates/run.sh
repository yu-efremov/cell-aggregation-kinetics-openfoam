#!/bin/bash
#SBATCH --partition normal
#SBATCH --nodes=1 --ntasks=1 --cpus-per-task=8
#SBATCH --time=10:00:00

#set -x
source scripts/config.sh # <-- should define OPENFOAM_DIR correctly
#echo ${OPENFOAM_DIR}
source ${OPENFOAM_DIR}/etc/bashrc

cd qwerty

echo 'Start time: ' $(date)
interFoam
echo 'End time: ' $(date)
