# DataFolder.parentFolder Property

Parent Object: [DataFolder](DataFolder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolder.h>

## Description

Returns the parent folder this folder is contained within. Returns null if this is the project's root folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolder\_var" is a variable referencing a DataFolder object. |

"dataFolder\_var" is a variable referencing a DataFolder object. ```` ``` #include <Core/Dashboard/DataFolder.h>  // Get the value of the property. Ptr<DataFolder> propertyValue = dataFolder_var->parentFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFolder](DataFolder.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |