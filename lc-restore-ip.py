#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-restore-ip.py 2024-01-17 2024-01-17 1.0

def solve(s: str) -> list[str]:
    """solve 1 task"""

    lens = len(s)
    assert lens >= 4

    result = []

    for d1 in range(1, 4):
        
        fin = d1
        if fin > lens:
            continue

        s1 = s[:d1]

        if s1[0] == '0' and len(s1) > 1:
            continue

        n1 = int(s1)

        if n1 > 255:
            continue

        for d2 in range(1, 4):

            fin = d1+d2
            if fin > lens:
                continue

            s2 = s[d1 : fin]

            if s2[0] == '0' and len(s2) > 1:
                continue

            n2 = int(s2)

            if n2 > 255:
                continue

            for d3 in range(1, 4):

                fin = d1+d2+d3
                if fin > lens:
                    continue

                s3 = s[d1+d2 : d1+d2+d3]

                if s3[0] == '0' and len(s3) > 1:
                    continue

                n3 = int(s3)

                if n3 > 255:
                    continue

                d4 = lens - d1 - d2 - d3
                if d4 > 3:
                    continue

                s4 = s[d1+d2+d3:]

                if s4[0] == '0' and len(s4) > 1:
                    continue

                n4 = int(s4)

                if n4 > 255:
                    continue

                result.append(s1+'.'+s2+'.'+s3+'.'+s4)

    return result


def test(s: str): 
    """ show """
    
    print(f"{s=} -> {solve(s)}")


test("25525511135")
test("0000")

# s='25525511135' -> ['255.255.11.135', '255.255.111.35']
# s='0000' -> ['0.0.0.0']

# Восстановить IP (https://leetcode.com/problems/restore-ip-addresses/description/)
#  (https://leetcode.com/problems/restore-ip-addresses/description/)
# Сложность: Средняя

# Условие задачи: действительный IP-адрес состоит ровно из четырех целых чисел, разделенных одиночными точками. Каждое целое число находится в диапазоне от 0 до 255 (включительно) и не может содержать начальных нулей.

# Например, "0.1.2.201" и "192.168.1.1" являются допустимыми IP-адресами, но "0.011.255.245", "192.168.1.312" и "192.168@1.1 " являются недопустимыми IP-адресами.
# Учитывая строку s, содержащую только цифры, верните все возможные действительные IP-адреса, которые могут быть сформированы путем вставки точек в s. Вам не разрешается изменять порядок или удалять какие-либо цифры в s. Вы можете вернуть действительные IP-адреса в любом порядке.

# Пример:

# Ввод: s = "25525511135"
# Вывод: ["255.255.11.135","255.255.111.35"]

# Ввод: s = "0000"
# Вывод: ["0.0.0.0"]