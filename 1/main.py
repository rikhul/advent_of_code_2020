numbers = []
for l in open("input.txt"):
    numbers.append(int(l))

for i, n in enumerate(numbers):
    for n2 in numbers[i:]:
        if n+n2 == 2020:
            print(n,n2,n*n2)
            break


here:
for i, n in enumerate(numbers):
    for i2, n2 in enumerate(numbers[i:]):
        for n3 in numbers[i2:]:
            if n+n2+n3 == 2020:
                print(n,n2,n3, n*n2*n3)
                break
