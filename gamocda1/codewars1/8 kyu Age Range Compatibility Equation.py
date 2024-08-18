def dating_range(age):
    age = 17
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = age // 2 + 7
        max = (age - 7) * 2
    return str(min) + "-" + str(max)
dating_range(17)