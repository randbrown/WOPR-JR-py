#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot

import subsystems
import oi
from commands.autonomous import AutonomousProgram
from commands.tankdrivejoystick import TankDriveJoystick


class WOPRJR(CommandBasedRobot):
    def robotInit(self):
        subsystems.init()
        self.autonomousProgram = AutonomousProgram()
        self.teleopProgram = TankDriveJoystick()

        oi.init()


    def autonomousInit(self):
        self.autonomousProgram.start()

    def teleopInit(self):
        self.teleopProgram.start()

    def teleopPeriodic(self):
        subsystems.dumpInfo()


if __name__ == '__main__':
    wpilib.run(WOPRJR)
