def func(str1, str2):
    # ეს ძალიან მარტივია უბრალოდ sorted უნდა გამოვიყენოთ რაცა დასორტირდნენ ანბანის მიხედვით და მერე ერთმანეთს შევადაროთ 
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2

print(func("listen", "silent"))
print(func("hello", "world"))
print(func("triangle", "integral"))