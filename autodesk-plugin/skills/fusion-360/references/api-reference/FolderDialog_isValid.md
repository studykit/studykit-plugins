# FolderDialog.isValid Property

Parent Object: [FolderDialog](FolderDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FolderDialog.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"folderDialog\_var" is a variable referencing a FolderDialog object. |

"folderDialog\_var" is a variable referencing a FolderDialog object. ```` ``` #include <Core/UserInterface/FolderDialog.h>  // Get the value of the property. boolean propertyValue = folderDialog_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |