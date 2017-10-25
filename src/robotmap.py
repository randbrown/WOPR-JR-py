
class PortsList:
    '''Dummy class used to store variables on an object.'''
    pass


motors = PortsList()
solenoids = PortsList()
buttons = PortsList()
axes = PortsList

motors.R0, motors.R1 = 0, 1
motors.L0, motors.L1 = 2, 3

motors.climb = 4
motors.intake = 5
motors.stir = 6
motors.shoot = 7

# open gate, close gate
solenoids.gate = 0, 1

# open intake, close intake
solenoids.gearintake = 2, 3

# high gear, low gear
solenoids.gearbox = 4, 5

buttons.square = 1
buttons.x = 2
buttons.circle = 3
buttons.triangle = 4

axes.L_x = 0
axes.L_y = 1
axes.R_x = 2
axes.R_y = 5

axes.L_trigger = 3
axes.R_trigger = 4

