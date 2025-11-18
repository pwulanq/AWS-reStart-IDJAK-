# Tanpa for untuk mencetak angka 1 - n
print("angka 1")
print("angka 2")
print("angka 3")
print("angka 4")
print("angka 5")
print("angka 6")

#Refactoring kode diatas menggunakan loop for
for i in range(1,7):
    print(f"angka{i}")

for i in range(1,10001):
    print(f"angka{i}")

print("==range variation==")
myList = list(range(6))
print(myList)
myList = list(range(1,6))
print(myList)
myList = list(range(1,6,2))
print(myList)

for i, z in enumerate(myList):
    print(f"Nilai my list index ke {i} adalah {z}")

# Study case
namaSiswa = ["Prithvi", "Ginda", "Abdul", "Chistoper"]
for nm in namaSiswa:
    print (f"{nm} Hadir")

listNumber = [1, 2, 4, 100]
tempSum = 0
for ln in listNumber:
    tempSum = tempSum + ln
    