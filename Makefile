all: your_file.exe

your_file.exe: mylib.o
	gcc -o your_file your_file.c mylib.o

utils.o: mylib/mylib.c
	gcc -o your_file.exe your_file.c mylib.o

clear:
	rm *.exe
	rm *.o
