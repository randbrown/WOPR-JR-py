"""

motor controllers

"""

from wpilib.command.subsystem import Subsystem
from hardware.motor import Motor

from commands.tankdrivetimed import TankDriveTimed


class Drive(Subsystem):

    def __init__(self, L0, L1, R0, R1):

        super().__init__('Drive')

        self.L0 = Motor(L0)
        self.L1 = Motor(L1)
        self.R0 = Motor(R0)
        self.R1 = Motor(R1)


    def set(self, Lpow, Rpow):
        self.L0.set(Lpow)
        self.L1.set(Lpow)

        self.R0.set(Rpow)
        self.R1.set(Rpow)
    

