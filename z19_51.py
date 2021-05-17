a = int(input())
b = a // 10 % 10
sum1 = a// 100 + b
sum2 = b+ a % 10
print(str(max(sum1, sum2)) + str(min(sum1, sum2)))

