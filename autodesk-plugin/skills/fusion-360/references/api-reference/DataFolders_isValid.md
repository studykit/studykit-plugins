# DataFolders.isValid Property

Parent Object: [DataFolders](DataFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolders\_var" is a variable referencing a DataFolders object. |

"dataFolders\_var" is a variable referencing a DataFolders object. ```` ``` #include <Core/Dashboard/DataFolders.h>  // Get the value of the property. boolean propertyValue = dataFolders_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |