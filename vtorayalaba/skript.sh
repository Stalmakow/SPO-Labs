#!/bin/bash     #ну это крч скрипт в том чтобы подкачать требуемых для ихнего скрипта прог и запустить ихний скрипт
mkdir /stalmakowproject     #создаю место под то что скачаю с гита и соответсвенно скачиваю и "развертываю" ето
cd /stalmakowproject        
git init
git remote add origin https://github.com/popcorn-official/popcorn-desktop
git pull https://github.com/popcorn-official/popcorn-desktop
apt install npm   #подкачиваю элемент npm
./makepopcorn.sh  #подрубаю их скрипт 
