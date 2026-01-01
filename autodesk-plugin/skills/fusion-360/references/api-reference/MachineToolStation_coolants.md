# MachineToolStation.coolants Property![](../images/TestTubeLarge.png)

Parent Object: [MachineToolStation](MachineToolStation.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineToolStation.h>

## Description

The coolants that this tool station can use. See MachineToolStationCoolant for possible values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineToolStation\_var" is a variable referencing a MachineToolStation object. |

"machineToolStation\_var" is a variable referencing a MachineToolStation object. ```` ``` #include <Cam/Machine/MachineToolStation.h>  // Get the value of the property. std::vector<integer> propertyValue = machineToolStation_var->coolants();  // Set the value of the property, where value_var is an integer. bool returnValue = machineToolStation_var->coolants(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type integer.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |