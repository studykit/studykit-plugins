# Data.dataHubs Property

Parent Object: [Data](Data.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Data.h>

## Description

Returns a collection of accessible hubs for the current user. A DataHub represents an A360 Team or Personal hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"data\_var" is a variable referencing a Data object. |

"data\_var" is a variable referencing a Data object. ```` ``` #include <Core/Dashboard/Data.h>  // Get the value of the property. Ptr<DataHubs> propertyValue = data_var->dataHubs(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataHubs](DataHubs.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |