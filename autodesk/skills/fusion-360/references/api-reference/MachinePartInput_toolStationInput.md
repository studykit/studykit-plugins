# MachinePartInput.toolStationInput Property![](../images/TestTubeLarge.png)

Parent Object: [MachinePartInput](MachinePartInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePartInput.h>

## Description

Gets or sets an tool station input object to create a new MachineToolStation with this part. Only valid when partType is not Axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePartInput\_var" is a variable referencing a MachinePartInput object. |

"machinePartInput\_var" is a variable referencing a MachinePartInput object. ```` ``` #include <Cam/Machine/MachinePartInput.h>  // Get the value of the property. Ptr<MachineToolStationInput> propertyValue = machinePartInput_var->toolStationInput();  // Set the value of the property, where value_var is a MachineToolStationInput. bool returnValue = machinePartInput_var->toolStationInput(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachineToolStationInput](MachineToolStationInput.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |