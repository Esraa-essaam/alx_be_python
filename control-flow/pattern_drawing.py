# طلب حجم النمط من المستخدم
size = int(input("Enter the size of the pattern: "))

# التأكد أن الحجم موجب
if size > 0:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # ينزل لسطر جديد بعد كل صف
        row += 1
else:
    print("Please enter a positive integer.")
