# FileDialog.isValid Property

Parent Object: [FileDialog](FileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FileDialog.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fileDialog\_var" is a variable referencing a FileDialog object. |

"fileDialog\_var" is a variable referencing a FileDialog object. ```` ``` #include <Core/UserInterface/FileDialog.h>  // Get the value of the property. boolean propertyValue = fileDialog_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |