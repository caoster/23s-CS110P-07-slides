all: clean main slow

main:
	gcc main.c -g -o main

slow:
	gcc slow.c -g -o slow

clean:
	rm -rf main slow cache*

.PHONY: main slow clean all
