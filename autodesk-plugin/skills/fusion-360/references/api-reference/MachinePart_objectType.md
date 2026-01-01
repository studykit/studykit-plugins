# MachinePart.objectType Property

Parent Object: [MachinePart](MachinePart.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePart\_var" is a variable referencing a MachinePart object.  ```` ``` # Get the value of the property. propertyValue = machinePart_var.objectType ``` ```` |

"machinePart\_var" is a variable referencing a MachinePart object. ```` ``` #include <Cam/Machine/MachinePart.h>  // Get the value of the property. string propertyValue = machinePart_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |