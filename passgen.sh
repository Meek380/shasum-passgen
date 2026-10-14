#!/bin/bash
read -p "Enter URL: " url
curl --silent $url >> seed.txt
python3 corrupter.py -c 10 seed.txt
sha1sum seed.txt > sha.txt
python3 specialcharacter.py -c 100 sha.txt
python3 printpass.py
rm seed.txt
rm sha.txt
