from wpilib.command.commandgroup import CommandGroup

from wpilib.command.waitcommand import WaitCommand
from commands.tankdrivetimed import TankDriveTimed

class AutonomousProgram(CommandGroup):
    '''
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    '''

    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(TankDriveTimed(1, .5, .5))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(SetSpeed(1, -1, .8))
