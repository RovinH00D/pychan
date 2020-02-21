import time
import random
import threading

from ticketing import *

#랜덤하게 리스트에서 값을 pop하는 함수
def random_pop(data):
    number = random.randint(0, len(data)-1)
    time.sleep(random.random())
    return data.pop(number)

#size크기의 공연장에서 티켓이 무작위로 사라지는 함수
#threading을 통해서 다른 thread에서 타임 슬립 0.5초 1초를 통해서 각각 시작 타이밍을 다르게 설정
#또한 threading을 통해 티켓 예매하는 thread도 따로 둘 것.
def Concert_simulate(size):
    ticket_sell = [num + 1 for num in range(0,size)] #size크기의 리스트 생성
    while ticket_sell:#티켓이 무작위로 팔림
        print(random_pop(ticket_sell))
