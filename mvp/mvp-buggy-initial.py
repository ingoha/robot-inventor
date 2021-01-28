from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

class MVP:
    _steering = Motor('A')
    # neutral position, must be calibrated
    _neutral = 0
    _drive = Motor('B')

    def calibrate(self):
        print("calibrating...")
        # should be neutral
        self._steering.run_to_position(0, 'shortest path')
        # try to run to left
        self._steering.run_to_position(90, 'shortest path')

        left = self._steering.get_position()
        print("left %d" % (left))

        self._steering.run_for_degrees(-90, 35)
        self._neutral = self._steering.get_position()
        print("neutral %d" % (self._neutral))

    # projects an angle into 0-359
    def sanitize_angle(self, degrees):
        return (degrees + 360) % 360

    def steer_left(self, degrees = 90):
        self._steering.run_to_position(self.sanitize_angle(self._neutral + degrees), 'shortest path')

    def steer_right(self, degrees = 90):
        self._steering.run_to_position(self.sanitize_angle(self._neutral - degrees), 'shortest path')

    def steer_straight(self):
        self._steering.run_to_position(self._neutral, 'shortest path')

    # positive value for rotation drives forward
    def drive(self, rotations):
        self._drive.run_for_rotations(-rotations, 80)

mvp = MVP()
mvp.calibrate()
mvp.steer_left()
mvp.drive(16)
