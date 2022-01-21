# 아이템 클래스 - 게임 내에서 사용되는 모든 아이템의 부모
# 속성
#   - name: 이름
#   - price: 가격
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def print_item_name(self):
        print("이 아이템의 이름은 %s 입니다." % self.name)