#!/usr/bin/env python

# Mikhail Kolodin
# lc-flylow.py 2023-07-22 2023-07-22 1.1

def solve():
    global bestprice
    
    if n<1 or len(flights)<1 or src<0 or src>=n or dst<0 or dst>=n or k<0 or k>=n:
        return -1
    
    bestprice = -1

    dive(0, src, 0)

    return bestprice


def dive(level, curnode, curprice):
    global bestprice

    if curnode == dst:
        if bestprice == -1:
            bestprice = curprice
        else:
            if bestprice > curprice:
                bestprice = curprice
        return

    if level > k:
        return

    for flight in [f for f in flights if f[0] == curnode]:
        dive(level+1, flight[1], curprice+flight[2])
    

def test():
    """run 1 test"""
    
    print(f"{n=}, {flights=}, {src=}, {dst=}, {k=} => {solve()}")


n = 4 
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
test()

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
test()

n = 3
flights = [[0,1,100],[0,2,100]]
src = 2
dst = 1
k = 1
test()

n = 3
flights = [[0,1,100],[0,2,100]]
src = 0
dst = 0
k = 1
test()

n = 3
flights = [[0,1,100],[0,2,100]]
src = 2
dst = 2
k = 1
test()

# n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3, k=1 => 700
# n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1 => 200
# n=3, flights=[[0, 1, 100], [0, 2, 100]], src=2, dst=1, k=1 => -1
# n=3, flights=[[0, 1, 100], [0, 2, 100]], src=0, dst=0, k=1 => 0
# n=3, flights=[[0, 1, 100], [0, 2, 100]], src=2, dst=2, k=1 => 0

# Перелет с наименьшей ценой

#  (https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)Сложность: Средняя 

# Условие задачи: есть n городов, соединенных некоторым количеством рейсов. Вам предоставляется массив рейсов, где рейсы[i] = [fromi, toi, pricei] указывают, что есть рейс из города из i в город toi со стоимостью pricei.

# Вам также даны три целых числа src, dst и k, возвращающие самую дешевую цену из src в dst не более чем с k остановками. Если такого маршрута нет, верните значение -1.

# Пример:

# Ввод: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Вывод: 700

# Ввод: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Вывод: 200
