from wpilib.command import TimedCommand

import subsystems
import oi

class TankDriveJoystick(TimedCommand):
    '''
    Spins the motor at the given power for a given number of seconds, then
    stops.
    '''

    def __init__(self):
        super().__init__('Tank Drive Joystick')

        self.requires(subsystems.drive)

    def initialize(self):
        subsystems.drive.set(self.Lpow, self.Rpow)

    def end(self):
        subsystems.drive.set(0, 0)