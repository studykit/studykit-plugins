# DataFileFuture.isValid Property

Parent Object: [DataFileFuture](DataFileFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFileFuture.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. |

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. ```` ``` #include <Core/Dashboard/DataFileFuture.h>  // Get the value of the property. boolean propertyValue = dataFileFuture_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |