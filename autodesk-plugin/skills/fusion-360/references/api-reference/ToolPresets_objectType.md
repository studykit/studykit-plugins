# ToolPresets.objectType Property

Parent Object: [ToolPresets](ToolPresets.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPresets.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPresets\_var" is a variable referencing a ToolPresets object.  ```` ``` # Get the value of the property. propertyValue = toolPresets_var.objectType ``` ```` |

"toolPresets\_var" is a variable referencing a ToolPresets object. ```` ``` #include <Cam/Tools/ToolPresets.h>  // Get the value of the property. string propertyValue = toolPresets_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |