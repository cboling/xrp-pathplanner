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
# Linux/macOS script to save current directory contents before we change
# code.
#
# Validate the backup parameter was provided
#
if [ $# -ne 1 ]; then
  echo
  echo "Usage: backup.sh <backup-sub-directory-name"
  echo
  echo "  such as:      backup.sh before-step-2"
  echo
  exit 1
fi
BACKUP_BASE_DIRECTORY=${BACKUP_BASE_DIRECTORY:-"{./backup"}
BACKUP_DIRECTORY="${BACKUP_BASE_DIRECTORY}/$1"

echo "Creating backup directory '${BACKUP_DIRECTORY}' and saving files..."

#mkdir -p .backup/before-step-1 && echo "Created our backup directory" && \
#mv *.toml *.py requirements*.txt .backup/before-step-1/ && echo "Moved our existing files to the backup" && \
#cp -rp ../steps/step-01 .  && echo "Copied this step files to our current directory '.'" && \
#source ./env.sh            && echo "Create and/or enter our virtual environment"
#