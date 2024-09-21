#!/bin/bash

> oldFiles.txt

files=$(grep ' jane ' ~/data/list.txt)

 # Iterate over the files
for file in $files
do
    echo "$file" >> oldFiles.txt
done
