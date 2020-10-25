angka = int(input("Type odd or even number that you want: "))
# Ini adalah modulus
if angka % 2 == 0:
#   print("Bilangan {} adalah bilangan genap" .format(bilangan))
    print(f"The number {angka} even number")
    
else:
#   print("Bilangan {} adalah bilangan ganjil" .format(bilangan))
    print(f"The number {angka} is odd number")


nilai = int(input("Type your mid test score: "))
if nilai >=80:
    print("Exelent, you got A")
    print("Keep learning")

elif nilai >=70:
    print("Great, you got B")
    print("Study hard is the key")

elif nilai >=60:
    print("Not bed, you got C")
    print("Never stop learning")

elif nilai >=50:
    print("Sadly, you D")
    print("Spend your time to learn and keep focus")

else:
    print("Oh my god terrible, you got E, you didn't pass the exam:(")



inputbil = int(input("Type positif or Negatif number: "))
if inputbil >0:
    print("it's positif number")

elif inputbil <0:
    print("it's a negatif number")

else:
    print("it's zero")