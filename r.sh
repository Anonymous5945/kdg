#!/bin/bash
input="$1"
output="$2"
rclone copy "$input" "Inizio Encode":"$output" -P
