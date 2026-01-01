# DataFolder.dataFiles Property

Parent Object: [DataFolder](DataFolder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolder.h>

## Description

Returns a collection containing all of the items within this folder, excluding folders. Use the dataFolders property to get the folders.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolder\_var" is a variable referencing a DataFolder object. |

"dataFolder\_var" is a variable referencing a DataFolder object. ```` ``` #include <Core/Dashboard/DataFolder.h>  // Get the value of the property. Ptr<DataFiles> propertyValue = dataFolder_var->dataFiles(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFiles](DataFiles.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |