if [ $(arch) != "x86_64" ];
then
	echo "64bit"
	mono ./python/ipy64.exe ./main.py
else
	echo "32bit"
	mono ./python/ipy.exe ./main.py
fi
