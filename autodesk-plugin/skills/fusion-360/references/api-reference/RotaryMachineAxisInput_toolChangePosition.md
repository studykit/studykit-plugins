# RotaryMachineAxisInput.toolChangePosition Property![](../images/TestTubeLarge.png)

Parent Object: [RotaryMachineAxisInput](RotaryMachineAxisInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxisInput.h>

## Description

Specifies the value that this axis returns to, prior to a tool change. Units are cm for linear axes or radians for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. |

"rotaryMachineAxisInput\_var" is a variable referencing a RotaryMachineAxisInput object. ```` ``` #include <Cam/Machine/RotaryMachineAxisInput.h>  // Get the value of the property. double propertyValue = rotaryMachineAxisInput_var->toolChangePosition();  // Set the value of the property, where value_var is a double. bool returnValue = rotaryMachineAxisInput_var->toolChangePosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |