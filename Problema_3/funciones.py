import math

class circulo:
    def __init__(self, radio):
        self.radio = radio

    def calculo_area(self):
        return 3.14159 * pow(self.radio, 2)