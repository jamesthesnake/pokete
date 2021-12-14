import time
import scrap_engine as se
from .color import Color


class HealthBar(se.Text):
    """Healthbar class"""
    def __init__(self, poke):
        self.poke = poke
        super().__init__(8 * "#", esccode=Color.green, state="float")

    def make(self, oldhp):
        """Creates the healthbar"""
        bar_num = round(oldhp * 8 / self.poke.full_hp)
        esccode = Color.red
        for size, color in zip([6, 2], [Color.green, Color.yellow]):
            if bar_num > size:
                esccode = color
                break
        self.rechar(bar_num * "#", esccode)

    def update(self, oldhp):
        """Updates the healthbar in steps"""
        while oldhp != self.poke.hp and oldhp > 0:
            oldhp += -1 if oldhp > self.poke.hp else 1
            self.poke.text_hp.rechar(f"HP:{oldhp}", esccode=Color.yellow)
            self.make(oldhp)
            time.sleep(0.1)
            self.poke.ico.map.show()
        self.poke.text_hp.rechar(f"HP:{oldhp}")
        time.sleep(0.1)


if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
