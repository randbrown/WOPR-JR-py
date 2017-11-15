'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''

from wpilib.robotbase import RobotBase
from wpilib import AnalogInput
from subsystems.drive import Drive
import robotmap
from networktables import NetworkTables
from robotpy_ext.common_drivers.navx import AHRS

drive = None
sd = None
ahrs = None
rangefinder = None

def init():
    global drive
    global sd
    global ahrs
    global rangefinder
    
    ahrs = AHRS.create_spi()

    if drive is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')
    
    sd = NetworkTables.getTable('SmartDashboard')
    rangefinder = AnalogInput(0)
    drive = Drive(robotmap.motors.L0, robotmap.motors.L1, robotmap.motors.R0, robotmap.motors.R1)

def dumpInfo():
    global ahrs
    sd.putNumber('Navx_getYaw', ahrs.getYaw())
    sd.putNumber('Navx_getPitch', ahrs.getPitch())
    sd.putNumber('Ultrasonic_getAverageVoltage', rangefinder.getAverageVoltage())
