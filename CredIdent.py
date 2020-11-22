"""

CredIdent

This is a tool to identify if a credit card number is valid

"""

number = input("Number: ")
number = [int(d) for d in number]
soma = 0

i = 0
for n in number[::-1]:
    if i % 2 == 0:
        soma = soma + n
    else:
        n = str(n * 2)
        n = [int(tmp) for tmp in n]
        soma = soma + sum(n)
    i = i + 1

digit = number[0] * 10 + number[1]

if soma % 10 == 0:
    if digit in [51, 52, 53, 54, 55] and len(number) == 16:
        print("MASTERCARD")
    elif digit in [34, 37] and len(number) == 15:
        print("AMEX")
    elif number[0] == 4 and len(number) == 12 or len(number) == 16:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")