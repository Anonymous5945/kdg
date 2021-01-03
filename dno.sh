#!/bin/bash
G="$1"
input="$2"
sub="$3"
output="$4"
echo "g is $G in is $input sub is $sub out is $output"
h=$((${G}/3600))
m=$(((${G}%3600)/60))
s=$((${G}%60))
d=$(printf "%02d:%02d:%02d,000
" $h $m $s)
ffmpeg -i "${sub}" -c:s srt infi.srt
echo "0
00:00:00,000 --> $d
Join @DnOMovies Telegram Channel for Latest Asian Movies ❤️
" | cat - infi.srt > temp && mv temp infi.srt

ffmpeg -i "${input}" -i infi.srt -c copy -attach Dno.jpg -metadata:s:t mimetype=image/jpeg -metadata:s:t filename=cover.jpg -metadata title="Upl.d By Team-D&O @DnOMovies TG Group" "${output}"
rm infi.srt
