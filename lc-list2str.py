#!/usr/bin/env python
# Mikhail Kolodin
# lc-list2str.py 2023-10-12 2023-10-12 1.0

def solve(word1, word2):
    """solve 1 task"""

    return "".join(word1) == "".join(word2)

def test(word1, word2):
    """run 1 test"""

    print(f"\n{word1=}, {word2=} => {solve(word1, word2)}")    


test(word1 = ["ab", "c"], word2 = ["a", "bc"])
test(word1 = ["a", "cb"], word2 = ["ab", "c"])

# word1=['ab', 'c'], word2=['a', 'bc'] => True
# word1=['a', 'cb'], word2=['ab', 'c'] => False

# Проверка соответствия строк в двух списках

#  (https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)
# 
# Сложность: Лёгкая 

# Условие задачи: на вход подаются два строковых массива, необходимо вернуть true, если два массива представляют одну и ту же строку, false  в противном случае.

# Под представлением одной и той же строки подразумевается, что после конкатенации всех фрагментов списков, две полученные строки будут идентичными.

# Пример:

# Ввод: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Вывод: true

# Объяснение:
# word1: "ab" + "c" -> "abc"
# word2: "a" + "bc" -> "abc"

# Ввод: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Вывод: false

# Решение задачи (https://telegra.ph/Proverka-sootvetstviya-strok-v-dvuh-spiskah-Reshenie-zadachi-10-26)
