import datetime

num = datetime.datetime.now()
month = num.month

if 3 <= month <= 5:
    print("현재는 봄입니다")
elif 6 <= month <= 8:
    print("현재는 여름입니다")
elif 9 <= month <= 11:
    print("현재는 가을입니다")
elif month == 12 or 1 <= month <= 2:
    print("현재는 겨울입니다")

