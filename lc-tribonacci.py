#!/usr/bin/env python
# Mikhail Kolodin
# lc-tribonacci.py 2023-08-11 2023-08-11 1.0


def solve(n: int) -> int:
    """solve complete task"""
    
    assert n >= 0
    if n ==0: return 0
    if n < 3: return 1

    t0 = 0; t1 = t2 = 1
    for i in range(n-2):
        t0, t1, t2 = t1, t2, t0 + t1 + t2

    return t2


def test(n: int) -> None:
    """run 1 test"""
    print(f"task: {n=} => {solve(n)}")


test(4)
test(100)
test(1)
test(0)

for i in range(50):
    print(i, solve(i))

test(-1)

# task: n=4 => 4
# task: n=100 => 98079530178586034536500564
# task: n=1 => 1
# task: n=0 => 0
# 0 0
# 1 1
# 2 1
# 3 2
# 4 4
# 5 7
# 6 13
# 7 24
# 8 44
# 9 81
# 10 149
# 11 274
# 12 504
# 13 927
# 14 1705
# 15 3136
# 16 5768
# 17 10609
# 18 19513
# 19 35890
# 20 66012
# 21 121415
# 22 223317
# 23 410744
# 24 755476
# 25 1389537
# 26 2555757
# 27 4700770
# 28 8646064
# 29 15902591
# 30 29249425
# 31 53798080
# 32 98950096
# 33 181997601
# 34 334745777
# 35 615693474
# 36 1132436852
# 37 2082876103
# 38 3831006429
# 39 7046319384
# 40 12960201916
# 41 23837527729
# 42 43844049029
# 43 80641778674
# 44 148323355432
# 45 272809183135
# 46 501774317241
# 47 922906855808
# 48 1697490356184
# 49 3122171529233
# Traceback (most recent call last):
#   File "/home/myke/pro/leetcoding/lc-tribonacci.py", line 33, in <module>
#     test(-1)
#   File "/home/myke/pro/leetcoding/lc-tribonacci.py", line 22, in test
#     print(f"task: {n=} => {solve(n)}")
#                            ^^^^^^^^
#   File "/home/myke/pro/leetcoding/lc-tribonacci.py", line 9, in solve
#     assert n>= 0
# AssertionError

# Nое число Трибоначчи

#  (https://leetcode.com/problems/n-th-tribonacci-number/description/)
# Сложность: Лёгкая 

# Условие задачи: последовательность Трибоначчи Tn определяется следующим образом:

# T0 = 0, T1 = 1, T2 = 1 и Tn+3 = Tn + Tn+1 + Tn+2 для n >= 0.

# По заданному n, верните значение Tn.

# Пример:

# Ввод: n = 4
# Вывод: 4
# Объяснение: 
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4