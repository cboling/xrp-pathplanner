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
#
# Constants for source in this subdirectory will go here
import math

from enum import IntEnum

from pyfrc.physics.units import units
from wpimath.units import kilograms


class XrpConstants:
    """
    Constants for the XRP Robot
    """
    class Physical:
        GearReduction = 48.75
        WheelDiameter = 0.060
        TrackWidth = 0.155
        RobotWidth = 0.19
        RobotLength = 0.19
        MassWithBatteries = 0.26   # With batteries

    class Motor:
        # The XRP uses a generic 4.5V motor, we can approximate its characteristics. The stall
        # current for a single motor on the XRP robot is approximately 1.2 Amps at 5V. When
        # operating on a 6V supply (such as 4-cell NiMH batteries when fully charged), the
        # stall current is around 1.4 Amps per motor.
        # The free current is minimal and the value below (0.02) is what the microprocessor
        # is drawing.
        Voltage = 4.5
        NoLoadOutputSpeed = 90   # RPM
        StallTorque = 1.0      # Stall torque in N*m (approximation) - Torque when stalled.
        StallCurrent = 1.2                    # Stall current - Current draw when stalled.
        FreeCurrent = 0.02 / 2             # Free Current - Current draw under no load.
        FreeSpeed = 90 * (2 * math.pi) / 60   # ~ 9.42 radians_per_second
        MotorCount = 1                                         # Number of motors in a gearbox

        MaxSpeed = 0.6  # Meters per second

        # NoLoadOutputSpeed = revolutions_per_minute(90)  # RPM
        # StallTorque = newton_meters(1.0),  # Stall torque in N*m (approximation) - Torque when stalled.
        # StallCurrent = amperes(1.2),  # Stall current - Current draw when stalled.
        # FreeCurrent = amperes(0.02 / 2),  # Free Current - Current draw under no load.
        # FreeSpeed = radians_per_second(NoLoadOutputSpeed * (2 * math.pi) / 60)  # ~ 9.42 radians_per_second
        # MotorCount = 1  # Number of motors in a gearbox.

    class MotorDeviceNumber(IntEnum):
        LeftDeviceNumber = 0
        RightDeviceNumber = 1

    class EncoderChannel(IntEnum):
        LeftChannel_A  = 4  # Left Encoder Quadrature Channel A
        LeftChannel_B  = 5
        RightChannel_A  = 6
        RightChannel_B = 7

        Motor3Channel_A = 8
        Motor3Channel_B = 9
        Motor4Channel_A = 10
        Motor4Channel_B = 11

        CountsPerRevolution = 585   # counts per wheel revolution

