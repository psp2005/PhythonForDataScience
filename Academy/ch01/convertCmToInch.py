a= "10 20 30 40 50"
print(type(a).__name__)
print(a.split("0"))
inch = input("몇 인치 인지 입력하세요: ")
cm = float(inch) * 2.54
print("%dinch는 %dcm입니다" % (float(inch), cm))

