# ToolQueryResult.toolLibraryURL Property

Parent Object: [ToolQueryResult](ToolQueryResult.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQueryResult.h>

## Description

The URL defines the location of the ToolLibrary asset in ToolLibraries.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolQueryResult\_var" is a variable referencing a ToolQueryResult object. |

"toolQueryResult\_var" is a variable referencing a ToolQueryResult object. ```` ``` #include <Cam/Tools/ToolQueryResult.h>  // Get the value of the property. Ptr<URL> propertyValue = toolQueryResult_var->toolLibraryURL(); ``` ```` |

## Property Value

This is a read only property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |