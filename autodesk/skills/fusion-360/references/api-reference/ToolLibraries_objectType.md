# ToolLibraries.objectType Property

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a ToolLibraries object.  ```` ``` # Get the value of the property. propertyValue = toolLibraries_var.objectType ``` ```` |

"toolLibraries\_var" is a variable referencing a ToolLibraries object. ```` ``` #include <Cam/Tools/ToolLibraries.h>  // Get the value of the property. string propertyValue = toolLibraries_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |