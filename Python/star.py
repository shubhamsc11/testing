n = int(input("Please enter the length: "))
a = "*****"
l = []

for x in range(n):
    s = a[x:n]
    s=" ".join(s)
    s = s.center((4*n)-3)
    print(s)

    l.append(s)

# print(l)
# print("\n".join(l[:0:-1]+l))
