# MultiAxisMachineElement.retractAndReconfigureSettings Property![](../images/TestTubeLarge.png)

Parent Object: [MultiAxisMachineElement](MultiAxisMachineElement.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisMachineElement.h>

## Description

The multi-axis retract and reconfigure settings for this machine. For changes to to this object to take effect, re-assign them to this property. To not use multi-axis retract and reconfigure, set this to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiAxisMachineElement\_var" is a variable referencing a MultiAxisMachineElement object. |

"multiAxisMachineElement\_var" is a variable referencing a MultiAxisMachineElement object. ```` ``` #include <Cam/Machine/MultiAxisMachineElement.h>  // Get the value of the property. Ptr<MultiAxisRetractAndReconfigureSettings> propertyValue = multiAxisMachineElement_var->retractAndReconfigureSettings();  // Set the value of the property, where value_var is a MultiAxisRetractAndReconfigureSettings. bool returnValue = multiAxisMachineElement_var->retractAndReconfigureSettings(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MultiAxisRetractAndReconfigureSettings](MultiAxisRetractAndReconfigureSettings.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |