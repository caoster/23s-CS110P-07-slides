import random

TOTAL_BIT = 32
TAG_BIT = 21
INDEX_BIT = 5
OFFSET_BIT = TOTAL_BIT - TAG_BIT - INDEX_BIT

ASSOCIATIVITY = 4

cache = [[] for _ in range(2 ** INDEX_BIT)]


def getValFromMem(addr):
    return str(hex(random.randint(0, 2 ** (8 * (2 ** OFFSET_BIT)) - 1)))[2:]


def log(*args):
    pass
    # print(*args)


def cache_log(*args):
    pass
    print(*args)


def disp_cache(hide_empty=False):
    print("Printing cache: ")
    for index, line in enumerate(cache):
        if hide_empty and len(line) == 0:
            continue
        print(f"{bin(index):<8}", end="")
        for i in line:
            print(i["tag"], end=" ")
        print()
    print("Finish printing!", end="\n\n")


def read(addr: str):
    addr = addr.replace(" ", "")
    assert len(addr) == TOTAL_BIT
    tag_field = int(addr[0:TAG_BIT], 2)
    index_field = int(addr[TAG_BIT + 1:-INDEX_BIT], 2)
    offset_field = int(addr[-INDEX_BIT - 1:TOTAL_BIT], 2)

    log(f"{'Reading: ':<10}", bin(int(addr, 2)))
    log(f"{'Tag: ':<10}", bin(tag_field))
    log(f"{'Index: ':<10}", bin(index_field))
    log(f"{'Offset: ':<10}", bin(offset_field))

    cache_line = cache[index_field]
    for i in cache_line:
        if i["tag"] == tag_field:
            cache_log("Cache Hit!")
            return "0x" + i["data"][offset_field * 2:offset_field * 2 + 2]

    cache_log("Cache Miss!")
    if len(cache_line) != ASSOCIATIVITY:
        cache_line.append({"tag": tag_field, "data": getValFromMem(addr)})
    else:
        cache_line.pop(0)  # remove the first entry
        cache_line.append({"tag": tag_field, "data": getValFromMem(addr)})
    return "0x" + cache_line[-1]["data"][offset_field * 2:offset_field * 2 + 2]


print("Different offsets")
print(read("11111111 11011111 11111111 10000000"))
print(read("11111111 11011111 11111111 10000000"))
print(read("11111111 11011111 11111111 10000001"))
print(read("11111111 11011111 11111111 10000010"))

print("Different tags")
print(read("11111100 11011111 11111111 10000010"))
print(read("11111101 11011111 11111111 10000010"))
print(read("11111110 11011111 11111111 10000010"))
print(read("11111111 11011111 11111111 10000010"))

disp_cache()

print("Different indices")
print(read("11111111 11011111 11111111 10000010"))
print(read("11111111 11011111 11111111 10100010"))
print(read("11111111 11011111 11111111 11000010"))
print(read("11111111 11011111 11111111 11100010"))

disp_cache(True)

# conflict
print(read("11101111 11011111 11111111 10000000"))
disp_cache(True)
