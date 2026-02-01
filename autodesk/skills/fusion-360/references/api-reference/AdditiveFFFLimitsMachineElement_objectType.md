# AdditiveFFFLimitsMachineElement.objectType Property

Parent Object: [AdditiveFFFLimitsMachineElement](AdditiveFFFLimitsMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditiveFFFLimitsMachineElement.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additiveFFFLimitsMachineElement\_var" is a variable referencing an AdditiveFFFLimitsMachineElement object.  ```` ``` # Get the value of the property. propertyValue = additiveFFFLimitsMachineElement_var.objectType ``` ```` |

"additiveFFFLimitsMachineElement\_var" is a variable referencing an AdditiveFFFLimitsMachineElement object. ```` ``` #include <Cam/Machine/AdditiveFFFLimitsMachineElement.h>  // Get the value of the property. string propertyValue = additiveFFFLimitsMachineElement_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |