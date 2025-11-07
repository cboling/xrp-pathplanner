# Investigation into PathPlanner with the XRP Robot

I am new to the First Robotics Challenge and I am working as a programing mentor for Team
6107 (CyberJagzz) in Huntsville, Alabama. They had previously used Java in previous competitions,
but I am hoping to get our freshmen class proficient in Python via robotics so a continuous
stream of new teammates can learn robotics and python in the years to come.

While you can clone the repository and learn from it, I hope you also can use various
steps that I went through to learn as well. 

At the end, I have some reference links that may be of help.

# Goal
 
- [ ] Set up a robotpy project from scratch
- [ ] Get a very simple framework set up and running under simulation and on the XRP
- [ ] Begin improvements to connect up a controller/joystick
- [ ] Get the robot to actually move
- [ ] Setting up a Makefile to allow you shell environment to be simple to use
- [ ] Learn the PathPlanner tool and apply it to a simple robot (XRP)
- [ ] Document each step here (and in a documents subdirectory) so others can learn and expand on this work
- [ ] Implement both autonomous and teleop modes
- [ ] Split off common code that can be used from year to year
- [ ] Learn about telemetry and all the other things I do not know yet that will help on the real competition robot.

# This base directory
The code in this base directory, plus the [frc-2026](2026) and [lib-6107](lib-6107) should run as final
completed code. Of course if you are using this as I write it (Fall of 2025), then consider it a work
in progress and check in as I get each step [Goal](#Goal) completed.

**TODO**: _If you see this line in the README, I am still writing this document_

# Step-0: Starting point

- [X] Set up a robotpy project from scratch
Skeleton files exist in the [step-00](/steps/step-00) subdirectory

Installed robotpy and performed init (I am using python 3.13.9 since I am learning for the 2026 competition)

```shell
mkdir -p xrp-pathplanner/robot && cd xrp-pathplanner/robot
python3 -m pip install pyrobot
python3 -m robotpy init
```
Then modify your pyproject.toml **robotpy_extras** to enable the _commands2_, _pathplannerlib_, and _xrp_ modules.
You can then sync your environment with the **robotpy** _sync_ command.
```shell
python3 -m robotpy sync
```
## Using a virtual environment
A virtual environment can be used if you wish to keep in separate from your other projects. This also
will help in keeping a consistent environment for your development.

### Creating the virtual python environment
Run the supplied **env.sh** script if you are on a linux or macOS system. You can manually perform the commands
if you are on Windows. An alternative if you have windows is to load the Windows Subsystem for Linux (WSL) and
use a bash shell in that environment instead. You can edit with you favorite Windows based IDE and execute command
lines in the bash shell.

Both the env.sh and reqirements-2026.txt were hand created. I often like to create a _Makefile_ and use **make**
command to do a bunch of my work from the command line. The _Makefile_ will be set up in []

```shell
source ./env.sh
```
This will create the same environment as the **python3 -m robotpy sync** command.  Should you log out
and need to re-enter the virtual environment, execute the same **env.sh** command above. It will activate
the virtual environment
 
# Step-1: Improve your initial files and directory structure

- [X] Get a very simple framework set up and running under simulation and on the XRP

This step creates our initial files and subdirectories. This the framework for everything will be done in the
first several steps. Completed files/directories exist in the [Step-1](/steps/step-01) subdirectory. Diff them with [Step-0](/steps/step-00)
to see what changed. 

First move all the files that we are going to 'copy over' from the Step-1 directory to a backup
location and then copy in the [Step-1](/steps/step-01) files. We will then describe what each file does and
I wrote it that way.

```shell
# This assumes you are in the .../xrp-pathplanner/robot subdirectory. This will
# copy all the source for step-1 into the base robot subdirectory and insure the
# virtual environment is set up

mkdir -p .backup/before-step-1 && mv pyproject.toml robot.py .backup/before-step-1/ && \
cp -rp ../steps/step-01 . && source ./env.sh
```
If all completed successfully, you should have all the files needed for step-1 completed and
your virtual environment initialized. All files are just skeletons of what we will be working
on later, so jost doing a blind copy is much easier. In later steps, we will be doing file-by-file
changes instead.

## robot.py

## frc-2026 Subdirectory
This subdirectory contains all the code (written in 2026) for this project. While this XRP
example is being written for myself and Team 6107 to learn from, it will mimick what we
will do for the FRC 2026 challenge.

Basically, we will be coding and experimenting here. As the code matures, we may begin to
break of re-usable portions and place them in the [lib-6107](../lib-6107/) subdirectories.

### constants.py

## robotcontainer.py

### autonomous Subdirectory

### commands Subdirectory

### subsystems Subdirectory


## lib-6107 Subdirectory

This subdirectory will eventually contain re-usable functions, base classes, and other resources
that will be re-usable from year-to-year. For now, it is empty, but in one of our last steps, the
existing [frc-2026](../frc-2026) code will be refactored and the initial library will be created. The
first consumer of that new library, besides this example, will be Team 6107's 2026 robot. It will not
be based on an XRP, but the actual deal. That project will also follow this same design pattern and
hopefully will be helpful to other FRC Teams in the 2026 competition as well as the future.

# Step-2: Hook up a controller
- [X] Begin improvements to connect up a controller/joystick


# Step-3: Lets get the robot to move
- [X] Get the robot to actually move


# Step-4: Makefiles and the CLI
- [X] Setting up a Makefile to allow you shell environment to be simple to use


# Step-5:
- [X] Learn the PathPlanner tool and apply it to a simple robot (XRP)



# References

 - [pyrobot](https://pyrobot.org/docs/overview.html)
 - [PathPlanner Docs](https://pathplanner.dev/home.html) - motion profile generator
 - [PathPlanner Python API](https://pathplanner.dev/api/python/)
 - [PathPlanner getting started](https://pathplanner.dev/pplib-getting-started.html)
 - [Command](https://robotpy.readthedocs.io/projects/commands-v2/en/stable/commands2/Command.html) - robotpy 'Command' class
