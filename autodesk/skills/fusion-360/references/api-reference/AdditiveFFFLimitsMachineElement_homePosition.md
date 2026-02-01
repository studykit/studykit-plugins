# AdditiveFFFLimitsMachineElement.homePosition Property

Parent Object: [AdditiveFFFLimitsMachineElement](AdditiveFFFLimitsMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditiveFFFLimitsMachineElement.h>

## Description

Position of the machine home location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveFFFLimitsMachineElement\_var" is a variable referencing an AdditiveFFFLimitsMachineElement object. |

"additiveFFFLimitsMachineElement\_var" is a variable referencing an AdditiveFFFLimitsMachineElement object. ```` ``` #include <Cam/Machine/AdditiveFFFLimitsMachineElement.h>  // Get the value of the property. Ptr<Point3D> propertyValue = additiveFFFLimitsMachineElement_var->homePosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = additiveFFFLimitsMachineElement_var->homePosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |