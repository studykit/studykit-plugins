# DataEventArgs.isValid Property

Parent Object: [DataEventArgs](DataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. |

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. ```` ``` #include <Core/Dashboard/DataEventArgs.h>  // Get the value of the property. boolean propertyValue = dataEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |