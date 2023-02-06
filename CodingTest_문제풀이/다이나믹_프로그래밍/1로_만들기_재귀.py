try:
    n = int(input())
except:
    print("wrong input")
    quit()


def find(n):
    n1 = n2 = n3 = n4 = n

    if n == 1:
        return 0
    
    if n == 2 or n == 3 or n == 5:
        return 1

    n1 = find(n - 1) + 1

    if n % 2 == 0:
        n2 = find(n // 2) + 1
    
    if n % 3 == 0:
        n3 = find(n // 3) + 1
    
    if n % 5 == 0:
        n4 = find(n // 5) + 1
    
    return min(n1, n2, n3, n4)


print(find(n))