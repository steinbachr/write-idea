#!/bin/bash
# gathers a random word of the day and gets it's definition, then opens up vim for editing the writing journal
# The user should specify the file to write to as an argument

FILE="journal.txt";
if [ -z "$1" ]; then
    echo "no file specified, using file $FILE";
else
    FILE=$1
fi

DIR_REL="`dirname \"$0\"`"
DIR_ABS="`( cd \"$DIR_REL\" && pwd )`"
SCRIPT="$DIR_ABS/write_idea.py"
WORDS=`python $SCRIPT`;

echo "$WORDS" >> $FILE;
vim $FILE;


