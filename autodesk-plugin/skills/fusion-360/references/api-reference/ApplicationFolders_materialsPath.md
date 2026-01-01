# ApplicationFolders.materialsPath Property

Parent Object: [ApplicationFolders](ApplicationFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationFolders.h>

## Description

Returns the path where user-created material and appearance libraries are saved.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. |

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. ```` ``` #include <Core/Application/ApplicationFolders.h>  // Get the value of the property. string propertyValue = applicationFolders_var->materialsPath(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |