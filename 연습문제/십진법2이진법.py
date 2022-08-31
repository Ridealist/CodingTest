def DecimalToBinary(n):
    if n > 1:
        return DecimalToBinary(n//2) + str(n%2)
    return str(n)


print(DecimalToBinary(3))