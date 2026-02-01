# Machine.objectType Property

Parent Object: [Machine](Machine.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/Machine.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machine\_var" is a variable referencing a Machine object.  ```` ``` # Get the value of the property. propertyValue = machine_var.objectType ``` ```` |

"machine\_var" is a variable referencing a Machine object. ```` ``` #include <Cam/Machine/Machine.h>  // Get the value of the property. string propertyValue = machine_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |