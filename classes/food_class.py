from mud_game.classes.item_class import Item


# 음식 클래스 - 사람이 먹을 수 있는 음식
# 속성
#   - name: 음식 이름
#   - price: 가격
#   - hp: 체력 회복량 (max: 100, min: 0)
#   - satiety: 포만감 (max: 100, min: 0)
#   - thirst: 갈증 (max: 100, min: 0)
#   - clean: 청결도 (max: 100, min: 0)
class Food(Item):

    def __init__(self, name, price, satiety, thirst, clean, hp):
        self.name = name
        self.price = price
        self.satiety = satiety
        self.thirst = thirst
        self.clean = clean
        self.hp = hp

    def __str__(self):
        return "%s| 가격:%d | 포만감: %d | HP회복량: %d" % (self.name, self.price, self.satiety, self.hp)


if __name__ == "__main__":
    print("food_module")
    sweet_potato = Food("고구마", 300, 30, 20, 4, 15)
    print(sweet_potato)



    