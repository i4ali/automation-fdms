# automation-fdms
Test automation project for FDMS software

Project root contains sub-project automation-UI and potentially automation-backend in the near future

## automation-UI
UI automation is done using Python binding for selenium v3

### Pre-requisite
Python v3.6

### Execution Steps
#### Linux
1) use python virtual environment(optional) - this is the preferred way but not required
2) clone the repo to a directory
3) copy the drivers in /automation-fdms/automation-UI/drivers to /usr/bin or /usr/local/bin
3) install dependencies and packages through "pip install -r requirements.txt"
4) cd into directory /automation-fdms/automation-UI
5) run "export PYTHONPATH=."
6) run "python3 -m unittest" 

#### Windows TBD

NOTE - Plan is to move the setup to a docker image to simplify the execution steps
