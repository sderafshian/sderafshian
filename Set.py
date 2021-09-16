list1 = []
i = 1
while i <= 5:
    name = input("نام خود را وارد کنید.\n")
    list1.append(name)
    i = i + 1
name1 = set(list1)
print(name1)
print("تعداد اسامی بدون تکرار: ")
print(len(name1))