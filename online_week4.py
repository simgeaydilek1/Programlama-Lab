# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:44:08 2020

@author: Administrator
"""


def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array [i] > array [left]:
        smallest = left
    if right <= length and array [smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)
        
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

my_array_1 = [8,10,3,4,7,15,1,2,16]

build_min_heap(my_array_1)

print(my_array_1)

def heapSort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array
        
my_array_1 = [8, 10, 3, 4, 7, 15, 1, 2, 16]
my_array_2 = heapSort(my_array_1)

print(my_array_1)
print(my_array_2)





