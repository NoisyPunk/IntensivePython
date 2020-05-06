# hour_cost = int(input('Hourcost >> '))
# day_quantity = int(input('Days >> '))

def salary(hour_cost, day_quantity):
    total = (hour_cost * 8) * day_quantity
    ndfl = total * 0.87

    return ndfl

a = salary(600, 2)
b = salary(1200, 6)

print(a, b)