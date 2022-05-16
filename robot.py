import wpilib
from wpilib import run, TimedRobot, Joystick
import math
from wpimath.controller import PIDController
from drivetrain import Drivetrain


class Robot(wpilib.TimedRobot):
    
    joy1=Joystick(0)
    
    def __init__(self):
        super().__init__()
        self.drivetrain = Drivetrain()

    def robotInit(self):
        self.drive_controller = PIDController(.003,0,0)

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
        self.drivetrain.m_left_encoder.setPosition(0)
        distance = 7
        wheel_radius = 2
        self.revolutions = (distance * 12 * 360) / (wheel_radius * 2 * math.pi)


    def autonomousPeriodic(self):
        self.drive_controller.setSetpoint(self.revolutions)

        motion = self.drive_controller.calculate(measurement = self.drivetrain.m_left_encoder)
        motion = min(0.4, max(-0.4, motion))
        self.drivetrain.set(motion, motion)



if __name__ == "__main__":
    wpilib.run(Robot)
