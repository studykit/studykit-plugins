# DataObjectFuture.dataObject Property

Parent Object: [DataObjectFuture](DataObjectFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObjectFuture.h>

## Description

Returns the DataObject when the data has become available, (state returns FinishedFutureState). Returns null if the operation is still running or has failed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. |

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. ```` ``` #include <Core/Dashboard/DataObjectFuture.h>  // Get the value of the property. Ptr<DataObject> propertyValue = dataObjectFuture_var->dataObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataObject](DataObject.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |