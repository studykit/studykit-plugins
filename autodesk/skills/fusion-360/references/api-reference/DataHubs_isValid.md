# DataHubs.isValid Property

Parent Object: [DataHubs](DataHubs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHubs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHubs\_var" is a variable referencing a DataHubs object. |

"dataHubs\_var" is a variable referencing a DataHubs object. ```` ``` #include <Core/Dashboard/DataHubs.h>  // Get the value of the property. boolean propertyValue = dataHubs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |