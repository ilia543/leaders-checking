def func(list1):
    
    # აქ შევქმენი 2 ჯამი 1 ყველა რიცხვის რომელიც 1 დან n-მდე არის ხოლო მეორე ლისთის ჯამი, შემდეგ ერთმანეთს გამოვაკელი და მივიღე საბოლოო რიცხვი რომელიც. 
    sum1 = sum(list1)


    numbs = len(list1) + 1
    sum2 = numbs * (numbs + 1) // 2

    if sum2 <= 3:
        return []
    else:
        return sum2 - sum1

print(func([1, 2, 4, 5]))
print(func([3, 5, 6, 1, 2]))
print(func([2]))