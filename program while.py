n = int(input("masukkan nilai: "))
x = 0
while (x < n):
    if (10 ** x < n):
        y = x
    else:
        break
    x += 1

print("nilai terkecil dari 10^x < n adalah", 10 ** x )