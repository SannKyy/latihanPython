a = input("masukan angka: ").split()

jadiAngka = []

for angka in a:
    jadiAngka.append(int(angka))

n = len(jadiAngka)
#mean
total = 0

for i in jadiAngka:
    total += i

if n == 0:
    print("data kosong")
else:
    mean = total/n
    print(mean)

#median
for i in range(n):
    for j in range(n-1):
        if jadiAngka[j]>jadiAngka[j+1]:
            temp = jadiAngka[j]
            jadiAngka[j] = jadiAngka[j+1]
            jadiAngka[j+1] = temp




if n % 2 != 0:
    median = jadiAngka[n//2]
else:
    median = (jadiAngka[n//2] + jadiAngka[(n//2)-1])/2

print("median nya adalah:", median)


