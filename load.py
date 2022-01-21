from classes.food_class import Food
from classes.shop_class import *
from classes.farm_class import *
from mud_game.modules.print_module import *
 
print_info_msg("게임 데이터 초기화중")
    
# Init Foods
carrot = Food("당근", 100, 5, 10, 0, 3)
sweet_potato = Food("고구마", 300, 30, 20, 4, 15)

# Init Places
veget_shop = VegetShop("야채 가게")
veget_shop.add_item(carrot)
veget_shop.add_item(sweet_potato)

print_info_msg("게임 데이터 초기화 완료")




