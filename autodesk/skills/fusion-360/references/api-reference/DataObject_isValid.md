# DataObject.isValid Property

Parent Object: [DataObject](DataObject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObject.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObject\_var" is a variable referencing a DataObject object. |

"dataObject\_var" is a variable referencing a DataObject object. ```` ``` #include <Core/Dashboard/DataObject.h>  // Get the value of the property. boolean propertyValue = dataObject_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |