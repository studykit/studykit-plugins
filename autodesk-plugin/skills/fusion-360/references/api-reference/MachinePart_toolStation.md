# MachinePart.toolStation Property![](../images/TestTubeLarge.png)

Parent Object: [MachinePart](MachinePart.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

Get the tool station object for this part. Will return null if the part has no tool station assigned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePart\_var" is a variable referencing a MachinePart object. |

"machinePart\_var" is a variable referencing a MachinePart object. ```` ``` #include <Cam/Machine/MachinePart.h>  // Get the value of the property. Ptr<MachineToolStation> propertyValue = machinePart_var->toolStation(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineToolStation](MachineToolStation.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |