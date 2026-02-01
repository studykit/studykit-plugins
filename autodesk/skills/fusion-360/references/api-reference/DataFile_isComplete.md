# DataFile.isComplete Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Returns if the DataFile is fully processed. This is especially useful when a new file is being saved or uploaded. The initial call to save or upload the file returns when the process has started but processing continues on the cloud. This property will return true when all of the processing has been completed and all information related to the Datafile is now available.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object. |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. boolean propertyValue = dataFile_var->isComplete(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |