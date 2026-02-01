# ToolPreset.isValid Property

Parent Object: [ToolPreset](ToolPreset.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPreset.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPreset\_var" is a variable referencing a ToolPreset object. |

"toolPreset\_var" is a variable referencing a ToolPreset object. ```` ``` #include <Cam/Tools/ToolPreset.h>  // Get the value of the property. boolean propertyValue = toolPreset_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |