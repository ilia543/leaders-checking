import math
def func(list1):
    list2 = []
    #უნდა შევქმნათ ფორ ციკლი რომელიც გადაუვლის მთლიან სტრინგს და შეამოწმებს არის თუ არა იგი 0ზე მეტი ამის შემდეგ თუ მეტია 0ზე დაემატება ლისთ2-ს და საბოლოოდ დავაბრუნებ მათ ჯამს. აქ უბრალოდ დავუმატე floor იმისთვის რომ გადავიყვანო ისინი უახლოეს მთელ რიცხვში
    for i in list1:
        if i > 0:
            i = math.floor(i)
            list2.append(i)
    return sum(list2)

print(func([1, -4, 7, 12]))
print(func([-1.5, 2.7, -3.3, 4.8]))
print(func([]))
print(func([-1, -2, -3]))