#!/bin/bash

EXERCISEFILE=exercises

if [ -f "$EXERCISEFILE" ]; then
   rm "$EXERCISEFILE"
fi

touch "$EXERCISEFILE"

if test ${1} -eq ${1} 2>/dev/null; then
  if test ${1} > 0; then
     number_of_exercises="$1"
  else
     number_of_exercises=10
  fi
else
  echo "Usage: pass the number of exercises you need to auto-generate as the single argument"
  echo "Default behavior: 10 exercise will be generated"
  number_of_exercises=10
fi

for (( i = 0; i < $number_of_exercises; i++ )) 
do
   python3 subnets.py >> "$EXERCISEFILE"
done
