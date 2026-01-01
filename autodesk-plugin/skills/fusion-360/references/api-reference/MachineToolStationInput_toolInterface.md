# MachineToolStationInput.toolInterface Property![](../images/TestTubeLarge.png)

Parent Object: [MachineToolStationInput](MachineToolStationInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineToolStationInput.h>

## Description

The type of interface that this tool station uses. (e.g. BT40, CAPTO C5, HSK A100, SK50, etc.) Note: All newline characters will be removed, and if the string contains only ASCII characters, it will be converted to uppercase.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineToolStationInput\_var" is a variable referencing a MachineToolStationInput object. |

"machineToolStationInput\_var" is a variable referencing a MachineToolStationInput object. ```` ``` #include <Cam/Machine/MachineToolStationInput.h>  // Get the value of the property. string propertyValue = machineToolStationInput_var->toolInterface();  // Set the value of the property, where value_var is a string. bool returnValue = machineToolStationInput_var->toolInterface(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |