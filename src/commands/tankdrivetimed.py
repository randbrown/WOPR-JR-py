from wpilib.command import TimedCommand

import subsystems

class TankDriveTimed(TimedCommand):
    '''
    Spins the motor at the given power for a given number of seconds, then
    stops.
    '''

    def __init__(self, timeout, Lpow, Rpow):
        super().__init__('Tank Drive Timed %d' % (Lpow, Rpow), timeout)

        self.Lpow = Lpow
        self.Rpow = Rpow
        self.requires(subsystems.drive)

    def initialize(self):
        subsystems.drive.set(self.Lpow, self.Rpow)

    def end(self):
        subsystems.drive.set(0, 0)
        