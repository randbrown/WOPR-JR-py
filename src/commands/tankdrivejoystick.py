from wpilib.command import Command

import subsystems
import oi
import robotmap

class TankDriveJoystick(Command):
    '''
    Spins the motor at the given power for a given number of seconds, then
    stops.
    '''

    def __init__(self):
        super().__init__('Tank Drive Joystick')

        self.requires(subsystems.drive)

    def execute(self):
        
        subsystems.drive.set(oi.joystick.getRawAxis(robotmap.axes.L_y), oi.joystick.getRawAxis(robotmap.axes.R_y))

    def end(self):
        subsystems.drive.set(0, 0)