# ApplicationFolders.isValid Property

Parent Object: [ApplicationFolders](ApplicationFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationFolders.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. |

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. ```` ``` #include <Core/Application/ApplicationFolders.h>  // Get the value of the property. boolean propertyValue = applicationFolders_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |