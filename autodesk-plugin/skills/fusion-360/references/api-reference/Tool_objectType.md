# Tool.objectType Property

Parent Object: [Tool](Tool.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/Tool.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tool\_var" is a variable referencing a Tool object.  ```` ``` # Get the value of the property. propertyValue = tool_var.objectType ``` ```` |

"tool\_var" is a variable referencing a Tool object. ```` ``` #include <Cam/Tools/Tool.h>  // Get the value of the property. string propertyValue = tool_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |