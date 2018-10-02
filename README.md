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
4) install dependencies and packages through "pip install -r requirements.txt"
5) cd into directory /automation-fdms/automation-UI
6) run "export PYTHONPATH=."
7) run "py.test <testfile> -v -s" 

#### Windows TBD

TODO 

