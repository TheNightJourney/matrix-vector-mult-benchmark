all: main_b_space.exe

main_b_space.exe: mylib.o
	gcc -o main_b_space main_b_space.c mylib.o

utils.o: mylib/mylib.c
	gcc -o main_b_space.exe main_b_space.c mylib.o

clear:
	rm *.exe
	rm *.o