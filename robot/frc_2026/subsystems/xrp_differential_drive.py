# ------------------------------------------------------------------------ #
#      o-o      o                o                                         #
#     /         |                |                                         #
#    O     o  o O-o  o-o o-o     |  oo o--o o-o o-o                        #
#     \    |  | |  | |-' |   \   o | | |  |  /   /                         #
#      o-o o--O o-o  o-o o    o-o  o-o-o--O o-o o-o                        #
#             |                           |                                #
#          o--o                        o--o                                #
#                        o--o      o         o                             #
#                        |   |     |         |  o                          #
#                        O-Oo  o-o O-o  o-o -o-    o-o o-o                 #
#                        |  \  | | |  | | |  |  | |     \                  #
#                        o   o o-o o-o  o-o  o  |  o-o o-o                 #
#                                                                          #
#    Jemison High School - Huntsville Alabama                              #
# ------------------------------------------------------------------------ #

import logging

from typing import Dict

from commands2 import Subsystem, RunCommand
from wpilib import Joystick, RobotBase
from wpilib.drive import DifferentialDrive
from xrp import XRPMotor
from lib_6107.constants import XrpConstants

logger = logging.getLogger(__name__)


class XrpDifferentialDriveSubsystem(Subsystem):
    """
    The drive subsystem for an XRP robot
    """
    def __init__(self):
        super().__init__()
        logger.info("__init__: entry")

        # For metrics in the future
        self._counter = 0

        # Motors
        self._left_motor: XRPMotor = XRPMotor(XrpConstants.MotorDeviceNumber.LeftDeviceNumber)
        self._right_motor: XRPMotor = XRPMotor(XrpConstants.MotorDeviceNumber.RightDeviceNumber)
        self._right_motor.setInverted(True)

        # Create the DifferentialDrive object
        self._drive: DifferentialDrive = DifferentialDrive(self._left_motor, self._right_motor)

        # # TODO: Resolve what we want to do here
        # # During simulation, we may want to interact with the encoders
        # # for each motor so we can simulate movement in the sim
        # if RobotBase.isSimulation():        #  or not RobotBase.isReal():
        #     self._left_motor.reset_encoder_position()
        #     self._right_motor.reset_encoder_position()

        # Define the default command for this subsystem
        # self._controller = Joystick(0)
        #
        # self.setDefaultCommand(
        #     RunCommand(
        #         lambda: self._drive.arcadeDrive(self._controller.getY(),
        #                                         self._controller.getX()), self)
        # )

    @property
    def motors(self) -> Dict[int, XRPMotor]:
        return {
            XrpConstants.MotorDeviceNumber.LeftDeviceNumber:  self._left_motor,
            XrpConstants.MotorDeviceNumber.RightDeviceNumber: self._right_motor
        }

    @property
    def left_motor(self) -> XRPMotor:
        return self._left_motor

    @property
    def right_motor(self) -> XRPMotor:
        return self._right_motor


    def arcadeDrive(self, speed, rotation, square_inputs=False) -> None:
        """
        Arcade drive method for differential drive platform.

        Note: Some drivers may prefer inverted rotation controls. This can be done
        by negating the value passed for rotation.

        :param speed:         The speed at which the robot should drive along the X
                              axis [-1.0..1.0]. Forward is positive.
        :param rotation:      The rotation rate of the robot around the Z axis
                               [-1.0..1.0]. Counterclockwise is positive.
        :param square_inputs: If set, decreases the input sensitivity at low speeds.
        """
        if speed or rotation:
            logger.info(f"arcadeDrive: entry, speed: {speed}, rotation: {rotation}, square_inputs: {square_inputs}")

        self._drive.arcadeDrive(speed, rotation, squareInputs=square_inputs)

    def tankDrive(self, left_speed, right_speed, square_inputs=False) -> None:
        """
        Tank drive method for differential drive platform.

        :param left_speed:    The robot left side's speed along the X axis
                              [-1.0..1.0]. Forward is positive.
        :param right_speed:   The robot right side's speed along the X axis
                              [-1.0..1.0]. Forward is positive.
        :param square_inputs: If set, decreases the input sensitivity at low speeds.
        """
        # logger.info(f"tankDrive: entry, speed: {left_speed}/{right_speed}, square_inputs: {square_inputs}")

        self._drive.tankDrive(left_speed, right_speed, squareInputs=square_inputs)

    def curvatureDrive(self, speed, rotation, allow_turn_in_place):  # real signature unknown; restored from __doc__
        """
        Curvature drive method for differential drive platform.

        The rotation argument controls the curvature of the robot's path rather
        than its rate of heading change. This makes the robot more controllable at
        high speeds.

        :param speed:               The robot's speed along the X axis [-1.0..1.0].
                                    Forward is positive.
        :param rotation:            The normalized curvature [-1.0..1.0].
                                    Counterclockwise is positive.
        :param allow_turn_in_place: If set, overrides constant-curvature turning for
                                    turn-in-place maneuvers. zRotation will control
                                    turning rate instead of curvature.
        """
        logger.info(f"curvatureDrive: entry, speed: {speed}, rotation: {rotation}, allow_turn_in_place: {allow_turn_in_place}")

        self._drive.curvatureDrive(speed, rotation, allow_turn_in_place)

    def stop(self) -> None:
        """
        Stop the motors
        """
        logger.info("stop: entry")

        self._drive.stopMotor()

    def periodic(self) -> None:
        """
        Called periodically by the scheduler
        """
        self._counter += 1