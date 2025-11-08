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
import sys
import time

from typing import Optional

from commands2.command import Command
from wpilib import RobotBase, DriverStation

logger = logging.getLogger(__name__)

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """
    def __init__(self) -> None:
        self.start_time = time.time()       # Will be useful for logging / telemetry message in the future

        if RobotBase.isSimulation():
            # The Joystick outputs warnings while running under the simulator
            DriverStation.silenceJoystickConnectionWarning(True)

        # Command(s) to run when in Autonomous Mode
        self._autonomous_command: Optional[Command] = None

        # TODO: Initialize the robot's subsystems

        # TODO: Configure the controller(s)

        # TODO: Register the commands

        # TODO: Initialize the dashboard

        # TODO: Preload/parse the pathfinder command

        # TODO: Perform any other variable/object initialization

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
