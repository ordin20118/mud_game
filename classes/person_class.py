from mud_game.classes.food_class import Food
# 사람 클래스 - 사용자 또는 NPC의 객체가 된다.
# 속성
#   - name: 캐릭터 이름
#   - sex: 성별
#   - age: 나이
#   - balance: 보유 금액
#   - hp: 체력 (max: 100, min: 0)
#   - satiety: 포만감 (max: 100, min: 0)
#   - thirst: 갈증 (max: 100, min: 0)
#   - clean: 청결도 (max: 100, min: 0)
#   - money: 소지금 (초기 자금: 500원)
# 기능
#   - 먹기 
#   - 지불하기
#   - 
#   - 
class Person:

    MAX_HP = 100
    MAX_SATIETY = 100
    MAX_THIRST = 100
    MAX_CLEAN = 100

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age        
        self.balance = 0
        self.hp = 100
        self.satiety = 0
        self.thirst = 0
        self.satiety = 100
        self.clean = 100
        self.money = 500
        self.inventory = {}

    def add_item_to_inventory(item):
        self.inventory[item.name] = item
        

    def show_inventory(self):
        print("show_inventory()")
        inventory_list = list(self.inventory)
        i = 0
        for item in inventory_list:
            print("%d. %s" % (i,item))
        

    # 먹기
    #   - food: 먹을 음식
    # 1. 음식의 포만감 만큼 포만감을 증가
    # 2. 음식의 갈증도 만큼 갈증을 증가
    # 3. 음식의 청결도 만큼 청결도 감소
    # 4. 음식의 체력 회복도 만큼 체력 회복
    def eat(self, food: Food):

        print("%s(을)를 먹습니다." % food.name)
        
        # 포만감 증가
        if self.satiety + food.satiety >= self.MAX_SATIETY:
            self.satiety = 100
        else:
            self.satiety += food.satiety

        # 갈증 증가
        if self.thirst + food.thirst >= self.MAX_THIRST:
            self.thirst = 100
        else:
            self.satiety += food.satiety
        
        # 청결 감소
        if self.clean + food.clean >= self.MAX_CLEAN:
            self.clean = 100
        else:
            self.satiety += food.satiety

        # 체력 회복
        if self.hp + food.hp >= self.MAX_HP:
            self.hp = 100
        else:
            self.hp += food.hp
        