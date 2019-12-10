import board
import busio

import adafruit_htu21d

# Interface
class Sensor:
    def data(self) -> dict:
        pass

class HTU21D(Sensor):
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_htu21d.HTU21D(i2c)

    def data(self):
        temp_c = round(self.sensor.temperature, 2)
        humid = round(self.sensor.relative_humidity)

        temp_f = temp_c * 9.0 / 5.0 + 32.0

        res = {
            "temp_c": temp_c,
            "temp_f": temp_f,
            "humidity": humid
            }
        return res

class PM(Sensor):
    def __init__(self):
        pass

    def data(self):
        pass

