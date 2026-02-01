# Data.activeHub Property

Parent Object: [Data](Data.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Data.h>

## Description

Gets the active DataHub.

## Remarks

Setting the active hub is not supported within any of the Command related events. When a command is running, a transaction is open, and changing the active hub cannot be transacted and, as a result, cannot be contained within a command transaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"data\_var" is a variable referencing a Data object. |

"data\_var" is a variable referencing a Data object. ```` ``` #include <Core/Dashboard/Data.h>  // Get the value of the property. Ptr<DataHub> propertyValue = data_var->activeHub();  // Set the value of the property, where value_var is a DataHub. bool returnValue = data_var->activeHub(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DataHub](DataHub.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |