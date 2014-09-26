#!/bin/bash
# gathers a random word of the day and gets it's definition, then opens up vim for editing the writing journal
# The user should specify the file to write to as an argument

FILE="journal.txt";
if [ -z "$1" ]; then
    echo "no file specified, using file $FILE";
else
    FILE=$1
fi

WORDS=`python write_idea.py`;

echo "$WORDS" >> $FILE;
vim $FILE;


