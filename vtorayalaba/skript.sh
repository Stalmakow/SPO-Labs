#!/bin/bash
mkdir /stalmakowproject
cd /stalmakowproject
git init
git remote add origin https://github.com/popcorn-official/popcorn-desktop
git pull https://github.com/popcorn-official/popcorn-desktop
apt install npm
./makepopcorn.sh
