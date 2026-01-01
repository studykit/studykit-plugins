# DataFile.publicLink Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and replaced by the functionality on the SharedLink object which can be obtained using the DataFile.sharedLink property. The behavior of this property has changed so it can return an empty string if a public link has not been generated.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object.  ```` ``` # Get the value of the property. propertyValue = dataFile_var.publicLink ``` ```` |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. string propertyValue = dataFile_var->publicLink(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2019
Retired in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |