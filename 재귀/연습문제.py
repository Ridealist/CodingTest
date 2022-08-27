def num(n):
    if n > 1:
        num(n-1)
    print(n)

# num(10)


# a, b = input().split()
# a = int(a)
# b = int(b)

def num(a,b):
    if a%2 == 0:
        if a+1 <= b:
            print(a+1)
    else:
        print(a)
    if a+2 <= b:
        num(a+2, b)

# num(a, b)


n = input()
n = int(n)

def sum(n):
    if n > 1:
        return n + sum(n-1)
    return n

print(sum(n))


def recursive_function(i):
    if i == 100:
        print(i, "번째 재귀 함수를 종료합니다.")
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀 함수를 종료합니다.")

recursive_function(1)