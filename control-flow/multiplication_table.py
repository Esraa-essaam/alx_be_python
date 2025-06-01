# طلب الرقم من المستخدم
number = int(input("Enter a number to see its multiplication table: "))

# توليد جدول الضرب من 1 إلى 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
