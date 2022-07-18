#!/bin/bash
 
for i in `seq 1 90`
do
   #echo $i
   DIR_NAME=`printf "%03d\n" "${i}"`
   mkdir -p $DIR_NAME
   cp main.py $DIR_NAME/.
done


