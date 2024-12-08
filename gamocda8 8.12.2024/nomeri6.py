def func(list1, list2):
    list3 = []

    #აქ დავწერე ფორ ციკლი რომ გადავუარო ლისთ1-ს და შემდეგ if რომელიც ამოწმებს არის თუ არა ეს i ლისთ2-ში და თუ არ არის ლისტ3-ში
    for i in list1:
        if (i in list2) and (i not in list3):
            list3.append(i)

    return list3

print(func([1, 2, 3], [2, 3, 4]))
print(func([1, 1, 2], [1, 3]))
print(func([], [1, 2]))