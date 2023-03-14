# NOTICE: Sorry I mistyped `ra` as `sp`. There are so many of them and I'm just too lazy.



# Part 1

## Exercise `I-type`

### 1. Calculation

Write the value of `t1` in the following code snippets.

This part should take you no longer than 3 minutes.

```
# a2 = 0x1234
# a3 = 0xFFFFFFFF
# a4 = 0x8

addi t1 a4 0x8
# What is the value of t1? ________________

addi t1 t1 -3
# What is the value of t1? ________________

ori t1 a3 0x246
# What is the value of t1? ________________

andi t1 a4 -1
# What is the value of t1? ________________

slli t1 a3 4
# What is the value of t1? ________________

srli t1 a3 4
# What is the value of t1? ________________

srai t1 a3 4
# What is the value of t1? ________________
```

### 2. Load data from memory

Write the value of `t1` in the following code snippets.

```
.data
number:
.word 0x01234567 0x89ABCDEF

.text
la t0 number

lw t1 0(t0)
# What is the value of t1? ________________

lb t1 0(t0)
# What is the value of t1? ________________

lb t1 3(t0)
# What is the value of t1? ________________

lh t1 1(t0)
# What is the value of t1? ________________

lw t1 3(t0)
# What is the value of t1? ________________

lhu t1 5(t0)
# What is the value of t1? ________________

lh t1 5(t0)
# What is the value of t1? ________________

lbu t1 7(t0)
# What is the value of t1? ________________

lb t1 7(t0)
# What is the value of t1? ________________
```

---

## Exercise `S-type`

Image what the memory section is like.

```
.data
number:
.word 0x01234567 0x89ABCDEF
.text
la t0 number
li t1 0x91

sw t1 0(t0)
sw t1 3(t0)
sb t1 2(t0)
sh t1 6(t0)
```

---

## Exercise `B-type`

## 1. Jump or not?

Decide whether the following commands jump to `label_1`:

```
label_1:
nop              # Stands for "pass"
nop              # Stands for "pass"
li t0 0x123ABC
li t1 0xFFFFFFFF
li t2 0x321321
li t3 0x321321

beq t2 t3 label_1
# Do we jump to label_1? _______________

bne t2 t3 label_1
# Do we jump to label_1? _______________

blt t1 t2 label_1
# Do we jump to label_1? _______________

bltu t1 t2 label_1
# Do we jump to label_1? _______________
```

## 2. Calculate offset

```
label_2:
nop
nop
beq x0 x0 label_2
```

Please write down the **offset** of `beq`.

What's the value of `imm` field in `beq`?

---

## Exercise `Jal, Jalr`

### 1. Jal

Try to tell what happened in `jal`

```
0  nop
1  jal sp label_1
2  nop
3  nop
   label_1:
   # Remember labels don't take space!
4 nop
```

1. `sp` is set to `0x8`

2. `PC` is set to `0xC`

### 2. Jalr

What happened after `jalr`?

```
0 la t0 label_2
1 jalr sp t0 4
2 nop
3 nop
  label_2:
4 nop
5 nop
```

1. `sp` is set to `0xC` (the first `nop`)

2. `PC` is set to `0x18` (the last `nop`)

---

# Part 2

This section is designed for those who find difficulty in programming and finding bugs.

```c
int a;

int func(int b) {
    static long long c = 1023;
    b += 100;
    return b - 5;
}

int main() {
    char *string = malloc(50);
    return 0;
}
```

Where are the following variables stored?

1. `a`

2. `b`

3. `c`

4. `string`

5. `string[2]`

Which of the following variables are never initialized?

1. `a`

2. `b`

3. `c`

4. `string`

5. `string[2]`
