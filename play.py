from modules.print_module import *
from classes.person_class import Person
from classes.crop_manager import CropManager
from classes.farm_class import *
from classes.shop_class import *
from datetime import datetime
import os
import sys

# 실행 파일 만들 시 경로 설정을 위한 코드
try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())
 
player = Person('', '', 0) 
my_farm = Farm("")

farm_manager = None

# 게임 플레이
def start_game():
    main_loop()


def main_loop():
    
    farm_manager = CropManager("CropManager", my_farm)
    farm_manager.start()

    go_to = 0
    while True:        
        if go_to == 0:
            print(" ~ 환영합니다! %s님 ~" % player.name)
            go_to = 1
        elif go_to == 1: # 농장
            my_farm.print_farm_menu()
            fram_op = int(input("메뉴를 선택해주세요: "))

            if fram_op == 1:
                print_info_msg("밭으로 이동")
                garden_proc()
            elif fram_op == 2:
                print_info_msg("야채가게로 이동")
                veget_shop_proc()
            elif fram_op == 3:
                print_info_msg("씨앗가게로 이동")
                seed_shop_proc()
            elif fram_op == 4:
                break
            elif fram_op == 5:
                f = open("./data/save_data.txt", "w")
                f.write("저장")
                f.close()
                break
            else:
                print_warning_msg("메뉴를 다시 확인하세요.")
        elif go_to == 2: # 시장
            pass
 
def garden_proc():
    while True:
        my_farm.print_garden_menu()
        garden_op = int(input("메뉴를 선택해주세요: "))

        if garden_op == 1:  # 농작물 확인
            my_farm.print_crop_list()
        elif garden_op == 2:    # 농작물 심기 
            # 플레이어의 작물 아이템 확인 
            # 선택
            # 심기
            pass
        elif garden_op == 3:    # 수확하기
            pass
        elif garden_op == 4:    # 뒤로가기
            break

def veget_shop_proc():
    
    while True:
        
        veget_shop.print_menu()

        veget_shop_op = int(input("메뉴를 선택해주세요: "))

        if veget_shop_op == 1:
            veget_shop.print_sell_list()
            
            item_num = int(input("구매하실 아이템을 선택하세요: "))

            item = veget_shop.sell_list[item_num-1]
            

            # 소지금 확인
            # 인벤토리에 아이템 넣기 
            # 소지금 차감
            # 구매하고 메시지 확인 후 메뉴로 복귀
            if player.money - item.price < 0:
                print_warning_msg("소지금이 부족합니다.")
            else:

                player.money -= item.price
                print_info_msg("%s 아이템을 구매했습니다." % item.name)
            
            print_confirm_msg("확인")

        elif veget_shop_op == 2:
            pass
        elif veget_shop_op == 3:
            break
        else:
            print_warning_msg("메뉴를 다시 확인하세요.")

def seed_shop_proc():
     while True:
        
        seed_shop.print_menu()

        seed_shop_op = int(input("메뉴를 선택해주세요: "))

        if seed_shop_op == 1:
            seed_shop.print_sell_list()
            
            item_num = int(input("구매하실 아이템을 선택하세요: "))

            item = seed_shop.sell_list[item_num-1]
            if player.money - item.price < 0:
                print_warning_msg("소지금이 부족합니다.")
            else:
                player.add_item_to_inventory(item)
                player.money -= item.price
                print_info_msg("%s 아이템을 구매했습니다." % item.name)
                
            print_confirm_msg("확인")

            player.show_inventory()

        elif seed_shop_op == 2:
            pass
        elif seed_shop_op == 3:
            break
        else:
            print_warning_msg("메뉴를 다시 확인하세요.")



if __name__ == "__main__":
    print("... Welcome Farm Game ...")

    isEnd = False
    while True:
        print("""
        1. 게임시작
        2. 불러오기
        3. 종료
        """)

        op = int(input("메뉴를 선택하세요: "))
        if op == 1:
            
            name = ""
            while True:
                name = input("이름을 입력하세요: ")
                if len(name) > 0:
                    break

            sex = ""
            while True:
                print("""
                1. 남자        2. 여자
                """)
                sex = int(input("성별을 선택하세요: "))
                if sex == 1:
                    sex = "남자"
                    break
                elif sex == 2:
                    sex = "여자"
                    break
                                    
            age = 0
            while True:
                age = int(input("나이를 입력하세요: "))
                if age > 0:
                    break

            farm_name = ""
            while True:
                farm_name = input("농장 이름을 입력하세요: ")
                if len(farm_name) > 0:
                    break
                
            player = Person(name, sex, age)
            my_farm = Farm(farm_name)

            from mud_game.load import *
            
            print_info_msg("%s 농장으로 이동합니다." % my_farm.name)
            start_game()
        elif op == 2:
            try:
                f = open("./save_data.txt", "r")
            except FileNotFoundError as e:
                print_warning_msg("저장된 데이터가 없습니다.")
        elif op == 3:
            print_info_msg("프로그램을 종료합니다.")
            isEnd = True
            break
        else:
            print_warning_msg("잘못된 메뉴 번호 입니다.")
