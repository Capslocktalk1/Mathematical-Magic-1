
n = int(input("Enter a number: "))

d = len(str(n))

result = 0

temp = n

while temp > 0 :
    num = temp % 10
    result += num**d
    temp //= 10


if n == result:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")