# ToolPreset.objectType Property

Parent Object: [ToolPreset](ToolPreset.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPreset.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPreset\_var" is a variable referencing a ToolPreset object.  ```` ``` # Get the value of the property. propertyValue = toolPreset_var.objectType ``` ```` |

"toolPreset\_var" is a variable referencing a ToolPreset object. ```` ``` #include <Cam/Tools/ToolPreset.h>  // Get the value of the property. string propertyValue = toolPreset_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |