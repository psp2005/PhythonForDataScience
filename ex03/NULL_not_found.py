Nothing = None
#None
Garlic = float("NaN")
#nan 정의되지 않거나 표현할 수 없는 수학적 계산 결과 ,예를 들어 0/0, 무한-무한, 음수의 제곱근
#기능1.정수를 실수로 변환 - float(10) = 10.0
#기능2. 문자열을 실수로 변환 - input()함수로 사용자로 부터 입력을 받을 때 num = float("123")을 하면 실제로 num은 실수 123이 된다 - atoi()같은 기능이 내장되어 있나보다
#기능3. 특수 기호 처리 - 파이썬 내부에는 True나False처럼 Nan과 Infinity를 직접 타이핑할 수 있는 예약어가 없다
# 따라서 IEEE 754기준 숫자가 아님, 무한대를 특수한 실수 상태로 만들기 위해
# float()함수에 문자열을 집어넣는 방식을 약속으로 정한다, "nan", "NaN", "NAN", "nAn"처럼 대소문자 구분하지 않는다
Zero = 0
#0
Empty = ""
#""
Fake = False
#False

case = [Nothing, Garlic, Zero, Empty, Fake]


def NULL_not_found(obj: any) -> int:
    if obj is None:#if type(obj) == type(None)
        print("Nothing:", obj, type(obj))
    elif isinstance(obj, float): #type(obj) is float, type(obj) == float
        print("Cheese:", obj, type(obj))
    #bool타입은 int타입의 서브클래스(자식)이다 True는 내부적으로 1, False는 내부적으로 0이다 
    #그래서 만약 아래 if조건문을 isinstance(obj, int)로 두면 bool형도 이 조건문에 걸려 버그를 발생할 것이다
    elif type(obj) is int:
        print("Zero:", obj, type(obj))
    elif type(obj) == str and len(obj) == 0 :
        print("Empty:", obj, type(obj))
    elif isinstance(obj, bool):
        print("Fake:", obj, type(obj))
    else:
        print("Type not Found")
        return 1
    return 0

