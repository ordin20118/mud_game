from mud_game.classes.food_class import Food
from mud_game.classes.item_class import Item
from mud_game.classes.person_class import Person
from mud_game.modules.print_module import *

# 농장 클래스
# 속성
#   - name: 농장 이름
#   - sell_list: 판매 물품 목록
# 기능
#   - 메뉴 출력
#   - 농작물 목록 조회
class Farm:

    def __init__(self, name):
        self.name = name
        self.crops = []

    def print_menu(self):
        print("""
        1. 텃밭으로
        2. 야채가게로
        3. 메인 메뉴로
        4. 저장하기
        """)

    def print_crop_list(self):
        print_title("나의 농작물")
        
        if len(self.print_crop_list) == 0:
            print_info_msg("심어둔 농작물이 없습니다.")
        else:
            i = 1
        for crop in self.crops:
            print("%d. %s"%(i, crop.name))
        
        print_line()








