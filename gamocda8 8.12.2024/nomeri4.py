def func(str1):

    list1 = []
    max1 = 0

    #აქ დავწერე ფორ ციკლი რომელიც გადაუვლის სტრ1-ს
    for i in str1:
        #აქ თუ ეს ი არის ლისთში შემდეგ ნახოს რამდენჯერ არის ი ლისთში და სანამ ი არის ლისთში პირველი რიცხვი წაშალოს
        if i in list1:
            while i in list1:

                list1.pop(0)
        #საბოლოოდ ლისთ1ში ჩაჯდეს ი და დავაბრუნო მაქსიმალური ლისთის სიგრძე რომელიც იქნება პასუხი
        list1.append(i)
        max1 = max(max1, len(list1)) 
    
    return max1


print(func("abcabcbb"))
print(func("bbbbb"))
print(func(""))
print(func("pwwkew"))