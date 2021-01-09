#!/bin/bash
F="$1"
G="$2"
dc="$3"
res="$4"
output="$5"
u="${output%.mkv}.srt"
h=$((${G}/3600))
m=$(((${G}%3600)/60))
s=$((${G}%60))
t=$((${F}/3600))
p=$(((${F}%3600)/60))
n=$((${F}%60))
d=$(printf "%02d:%02d:%02d,000
" $h $m $s)
c=$(printf "%02d:%02d:%02d,000
" $t $p $n)
ffmpeg -y -i "https://goplay.anontpp.com/?dcode=${dc}&downloadccsub=1" -c:s srt ${u}
echo "0
$c --> $d
Join @kdramaupdates Telegram Channel for Latest Kdrama ❤️
" | cat - ${u} > temp && mv temp ${u}

ffmpeg -loglevel error -stats -y -i "https://goplay.anontpp.com/?dcode=${dc}&quality=${res}&downloadmp4vid=2" -i "${u}" -headers "Origin: https://goplay.cf" -attach Docover.jpg -metadata:s:t mimetype=image/jpeg -metadata:s:t filename=cover.jpg -metadata title="Upl.d By Team-D&O @dramaost TG Group" -c copy -disposition:s:0 default -bsf:a aac_adtstoasc "${output}"
