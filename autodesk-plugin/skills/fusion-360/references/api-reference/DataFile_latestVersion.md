# DataFile.latestVersion Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Returns the latest version of the DataFile. It can return a reference to the same DataFile is this DataFile is the latest version.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object. |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. Ptr<DataFile> propertyValue = dataFile_var->latestVersion(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |