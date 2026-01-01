# ToolQuery.vendor Property

Parent Object: [ToolQuery](ToolQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQuery.h>

## Description

The case-insensitive vendor specifies the vendor of the tool. The default empty vendor applies to all tools.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolQuery\_var" is a variable referencing a ToolQuery object. |

"toolQuery\_var" is a variable referencing a ToolQuery object. ```` ``` #include <Cam/Tools/ToolQuery.h>  // Get the value of the property. string propertyValue = toolQuery_var->vendor();  // Set the value of the property, where value_var is a string. bool returnValue = toolQuery_var->vendor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |