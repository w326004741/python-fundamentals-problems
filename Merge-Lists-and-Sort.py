# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]
# by Weichen Wang



# make three empty lists called list1,list2,list3,respectively
list1 = []
list2 = []
list3 = []


print("Please enter 3 numbers for each list")

print("List 1")
for i in range (0,3): #using for loop set need enter float type number three times and append to the listItem as list1 
    listItem = float(input(str(i + 1) + ": "))
    list1.append(listItem)

print("List 2") #using for loop set need enter number three times and append to the listItem as list2
for i in range (0,3):
    listItem = float(input(str(i + 1) + ": "))
    list2.append(listItem)

list3 = list1 + list2 # Merge list1 and list2

print()
print("List 1: " + str(list1))
print("List 2: " + str(list2))
print("List 3: " + str(list3))
print("Sorted List: " + str(sorted(list3))) # sorted() funtion is sort the list3

