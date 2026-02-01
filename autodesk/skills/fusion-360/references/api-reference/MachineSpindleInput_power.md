# MachineSpindleInput.power Property![](../images/TestTubeLarge.png)

Parent Object: [MachineSpindleInput](MachineSpindleInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindleInput.h>

## Description

Specifies the power for this spindle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineSpindleInput\_var" is a variable referencing a MachineSpindleInput object. |

"machineSpindleInput\_var" is a variable referencing a MachineSpindleInput object. ```` ``` #include <Cam/Machine/MachineSpindleInput.h>  // Get the value of the property. double propertyValue = machineSpindleInput_var->power();  // Set the value of the property, where value_var is a double. bool returnValue = machineSpindleInput_var->power(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |