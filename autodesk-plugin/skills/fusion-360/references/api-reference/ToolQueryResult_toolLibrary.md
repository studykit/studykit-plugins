# ToolQueryResult.toolLibrary Property

Parent Object: [ToolQueryResult](ToolQueryResult.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQueryResult.h>

## Description

The ToolLibrary contains a Tool that matches the query.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolQueryResult\_var" is a variable referencing a ToolQueryResult object. |

"toolQueryResult\_var" is a variable referencing a ToolQueryResult object. ```` ``` #include <Cam/Tools/ToolQueryResult.h>  // Get the value of the property. Ptr<ToolLibrary> propertyValue = toolQueryResult_var->toolLibrary(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolLibrary](ToolLibrary.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |