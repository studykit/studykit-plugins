# DataFileFuture.dataFile Property

Parent Object: [DataFileFuture](DataFileFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFileFuture.h>

## Description

Returns the DataFile when the upload is complete (uplodeState returns UploadFinished). Returns null if the upload is still running or has failed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. |

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. ```` ``` #include <Core/Dashboard/DataFileFuture.h>  // Get the value of the property. Ptr<DataFile> propertyValue = dataFileFuture_var->dataFile(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |