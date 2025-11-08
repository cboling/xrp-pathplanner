#!/usr/bin/env python3
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

from typing import Optional

from commands2 import TimedCommandRobot, CommandScheduler
from wpilib import RobotBase

from version import VERSION
from frc_2026.robotcontainer import RobotContainer

logger = logging.getLogger(__name__)

class MyRobot(TimedCommandRobot):
    """
    Our default robot class

    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you
    """
    def __init__(self):
        super().__init__()

        # Define / initialize all of our class variables
        self._container: Optional[RobotContainer] = None

    def robotInit(self) -> None:
        """
        Robot-wide initialization code should go here.

        Users should override this method for default Robot-wide initialization
        which will be called when the robot is first powered on. It will be called
        exactly one time.
        """
        if RobotBase.isSimulation():
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.ERROR)

        version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        logger.info(f"Python: {version}, Software Version: {VERSION}")

        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self._container = RobotContainer()

    def robotPeriodic(self) -> None:
        """
        Periodic code for all modes should go here.

        This function is called each time a new packet is received from the driver
        station.
        """
        pass

    def disabledInit(self) -> None:
        """
        Initialization code for disabled mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters disabled mode.
        """
        pass

    def disabledPeriodic(self) -> None:
        """
        Periodic code for disabled mode should go here.

        Users should override this method for code which will be called each time a
        new packet is received from the driver station and the robot is in disabled
        mode.
        """
        pass

    def disabledExit(self) -> None:
        """
        Exit code for disabled mode should go here.

        Users should override this method for code which will be called each time
        the robot exits disabled mode.
        """
        pass

    def autonomousInit(self) -> None:
        """
        Initialization code for autonomous mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters autonomous mode.
        """
        command = self._container.get_autonomous_command()
        if command:
            command.schedule()

    def autonomousPeriodic(self) -> None:
        """
        Periodic code for autonomous mode should go here.

        Users should override this method for code which will be called each time a
        new packet is received from the driver station and the robot is in
        autonomous mode.
        """
        pass

    def autonomousExit(self) -> None:
        """
        Exit code for autonomous mode should go here.

        Users should override this method for code which will be called each time
        the robot exits autonomous mode.
        """
        command = self._container.get_autonomous_command()
        if command:
            command.cancel()

    def teleopInit(self) -> None:
        """
        Initialization code for teleop mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters teleop mode.
        """
        command = self._container.get_autonomous_command()
        if command:
            command.cancel()

    def teleopPeriodic(self) -> None:
        """
        Periodic code for teleop mode should go here.

        Users should override this method for code which will be called each time a
        new packet is received from the driver station and the robot is in teleop
        mode.
        """
        pass

    def teleopExit(self) -> None:
        """
        Exit code for teleop mode should go here.

        Users should override this method for code which will be called each time
        the robot exits teleop mode.
        """
        pass

    def testInit(self) -> None:
        """
        Initialization code for test mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters test mode.
        """
        CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self):
        """
        Periodic code for test mode should go here.

        Users should override this method for code which will be called each time a
        new packet is received from the driver station and the robot is in test
        mode.
        """
        pass

    def testExit(self) -> None:
        """
        Exit code for test mode should go here.

        Users should override this method for code which will be called each time
        the robot exits test mode.
        """
        pass

    def _simulationInit(self) -> None:
        """
        Robot-wide simulation initialization code should go here.

        Users should override this method for default Robot-wide simulation
        related initialization which will be called when the robot is first
        started. It will be called exactly one time after RobotInit is called
        only when the robot is in simulation.
        """
        pass

    def _simulationPeriodic(self):
        """
        Periodic simulation code should go here.

        This function is called in a simulated robot after user code executes.
        """
        pass

""""
Main CLI entry point. Run the MyRobot class via the wpilib 'run' command

  ``wpilib.run`` is no longer used. You should run your robot code via one of
the following methods instead:

* Windows: ``py -m robotpy [arguments]``
* Linux/macOS: ``python -m robotpy [arguments]``

In a virtualenv the ``robotpy`` command can be used directly.

If you are running under the PyCharm IDE: You
"""
