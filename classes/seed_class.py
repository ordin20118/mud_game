from time import time
from mud_game.classes.item_class import Item
import random

# 씨,종자 클래스
# 작물을 얻기 위한 종자를 나타내는 클래스
# 속성
#   - name: 음식 이름
#   - price: 가격
#   - state: 상태 (max: 100, min:0) (수분 공급을 받지 못하면 감소, 0이될 경우 시듦)
#   - time: 성장 시간(기준: 초)
#   - harvest_cnt: 수확량(성장이 완료되면 얻는 수확물의 최대 개수)
#   - growth_power: 성장력 => 해당 작물의 성장력
# 기능
#   - 성장
class Seed(Item):
    
    UNIT_MIN = 60 * 1000
    UNIT_HOUR = UNIT_MIN * 60
    UNIT_DAY = UNIT_HOUR * 24
    UNIT_MONTH = UNIT_DAY * 31

    def __init__(self, name: str, price: int, time: int, harvest_cnt: int):
        self.name = name
        self.price = price
        self.time = time
        self.state = 100
        self.harvest_cnt = harvest_cnt
        self.growth_power = random.randrange(1,7)
        self.icon = ""

    def __str__(self):
        return "%s=> 가격:%d | 재배 기간: %s | 수확량: %d" % (self.name, self.price, self.get_left_time(), self.harvest_cnt)

    # 성장 기능
    # 작물의 성장력 만큼 성장한다.
    def grow(self):
        pass

    def get_left_time(self):

        month = int(self.time / self.UNIT_MONTH)
        day = int((self.time % self.UNIT_MONTH)/self.UNIT_DAY)
        hour = int((self.time - month*self.UNIT_MONTH - day*self.UNIT_DAY) / self.UNIT_HOUR)
        min = int((self.time - month*self.UNIT_MONTH - day*self.UNIT_DAY - hour*self.UNIT_HOUR) / self.UNIT_MIN)
        sec = int((self.time - month*self.UNIT_MONTH - day*self.UNIT_DAY - hour*self.UNIT_HOUR - min*self.UNIT_MIN) / 1000)

        time_str = ""

        if month > 0:
            time_str += "%dM " % month

        if day > 0:
            time_str += "%dd " % day
        
        if hour > 0:
            time_str += "%dh " % hour

        if min > 0:
            time_str += "%dm " % min

        if sec > 0:
            time_str += "%ds" % sec

        return time_str