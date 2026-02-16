#akar kuadrat
n = float(input("Masukkan angka: "))

x = n / 2  # tebakan awal

for i in range(10):  # ulangi 10 kali
    x = 0.5 * (x + n / x)

print("Akar kuadrat =", x)
