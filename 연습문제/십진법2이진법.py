def DecimalToBinary(n):
    if n >= 1:
        DecimalToBinary(n//2)
        print(n%2)

DecimalToBinary(17)