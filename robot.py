from wpilib import run, TimedRobot, Joystick
import math
from wpimath.controller import PIDController
from drivetrain import Drivetrain


class Robot(TimedRobot):
    
    joy1 = Joystick(0)
    
    def __init__(self):
        super().__init__()
        self.drivetrain = Drivetrain()
        self.turn_controller = PIDController(0.001, 0, 0)
        self.drive_controller = PIDController(0.001, 0, 0)
        self.stage = 0

    def robotInit(self):
        pass

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        speed=-self.joy1.getRawAxis(1)*.4
        turn=self.joy1.getRawAxis(4)*.2
        #print(f"Speed: {speed} Turn: {turn}")
        self.drivetrain.set(speed+turn, speed-turn)

    def autonomousInit(self):
        self.turn_controller.setPosition(0)
        self.drive_controller.setPosition(0)
        self.turn_controller.setTolerance(1, 1)
        self.drive_controller.setTolerance(1, 1)
        self.drivetrain.setYaw(0)

    def autonomousPeriodic(self):
        self.drive_controller.setSetpoint(10)
        if self.drive_controller.atSetpoint():
            self.stage += 1


if __name__ == "__main__":
    run(Robot)
