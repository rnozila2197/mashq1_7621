# 1
age = int(input("Yoshingizni kiriting: "))
if age > 18:
    print("Kattasisiz")
else:
    print("Kattasiz emas")


# 2
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
if a > b:
    print("Birinchi son katta")
else:
    print("Ikkinchi son katta")


# 3
num = int(input("Son kiriting: "))
if num > 0:
    print("Musbat son")
else:
    print("Manfiy son")


# 4
n = int(input("Raqam kiriting: "))
if n < 10:
    print("10 dan kichik")
elif n == 10:
    print("10 ga teng")
else:
    print("10 dan katta")

# 5
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
if x == y:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")


# 6
word = input("So'z kiriting: ")
if word == "hello":
    print("Salom!")
elif word == "bye":
    print("Xayr!")
else:
    print("Noma'lum so'z")
