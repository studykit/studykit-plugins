# AdditivePlatformMachineElement.clearance Property

Parent Object: [AdditivePlatformMachineElement](AdditivePlatformMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditivePlatformMachineElement.h>

## Description

Clearance height used for automatically arranging parts and suggested height for positioning part on the build platform. Units are cm.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additivePlatformMachineElement\_var" is a variable referencing an AdditivePlatformMachineElement object. |

"additivePlatformMachineElement\_var" is a variable referencing an AdditivePlatformMachineElement object. ```` ``` #include <Cam/Machine/AdditivePlatformMachineElement.h>  // Get the value of the property. double propertyValue = additivePlatformMachineElement_var->clearance();  // Set the value of the property, where value_var is a double. bool returnValue = additivePlatformMachineElement_var->clearance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |