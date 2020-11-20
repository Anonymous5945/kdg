#!/bin/bash

(find $directory -type f -name "*.mkv"; find $directory -type f -name "*.mp4"; find $directory -type f -name "*.vtt"; find $directory -type f -name "*.srt";) 2>&1 | tee ror.txt
IFS='
'
j=0
for i in $(cat ror.txt)
do
rm ${i}
done
rm ror.txt