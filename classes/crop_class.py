from mud_game.classes.item_class import Item


# 작물 클래스 - 사람이 재배한 농작물
# 속성
#   - name: 농작물 이름
#   - price: 가격
#   - hp: 체력 회복량 (max: 100, min: 0)
#   - satiety: 포만감 (max: 100, min: 0)
#   - thirst: 갈증 (max: 100, min: 0)
#   - clean: 청결도 (max: 100, min: 0)
class Crop(Item):

    def __init__(self, name, price, satiety, thirst, clean, hp):
        self.name = name
        self.price = price
        self.satiety = satiety
        self.thirst = thirst
        self.clean = clean
        self.hp = hp

    def set_icon(self, icon):
        self.icon = icon

    def __str__(self):
        return "%s=> 가격:%d | 포만감: %d | HP회복량: %d" % (self.name, self.price, self.satiety, self.hp)


if __name__ == "__main__":
    pass


    