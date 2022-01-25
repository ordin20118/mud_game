from mud_game.classes.food_class import Food
from mud_game.classes.crop_class import Crop
from mud_game.classes.seed_class import Seed
from mud_game.classes.shop_class import *
from mud_game.classes.farm_class import *
from mud_game.modules.print_module import *
import json

print_info_msg("게임 데이터 초기화중")


# Init Crops
carrot = Crop("당근", 100, 5, 10, 0, 3)
carrot.set_icon("🥕")

corn = Crop("옥수수", 150, 20, 8, 4, 4)
corn.set_icon("🌽")

sweet_potato = Crop("고구마", 500, 30, 20, 4, 15)
sweet_potato.set_icon("🍠")

apple = Crop("사과", 300, 30, 5, 4, 20)
apple.set_icon("🍎")

strawberry = Crop("딸기", 400, 22, 6, 5, 15)
strawberry.set_icon("🍓")

grape = Crop("포도", 450, 20, 20, 8, 20)
grape.set_icon("🍇")


# Init Places
veget_shop = VegetShop("야채 가게")
veget_shop.add_item(carrot)
veget_shop.add_item(corn)
veget_shop.add_item(sweet_potato)
veget_shop.add_item(apple)
veget_shop.add_item(strawberry)
veget_shop.add_item(grape)


seed_shop = VegetShop("씨앗 가게")


# Init Seeds
try:
    f_seed = open("./data/seed_data.txt", "r")

    while True:
        line = f_seed.readline()
        if not line: break
        seed_json = json.loads(line)

        time_str = seed_json['time']
        time_arr = time_str.split()

        time = 0
        for t in time_arr:
            if t[-1] == "M":
                time += int(t[0:-1]) * Seed.UNIT_MONTH
            if t[-1] == "d":
                time += int(t[0:-1]) * Seed.UNIT_DAY
            if t[-1] == "h":
                time += int(t[0:-1]) * Seed.UNIT_HOUR
            if t[-1] == "m":
                time += int(t[0:-1]) * Seed.UNIT_MIN
            if t[-1] == "s":
                time += int(t[0:-1]) * 1000

        seed = Seed(seed_json['name'], seed_json['price'], time,seed_json['harvest_cnt'])
        seed_shop.add_item(seed)

    f_seed.close()

except FileNotFoundError as e:
    print(e)
    print_warning_msg("씨앗 데이터 파일이 없습니다.")

seed_shop.print_sell_list()

 

print_info_msg("게임 데이터 초기화 완료")




