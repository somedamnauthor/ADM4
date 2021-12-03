CC=gcc
CFLAGS=-Wformat=2 -Wextra -Wall -Wpedantic -Werror -pedantic-errors -O3
BINARIES=\
	ADM-2021-A4-sort-branched-inplace \
	ADM-2021-A4-sort-predicated-inplace \
	ADM-2021-A4-sort-branched-outoffplace \
	ADM-2021-A4-sort-predicated-outoffplace

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

.PHONY: all clean

all: $(BINARIES)

clean:
	rm -v $(BINARIES)
