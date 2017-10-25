import wpilib
from wpilib.command.subsystem import Subsystem

import robotmap

class Motor:
    def __init__(self, id):
        self.motor = wpilib.Talon(id)

    def set(self, speed):
        self.motor.set(speed)
