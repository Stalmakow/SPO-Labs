#!/bin/bash
(echo "Name,Format,Size,Creat-time,Change-time,Type,Audio-Video Duration")>./Data.xls   #это комментарий к коду
rm -r ~/Downloads   
files()   # ну в общем крч это функция, и она функционирует
{
( 
for i in "$1"/*       
do
N1=$(expr length "$i")
N2=3
N3=$(echo "$i"|rev|cut -f1 -d .|rev)
if [[ $N3 == $i ]]; then
w=' '
else
w=$N3
fi
s=$i
e=$(($N1+$N2))
if [[ $w == "mkv" || $w == "mp4" ]]; then         #Самая большая и болезненная часть скрипта- определение на видео-аудио
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
),$(mediainfo "$s"|head -n7|tail -n1|cut -c44-)   #Сразу скажу идея этого определения не моя, я ее поташил у друга потому что нашел приемлемой
elif [[ $w == "mp3" ]]; then
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
),$(mediainfo "$s"|head -n5|tail -n1|cut -c44-)
elif [[ $w == "avi" ]]; then
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
),$(mediainfo "$s"|head -n6|tail -n1|cut -c44-)
elif [[ $(echo "$i"|rev|cut -f1 -d /|rev) == "*" ]]; then
continue
elif [[ -d "$s" && $(echo "$s"|wc -l) -ne 0 ]]; then
files "$s"
else
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
)
fi
done)>>./Data.xls  #Сюда будет помещена информация (Местонахождение-текущая папка)
}
files ~/1  #Сюда вписать название папки по которой производится анализ
