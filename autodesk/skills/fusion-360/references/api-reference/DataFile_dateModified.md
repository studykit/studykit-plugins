# DataFile.dateModified Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Returns the date when this data file was modified. Most changes to a file result in a new version which means a new DataFile is created and will have a new creation date. There are a few changes, like rename, that modify a DataFile without creating a new version and the date of that change is returned by this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object.  ```` ``` # Get the value of the property. propertyValue = dataFile_var.dateModified ``` ```` |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. uinteger propertyValue = dataFile_var->dateModified(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |