# demo-br-asyncua
simple example how to get access to B&amp;R PLC with [asyncua: Python asyncio based OPC-UA stack](https://github.com/FreeOpcUa/opcua-asyncio)

## Installation

### Python
tested with Python 3.9.5 under Win10/64Bit

### asyncua library
`pip install asyncua`

### VNC-Viewer
Many VNC viewers work but B&R VNC Viewer is already reasonably preconfigured:
[B&R VNC Viewer](https://www.br-automation.com/en/downloads/software/hmi-software/vnc-viewer/vnc-viewer-winxp-win7-win81-win10/?noredirect=1)


## Prepare Automation Studio project

### B&R 'coffeemachine'
I used Automation Studio 4.1 which can be used without a licence since 4.1.14 and its demo project 'Coffeemachine' for testing.
OPC-UA server is already configured in this version.

![coffeemachine1](/doc/coffeemachine1.png)

### insert an OPC-UA Default Configuration and enable Tags

![coffeemachine2](/doc/coffeemachine2.png)

### create a simulated PLC (ArSim)

![coffeemachine3](/doc/coffeemachine3.png)

## Test

- connect VNC viewer (IP:127.0.0.1, password 'c')
- open console and start script

![coffeemachine4](/doc/coffeemachine4.png)





