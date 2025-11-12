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
import time

from typing import Optional

from commands2.command import Command
from wpilib import RobotBase, DriverStation, Joystick

from frc_2026.constants import IOConstants
from frc_2026.subsystems.xrp_differential_drive import XrpDifferentialDriveSubsystem

logger = logging.getLogger(__name__)

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """
    def __init__(self) -> None:
        logger.info("__init__: entry")

        self.start_time = time.time()       # Will be useful for logging / telemetry message in the future

        if RobotBase.isSimulation():
            # The Joystick outputs warnings while running under the simulator
            DriverStation.silenceJoystickConnectionWarning(True)

        # Command(s) to run when in Autonomous Mode
        self._autonomous_command: Optional[Command] = None

        # Initialize the robot's subsystems
        self._drive = XrpDifferentialDriveSubsystem()

        # Initialize and then configure the controllers
        self._driver_controller, self._operator_controller = self._configure_controller()
        # Initialize and then configure the controller
        self._driver_controller: Joystick = self._configure_controller()    # If single joystick

        # TODO: Register the commands

        # TODO: Initialize the dashboard

        # TODO: Preload/parse the pathfinder command

        # TODO: Perform any other variable/object initialization

    @property
    def controller(self) -> Joystick:
        return self._driver_controller

    @property
    def drive(self) -> XrpDifferentialDriveSubsystem:
        return self._drive

    def set_start_time(self):  # call in teleopInit and autonomousInit in the robot
        self.start_time = time.time()

    def get_enabled_time(self):  # call when we want to know the start/elapsed time for status and debug messages
        return time.time() - self.start_time

    @property
    def elapsed_time(self) -> float:
        """
        Return the number of seconds that have elapsed since the start time was set.

        :return: elapsed time in seconds
        """
        return self.get_enabled_time() - self.start_time

    def get_autonomous_command(self) -> Optional[Command]:
        """
        Get the Autonomous command to run.

        Once we start working with PathPlanner, there is an AutoBuilder component that
        creates fully autonomous routines from paths and auto files created in the
        PathPlanner GUI.

        :return: Autonomous command to run.
        """
        return self._autonomous_command

    def _configure_controller(self) -> Joystick:
        """
        Use this command to configure your robot controller(s)

        :return: Tuple containing the driver and operator controllers
        """
        driver_controller = Joystick(IOConstants.DRIVER_CONTROLLER_PORT)

        # For simulation using the keyboard
        #
        #  w  : Forward:  Increases as it is held, decreases after it releases. Starts
        #                 at 0.0 and increases toward -1.0
        #  s  : Backward: Increases as it is held, decreases after it releases. Starts
        #                 at 0.0 and increases toward 1.0
        #  a  : Rotation: Increases as it is held, decreases after it releases. Starts
        #                 at 0.0 and increases toward -1.0
        #  d  : Rotation: Increases as it is held, decreases after it releases. Starts
        #                at 0.0 and increases toward 1.0
        #
        ###############
        # Buttons are the 'z', 'x', 'c', and 'v'.  TODO: Currently do not know the names, assume z is Button 1

        # TODO: Configure the button bindings on the keyboard for other operations
        #       or command we need.

        return driver_controller

    def _secondary_controller(self) -> Joystick:
        """
        Use this command to configure your robot controller(s)

        :return: Tuple containing the driver and operator controllers
        """
        driver_controller = Joystick(IOConstants.OPERATOR_CONTROLLER_PORT)

        # For simulation using the keyboard
        #
        #  i  : Forward:  Increases as it is held, decreases after it releases. Starts
        #                 at 0.0 and increases toward -1.0
        #  k  : Backward: Increases as it is held, decreases after it releases. Starts
        #                 at 0.0 and increases toward 1.0
        #  j  : Rotation: Increases as it is held, decreases after it releases. Starts
        #                 at 0.0 and increases toward -1.0
        #  l  : Rotation: Increases as it is held, decreases after it releases. Starts
        #                at 0.0 and increases toward 1.0
        #
        ###############
        # Buttons are the 'z', 'x', 'c', and 'v'.  TODO: Currently do not know the names, assume z is Button 1

        # TODO: Configure the button bindings on the keyboard for other operations
        #       or command we need.

        return driver_controller