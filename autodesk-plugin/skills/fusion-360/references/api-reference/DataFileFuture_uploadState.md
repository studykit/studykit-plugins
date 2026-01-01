# DataFileFuture.uploadState Property

Parent Object: [DataFileFuture](DataFileFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFileFuture.h>

## Description

Returns the current state of the upload.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. |

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. ```` ``` #include <Core/Dashboard/DataFileFuture.h>  // Get the value of the property. UploadStates propertyValue = dataFileFuture_var->uploadState(); ``` ```` |

## Property Value

This is a read only property whose value is a [UploadStates](UploadStates.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |