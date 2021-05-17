a = int(input("Возраст Антона:   "))
b = int(input("Восвраст Бориса:  "))
c = int(input("Возраст Виктора:  "))
if a > b and a > c:
    print("Антон старше всех")
elif b > a and b > c:
    print("Борис старше всех")
elif c > b and c > a:
    print("Виктор старше всех")
