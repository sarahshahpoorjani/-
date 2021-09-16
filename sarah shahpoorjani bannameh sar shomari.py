#برنامه سرشماری
result = ""
marital_number = 0
afrad = int(input("لطفا تعداد افراد خانواده را وارد کنید!"))
tedad = 1
while tedad <= afrad:
    tedad = tedad + 1
    name = input("نام و نام خانوادگی خود را وارد کنید!")
    jender = input("جنسیت خود را وارد کنید!")
    live = input("فرد مورد نظر در قید حیات میباشد؟")
    if live == "خیر":
        result += "نام و نام خانوادگی: " + name + " جنسیت: " + jender + " وضعیت حیات: " + live + "\n"
        continue
    age = int(input("سن خود را وارد کنید!"))
    if age < 18:
        result +="نام و نام خانوادگی: " + name + " جنسیت: " + jender + " وضعیت حیات: " + live + " سن: " + str(age) +"\n"
        continue
    if age >= 18:
        educational = input("میزان تحصیلات خود را وارد کنید!")
        occupational = input("آیا شاغل هستید؟")
        if occupational == "بله":
            income =input("میزان درامد ماهانه خود را وارد کنید!")
        marital = input("وضعیت تاهل؟ {مجرد یا متاهل}")
        if occupational == "خیر":
            result += "نام و نام خانوادگی: " + name + " جنسیت: " + jender + " وضعیت حیات: " + live + " سن: " + str(
            age) + " میزان تحصیلات: " + educational + " وضعیت اشتغال: " + occupational + " وضعیت تاهل: " + marital + "\n"
        if occupational== "بله":
            result += "نام و نام خانوادگی: " + name + " جنسیت: " + jender + " وضعیت حیات: " + live + " سن: " + str(
                age) + " میزان تحصیلات: " + educational + " میزان درامد ماهانه: " + income + " وضعیت اشتغال: " + occupational + " وضعیت تاهل: " + marital + "\n"
        if marital == "متاهل":
            marital_number += 1
marital_number /= 2
print(result)
print("تعداد خانواده ها: " + str(int(marital_number)))