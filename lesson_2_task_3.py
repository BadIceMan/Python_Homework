def square(side):
    area = side * side
    if area % 1 == 0:
        return int(area)
    else:
        return int(area) + 1


print(square(5))
print(square(4.1))
