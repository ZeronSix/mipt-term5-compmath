#!/bin/bash
rm -f output.txt

echo $'n\terror\ttime' > output.txt
for n in $(seq 100 200 1000); do
  ./project.py $n >> output.txt
done
