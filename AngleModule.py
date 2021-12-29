import board
import adafruit_bno055

class Orientation():
    
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)

    def calibrationStatus(self):
        try:
            while not self.sensor.calibrated:
                print(self.sensor.calibration_status)
            print("Calibration complete!")
            print(self.sensor.offsets_accelerometer)
        except:
            print("Calibration failed")

    def angle(self):
        angle = self.sensor.euler[0]
        if angle is not None:
            if angle > 180:
                angle = angle - 360
        print(angle)
        return angle

if __name__ == '__main__':
    #calibrationStatus()
    IMU = Orientation()
    while True:
        IMU.angle()

