# num = input("정수를 입력")
# last_chracter = num[-1]
# last_number = int(last_chracter)

# if last_number == 0\
#     or last_number == 2\
#     or last_number == 4\
#     or last_number == 6\
#     or last_number == 8 :
#     print("짝수입니다")

# if last_number == 1\
#     or last_number == 3\
#     or last_number == 5\
#     or last_number == 7\
#     or last_number == 9 :
#     print("홀수입니다")

num = int(input("정수를 입력하세요"))

if(not (num%2)):
    print("짝수입니다")
else:
    print("홀수입니다")
