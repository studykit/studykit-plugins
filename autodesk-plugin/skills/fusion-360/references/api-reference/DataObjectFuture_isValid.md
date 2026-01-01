# DataObjectFuture.isValid Property

Parent Object: [DataObjectFuture](DataObjectFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObjectFuture.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. |

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. ```` ``` #include <Core/Dashboard/DataObjectFuture.h>  // Get the value of the property. boolean propertyValue = dataObjectFuture_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |