#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
global lst
lst = [0] * 1000000

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert (i > 0 and i < 1000000)
    assert (j > 0 and j < 1000000)
    if (i <= j):
        return collatz_maxcl(i, j)
    else:
        return collatz_maxcl(j, i)

# ------------
# collatz_maxcl
# ------------

def collatz_maxcl (i, j) :
    """
    i the beginning of the range, inclusive
    j the end of the range, inclusive
    return max cycle length of the range [i, j]
    """
    assert (i > 0 and i < 1000000)
    assert (j > 0 and j < 1000000)
    max = 0
    while (i <= j):
        n = collatz_cycle_length(i)
        if (n > max):
            max = n
        i += 1
    assert (max > 0)
    return max

# ------------
# collatz_cycle_length
# ------------

def collatz_cycle_length(i):
    """
    i is the current number to find the cycle length of
    if odd multiply by 3 and add 1
    if even divide by two
    continue until reached 1
    """
    assert (i > 0)
    current = i
    if (current < 1000000 and lst[current] != 0):
        return lst[i]
    c =1
    while i > 1 :
        if (i < 1000000 and lst[i] != 0):
           k = c - 1 + lst[i]
           lst[current] = k
           return k
        if (i % 2) == 0 :
            i = (i // 2)
        else :
            i = (3 * i) + 1
        c += 1
    assert (c > 0)
    lst[current] = c
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
