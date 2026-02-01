# DataEventArgs.status Property

Parent Object: [DataEventArgs](DataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventArgs.h>

## Description

Returns a Status object that provides additional information about the success or failure of the operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. |

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. ```` ``` #include <Core/Dashboard/DataEventArgs.h>  // Get the value of the property. Ptr<Status> propertyValue = dataEventArgs_var->status(); ``` ```` |

## Property Value

This is a read only property whose value is a [Status](Status.htm).

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |