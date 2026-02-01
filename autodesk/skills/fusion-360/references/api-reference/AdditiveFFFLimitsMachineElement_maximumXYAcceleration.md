# AdditiveFFFLimitsMachineElement.maximumXYAcceleration Property

Parent Object: [AdditiveFFFLimitsMachineElement](AdditiveFFFLimitsMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditiveFFFLimitsMachineElement.h>

## Description

Maximum supported acceleration for motion in the X or Y axes in cm/s^2.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveFFFLimitsMachineElement\_var" is a variable referencing an AdditiveFFFLimitsMachineElement object. |

"additiveFFFLimitsMachineElement\_var" is a variable referencing an AdditiveFFFLimitsMachineElement object. ```` ``` #include <Cam/Machine/AdditiveFFFLimitsMachineElement.h>  // Get the value of the property. double propertyValue = additiveFFFLimitsMachineElement_var->maximumXYAcceleration();  // Set the value of the property, where value_var is a double. bool returnValue = additiveFFFLimitsMachineElement_var->maximumXYAcceleration(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |