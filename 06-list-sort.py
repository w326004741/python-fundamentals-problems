#Write a function that returns the largest and smallest elements in a list - by Weichen Wang


import heapq # Import heaqp library to use the priority queue algorithm functions

grades = [32,43,45,424,11,66,77,88,99,999]
print(heapq.nsmallest(3,grades), heapq.nlargest(3,grades))