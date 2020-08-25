#! /bin/bash

# bash script. We ask the user for input,
# place the input in a variable,
# and display the variable contents in a string

echo "What is your name?"

read name

echo "What chapter are you on in Linux Basics for Hackers?"

read chapter

echo "Welcome" $name " to Chapter" $chapter " of Linux Basics for Hackers!"
