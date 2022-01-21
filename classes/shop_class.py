from mud_game.classes.food_class import Food
from mud_game.classes.item_class import Item
from mud_game.classes.person_class import Person

# 상점 클래스
# 속성
#   - name: 상점 이름
#   - sell_list: 판매 물품 목록
# 기능
#   - 상품 목록 조회
#   - 상품 추가
#   - 상품 구매
#   - 상품 판매
class Shop:

    def __init__(self, name):
        self.name = name
        self.sell_list = []

    # 상품 추가
    def add_item(self, item: Item):
        
        if type(item) != Item:
            print("판매 상품으로 추가할 수 없는 아이템입니다.")
            return 0

        print("==== Add Item!!! ====")
        print(item)
        self.sell_list.append(item)
        print("="*30)

    # 상품 목록 출력
    def print_sell_list(self):
        i = 1
        for item in self.sell_list:
            print(" %d. %s" % (i,item))
            i += 1
        print("구매할 아이템 번호를 선택해 주세요: ")

    def buy_item(self, person: Person, item_num: int):
        item = self.sell_list[item_num]
        print("아이템 %s을 구입했습니다." % item.name)
        # 아이템 구매에 의한 금액 차감 및 소지품 추가

# 야채 가게  클래스
class VegetShop(Shop):
    def add_item(self, vegetable: Food):
        
        if type(vegetable) != Food:
            print("판매 상품으로 추가할 수 없는 아이템입니다.")
            return 0

        self.sell_list.append(vegetable)

    def print_menu(self):
        print("""
        1. 구매하기
        2. 판매하기
        3. 뒤로가기
        """)



if __name__ == "__main__":
    vegetable_shop = Shop("야채 가게")
    vegetable_shop.print_sell_list()

    # 음식 객체 데이터 생성
    carrot = Food("당근", 100, 5, 10, 0, 3)
    sweet_potato = Food("고구마", 300, 30, 20, 4, 15)
    person = Person("철수", "M", 19)

    print("="*40)
    veget_shop2 = VegetShop("야채 가게2")
    veget_shop2.add_item(carrot)
    veget_shop2.add_item(sweet_potato)
    veget_shop2.add_item(person)
    veget_shop2.print_sell_list()





