# Cache

## 1. Introduction

1. What's the difference between `cache` and `buffer`?
   
   ```c
   |
   |
   ```

2. Why we `cache`, do we still need `memory`?

3. What CPU do when waiting for memory? Stall.

## 2. Indexing cache & Associativity

1. Assume a 4-way set associative cache (Tag:21 | Index:5 | Offset:6)
   
   1. `Block size`
   2. `# of possible offsets`
   3. `# of possible indices`
   4. `# of cache blocks`
   5. `Total capacity of cache`

2. Assume a 8-way set associative cache (Tag:17 | Index:8 | Offset:7)
   
   1. `Block size`
   2. `# of possible offsets`
   3. `# of possible indices`
   4. `# of cache blocks`
   5. `Total capacity of cache`

3. Assume a cache (Tag:16 | Index:6 | Offset:10), with total size of `1MB`, what's the associativity?
   
   ```c
   // Write your answer here
   |
   |
   |
   |
   |
   |
   |
   |
   ```

4. (Optional) Assume a n-way set associative cache (Tag:t | Index:i | Offset:o)
   
   1. `Block size`
   2. `# of possible offsets`
   3. `# of possible indices`
   4. `# of cache blocks`
   5. `Total capacity of cache`

## 3. Replacement policy

Assume we have a 2-way associative cache, with 8-bit address, (Tag:4 | Index:2 | Offset:2), we use "LRU".

```c
0: 0b 1100 01 10
1: 0b 0110 01 01
2: 0b 1110 11 00
3: 0b 1100 01 10
4: 0b 0110 10 10
5: 0b 1111 01 11
```

<div>
<table style="border-collapse:collapse;border-spacing:0" class="tg"><tbody><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">Index</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">Visit</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">0</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">1</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">2</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">3</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">4</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">5</td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:center;vertical-align:middle;word-break:normal" rowspan="2">00</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot0</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot1</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:center;vertical-align:middle;word-break:normal" rowspan="2">01</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot0</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot1</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:center;vertical-align:middle;word-break:normal" rowspan="2">10</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot0</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot1</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:center;vertical-align:middle;word-break:normal" rowspan="2">11</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot0</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr><tr><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal">slot1</td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td><td style="border-color:#000000;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 20px;text-align:left;vertical-align:top;word-break:normal"></td></tr></tbody></table>
</div>



## 4. Something else

1. Why (Tag | Index | Offset) instead of (Index | Tag | Offset)?

2. Where is cache located at? (CPU / Memory)

3. Who controls cache? (CPU / OS)



## 5. Cachegrind

```shell
valgrind --tool=cachegrind ./main
```
