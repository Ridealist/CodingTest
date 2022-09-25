"""
https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
"""

# return 값이 없는 함수는 print시 None값 반환


def tobinary_recursive(n):
    global bi
    if n > 1:
        tobinary_recursive(n//2)
    return bi + str(n%2)


def tobinary_recursive(n):
    if n == 1:
        return "1"
    elif n == 0:
        return "0"
    return tobinary_recursive(n//2) + str(n%2)


## built-in 'bin()' func
def tobinary_builtin(n):
    return bin(n).replace("0b", "")


def tobinary_format(n):
    return "{0:b}".format(int(n))


## 반복문 사용
def tobinary_iter(n):
    answer = ""
    while n > 1:
        answer += str(n % 2)
        n = n // 2
    answer += "1"
    
    return answer[::-1]

print(tobinary_iter(9))