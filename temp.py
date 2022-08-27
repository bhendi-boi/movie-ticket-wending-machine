n = int(input())
for i in range(1, (2*n)):
    if i <= n:
        print("* " * i)
    else:
        if i == (2*n - 1):
            print("*" * (2*n - i), end="")
        else:
            print("* " * (2*n - i))
