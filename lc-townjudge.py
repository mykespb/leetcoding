#!/usr/bin/env python
# Mikhail Kolodin
# lc-townjudge.py 2023-10-20 2023-10-20 1.0

def solve(n, trust):
    """solve 1 task"""

    town = set( [ x for x in range(1, n+1)])
    kto = set( [ x[0] for x in trust])
    komu = set( [ x[1] for x in trust])
    poss = town - kto
    if not poss:
        return -1

    if (judge := poss.pop()) in komu:
        return judge
    else:
        return -1


def test(n, trust):
    """run 1 test"""

    print(f"\n{n=}, {trust=} => {solve(n, trust)}")

test(n = 2, trust = [[1,2]])
test(n = 3, trust = [[1,3],[2,3],[3,1]])


# n=2, trust=[[1, 2]] => 2

# n=3, trust=[[1, 3], [2, 3], [3, 1]] => -1

# Городской судья  
# (https://leetcode.com/problems/find-the-town-judge/)

# Сложность: Лёгкая 

# Условие задачи: в городе живёт n людей, проиндексированные с 1 до n. Пошел слух, что один из горожан является судьей. 

# Если в городе-таки имеется судья, то:

# 1. Судья никому не доверяет. 
# 2. Каждый горожанин, за исключением судьи, доверяет судье. 
# 3. Существует один и единственный человек, который удовлетворяет правилам 1 и 2. 

# На вход подается массив связей доверия между гражданами, где trust[i] = [ai, bi] обозначает, что ai доверяет жителю bi.

# Вывести надо индекс судьи или же -1 в случае отсутствия такового среди жителей города. 

# Пример:

# Ввод: n = 2, trust = [[1,2]]
# Вывод: 2

# Ввод: n = 3, trust = [[1,3],[2,3],[3,1]]
# Вывод: -1

# Решение задачи (https://telegra.ph/Gorodskoj-sudya-Reshenie-zadachi-10-13)