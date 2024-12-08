def func(numbs):
    #ჯერ გვჭირდება დასორტირება რათა რიცხვები ზრდადობით დაიწეროს
    numbs.sort()

    l = 1
    numb = 1

    #ჯერ უნდა გადავუაროთ რიცხვებს 1 დან ლისთსი სიგრძემდე ფორ ციკლით
    for i in range(1, len(numbs)):
        #შემდეგ გვჭირდება if-ი რომელიც ნახავს არის თუ არა ტოლი რიცხვი და მისი წინა რიცხვი
        if numbs[i] != numbs[i - 1]:
            #თუ არ არის ტოლი მაშინ უნდა შევამოწმოთ რიცხვი 1ით მეტია თუ არა წინა რიცხვზე
            if numbs[i] == numbs[i - 1] + 1:
                numb +=1

            else:
                if numb > l:
                    l = numb

                numb = 1

    if numb > l:
        l = numb

    return l
print(func([100, 4, 200, 1, 3, 2]))
print(func([0, 0]))
print(func([9, 1, 4, 7, 3, 2, 8, 5, 6]))