from mud_game.classes.farm_class import Farm
import threading
import time


class CropManager(threading.Thread):
    def __init__(self, name, farm: Farm):
        super().__init__()
        self.name = name
        self.farm = farm

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        while True:
            for crop in self.farm.crops:
                #print("[%s] Checking Crop %s" % (self.name, crop))
                if crop.time - 1000 <= 0:
                    print("[%s] %s가 다 자랐습니다!" % (self.name, crop.name))
                else:
                    crop.time -= 1000
            time.sleep(1)

        