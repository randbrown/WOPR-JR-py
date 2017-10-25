'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''

from wpilib.robotbase import RobotBase
from subsystems.tankdrive import TankDrive
import robotmap

drive = None

def init():
    global drive

    if drive is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    drive = TankDrive(robotmap.motors.L0, robotmap.motors.L1, robotmap.motors.R0, robotmap.motors.R1)

