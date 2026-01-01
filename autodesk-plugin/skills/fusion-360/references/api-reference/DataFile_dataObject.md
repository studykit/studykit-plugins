# DataFile.dataObject Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Starts the process to get the raw binary data associated with this DataFile. Because the data exists on the cloud, a DataObjectFuture is returned that you can use to monitor the state of downloading the data and then getting the raw data once it is available.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object.  ```` ``` # Get the value of the property. propertyValue = dataFile_var.dataObject ``` ```` |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. Ptr<DataObjectFuture> propertyValue = dataFile_var->dataObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataObjectFuture](DataObjectFuture.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |