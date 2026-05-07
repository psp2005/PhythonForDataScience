#time, datetime, any other library
import time
#from A(모듈/패키지) import B(작은 단위 클래스/함수/변수)
from datetime import datetime

firstStr = "Seconds since January 1, 1970: "
timeDotTime = time.time()
secondStr = " or "
timeExponent = ""
thirdStr = " in scientific notation"
# todayStr = time.

print(f"time.time(): {time.time()}\n")
print(f"time.strftime(): {time.strftime("%b %d %Y")}\n" )