# AdditivePlatformMachineElement.objectType Property

Parent Object: [AdditivePlatformMachineElement](AdditivePlatformMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditivePlatformMachineElement.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additivePlatformMachineElement\_var" is a variable referencing an AdditivePlatformMachineElement object.  ```` ``` # Get the value of the property. propertyValue = additivePlatformMachineElement_var.objectType ``` ```` |

"additivePlatformMachineElement\_var" is a variable referencing an AdditivePlatformMachineElement object. ```` ``` #include <Cam/Machine/AdditivePlatformMachineElement.h>  // Get the value of the property. string propertyValue = additivePlatformMachineElement_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |