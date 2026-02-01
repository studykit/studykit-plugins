# ToolLibraries.isValid Property

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a ToolLibraries object. |

"toolLibraries\_var" is a variable referencing a ToolLibraries object. ```` ``` #include <Cam/Tools/ToolLibraries.h>  // Get the value of the property. boolean propertyValue = toolLibraries_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |