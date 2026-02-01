# ToolLibraries.assetTypeName Property

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

Get the name of the asset type which can be accessed by the library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a ToolLibraries object. |

"toolLibraries\_var" is a variable referencing a ToolLibraries object. ```` ``` #include <Cam/Tools/ToolLibraries.h>  // Get the value of the property. string propertyValue = toolLibraries_var->assetTypeName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |