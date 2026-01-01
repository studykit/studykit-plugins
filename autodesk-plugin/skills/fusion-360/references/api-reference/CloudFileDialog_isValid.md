# CloudFileDialog.isValid Property

Parent Object: [CloudFileDialog](CloudFileDialog.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CloudFileDialog.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. |

"cloudFileDialog\_var" is a variable referencing a CloudFileDialog object. ```` ``` #include <Core/UserInterface/CloudFileDialog.h>  // Get the value of the property. boolean propertyValue = cloudFileDialog_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |