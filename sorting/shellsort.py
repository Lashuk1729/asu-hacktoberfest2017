# -*- coding: utf-8 -*-
"""
@author: Lashuk1729

Just a simple implementation of the selectionsort algo
"""

def shell_sort(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

a = [12, 33, 1, 3, 54, 32, 78, 54, 99, 6]
print(a)
shell_sort(a)
print(a)
