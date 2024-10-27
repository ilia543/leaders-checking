# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)