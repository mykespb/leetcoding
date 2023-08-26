#!/usr/bin/env python
# Mikhail Kolodin
# lc-minbigger.py 2023-08-26 2023-08-26 1.1

def solve(letters: list[str], target: str) -> str:
    """solve complete task"""

    for c in letters:
        if c > target:
            return c

    return letters[0]

def test(letters: list[str], target: str) -> None:
    """run 1 test"""

    assert type(letters) == list
    assert type(target) == str
    assert len(letters)
    assert target

    print(f"{letters=}, {target=} => {solve(letters, target)}")    

test(letters = ["c","f","j"], target = "a")
test(letters = ["c","f","j"], target = "c")

# test([], "")

# letters=['c', 'f', 'j'], target='a' => c
# letters=['c', 'f', 'j'], target='c' => f


# Traceback (most recent call last):
#   File "/home/myke/pro/leetcoding/lc-minbigger.py", line 25, in <module>
#     test([], "")
#   File "/home/myke/pro/leetcoding/lc-minbigger.py", line 17, in test
#     assert len(letters)
# AssertionError

# Traceback (most recent call last):
#   File "/home/myke/pro/leetcoding/lc-minbigger.py", line 25, in <module>
#     test(['a'], "")
#   File "/home/myke/pro/leetcoding/lc-minbigger.py", line 18, in test
#     assert target
# AssertionError

# Минимальное большее 
#  (https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
# Сложность: Лёгкая

# Условие задачи: задан массив букв символов, отсортированных в порядке неубывания, и целевой символ. В буквах есть по крайней мере два разных символа.

# Необходимо вернуть наименьший символ в буквах, который лексикографически больше целевого. Если такого символа не существует, верните первый символ буквами.

# Пример:

# Ввод: letters = ["c","f","j"], target = "a"
# Вывод: "c"

# Ввод: letters = ["c","f","j"], target = "c"
# Вывод: "f"
