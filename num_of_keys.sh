#!/bin/sh

#Bash-Script, berechnet Anzahl der Artikel im geparsten Wikipedia-Korpus
total_length=0
for file in /home/thomas/bachelorarbeit/wiki_intros_cheap/*
 do
   len="$(jq length $file)"
   total_length=$((total_length+len))
done
echo $total_length