#!/usr/bin/env python

# Mikhail Kolodin, 2023-04-18
# exipath.py 2023-04-18 2023-04-18 1.0

def way(n, edges, source, destination):
    """determine existence of the path"""
    
    if source == destination:
        return True

    links = []
    for edge in edges:
        links += [edge]
        links += [edge[::-1]]

    passed = []
    que = [source]

    need = True
    while need:
        if not que:
            return False
        
        weat = que[0]
        que = que[1:]
        passed.append(weat)

        for vert in links:
            f, t = vert
            if f != weat or t in passed:
                continue
            if t == destination:
                return True
            que.append(t)

    return False   


# tests

print( way(3, [[0, 1], [1, 2], [2, 0]], 0, 2) )
print( way(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) )

# True
# False

# Нахождение существующего пути

#  (https://leetcode.com/problems/find-if-path-exists-in-graph/)Сложность: Лёгкая 

# Условие задачи: дается ненаправленный граф, ребра которого представлены в массиве. Между каждой парой узлов в дереве имеется не более одного ребра.

# Необходимо определить существует ли корректная дорога между узлом source и destination.

# Пример:

# Ввод: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Вывод: true
# Объяснение: *во вложении

# Ввод: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Вывод: false
