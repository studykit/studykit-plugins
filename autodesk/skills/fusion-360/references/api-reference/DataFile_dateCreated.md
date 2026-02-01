# DataFile.dateCreated Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Returns the date when this data file was created as UNIX epoch time. UNIX epoch time is the number of seconds since January 1, 1970 (midnight UTC/GMT).

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object.  ```` ``` # Get the value of the property. propertyValue = dataFile_var.dateCreated ``` ```` |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. uinteger propertyValue = dataFile_var->dateCreated(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |