#!/usr/bin/env python3
import random
from typing import List

N = 30
SEED = 769

def insertion_sort(xs: List[int]) -> List[int]:
    arr = xs[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubblesort(xs: List[int]) -> None:
    n = len(xs)
    for i in range(n):
        for j in range(0, n - i - 1):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = xs[j + 1], xs[j]


if __name__ == "__main__":
    random.seed(SEED)
    data = [random.randint(-100, 100) for _ in range(N)]
    print("Input:", data)

    ins = insertion_sort(data)
    bub = data[:]
    bubblesort(bub)

    print("Insertion sort:", ins)
    print("Bubblesort:", bub)

    assert ins == sorted(data) == bub, "Sort differ from default sorted()!"
    print("Verification with sorted() -> OK")
