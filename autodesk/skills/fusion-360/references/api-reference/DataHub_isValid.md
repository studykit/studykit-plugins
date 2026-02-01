# DataHub.isValid Property

Parent Object: [DataHub](DataHub.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHub\_var" is a variable referencing a DataHub object. |

"dataHub\_var" is a variable referencing a DataHub object. ```` ``` #include <Core/Dashboard/DataHub.h>  // Get the value of the property. boolean propertyValue = dataHub_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |