# ToolQuery.objectType Property

Parent Object: [ToolQuery](ToolQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQuery.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolQuery\_var" is a variable referencing a ToolQuery object.  ```` ``` # Get the value of the property. propertyValue = toolQuery_var.objectType ``` ```` |

"toolQuery\_var" is a variable referencing a ToolQuery object. ```` ``` #include <Cam/Tools/ToolQuery.h>  // Get the value of the property. string propertyValue = toolQuery_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |