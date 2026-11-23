def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if prime(7):
    print("Prime Number")
else:
    print("Not Prime")