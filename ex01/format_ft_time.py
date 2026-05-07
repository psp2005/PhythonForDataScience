#time, datetime, any other library
import time
#from A(모듈/패키지) import B(작은 단위 클래스/함수/변수)
from datetime import datetime

current_time = time.time()
result = f"Seconds since January 1, 1970: {current_time:,} or {current_time:.2e} in scientific notation"

print(result)
print(time.strftime("%b %d %Y"))