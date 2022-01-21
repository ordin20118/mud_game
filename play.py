from mud_game.modules.print_module import *
from mud_game.classes.person_class import Person
from mud_game.classes.farm_class import *
from classes.shop_class import *

player = Person('', '', 0) 
my_farm = Farm("")
veget_shop = VegetShop("야채 가게")

# 게임 플레이
def start_game():
    loop()


def loop():
    go_to = 0
    while True:        
        if go_to == 0:
            print(" ~ 환영합니다! %s님 ~" % player.name)
            go_to = 1
        elif go_to == 1: # 농장
            my_farm.print_menu()
            fram_op = int(input())

            if fram_op == 1:
                print_info_msg("텃밭으로 선택됨")
                pass
            elif fram_op == 2:
                print_info_msg("야채가게로 선택됨")
                veget_shop_proc()
            elif fram_op == 3:
                break
            elif fram_op == 4:
                f = open("./save_data.txt", "w")
                f.write("저장")
                f.close()
                break
            else:
                print_warning_msg("메뉴를 다시 확인하세요.")
        elif go_to == 2: # 시장
            pass

def garden_proc():
    while True:
        print("""
        1. 농작물 확인
        2. 재배하기
        3. 물주기
        4. 뒤로가기
        """)

        garden_op = int(input())

        if garden_op == 1:
            my_farm.print_crop_list()
        elif garden_op == 2:
            pass
        elif garden_op == 3:
            pass
        elif garden_op == 4:
            pass

def veget_shop_proc():
    
    while True:
        
        veget_shop.print_menu()

        garden_op = int(input())

        if garden_op == 1:
            pass
        elif garden_op == 2:
            pass
        elif garden_op == 3:
            pass
        elif garden_op == 4:
            pass




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

            import mud_game.load
            
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
            print("     !!! 잘못된 메뉴 번호 입니다. !!!    ")
