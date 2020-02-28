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
#threading을 어떤 식으로 응용할 것인지 제대로 구상해야함.
#또한 class와 run으로 구현할 것인지 함수로서만 구현할 것인지도 구상해야함.
def Now_ticketing(msize, Msize):
    ticket_sell = [num + 1 for num in range(msize,Msize)] #size크기의 리스트 생성
    while ticket_sell:#티켓이 무작위로 팔림
        print(random_pop(ticket_sell))
        time.sleep(1/1000,1) #0.001초~1초에 한 장씩 팔림

#시뮬레이터 모듈의 전신
def simulater_for_ticketing(size):
    to_hund = threading.Thread(target = Now_ticketing, args = (0, 100)) #100번대 이하의 티켓이 무작위로 팔림
    to_Two_hund = threading.Thread(target = Now_ticketing, args = (100, 200))
    to_all = threading.Thread(target = Now_ticketing, args = (200, size))#200번대 이상 모든 티켓이 무작위로 팔림

# 각 함수 실행하기 전에 1초의 텀을 가짐
to_hund.start()
time.sleep(1)
to_Two_hund.start()
time.sleep(2)
to_all.start()
