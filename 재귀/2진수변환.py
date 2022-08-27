"""
https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
"""



def tobinary(n):
    global bi
    if n == 1:
        return bi.append(1)
    return bi.append(tobinary(n//2))

bi = []

def DecimalToBinary(num):
     
    if num > 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

# return 값이 없는 함수는 print시 None값 반환

tobinary(5)
print(bi)