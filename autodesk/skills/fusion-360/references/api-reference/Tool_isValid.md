# Tool.isValid Property

Parent Object: [Tool](Tool.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/Tool.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tool\_var" is a variable referencing a Tool object. |

"tool\_var" is a variable referencing a Tool object. ```` ``` #include <Cam/Tools/Tool.h>  // Get the value of the property. boolean propertyValue = tool_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |