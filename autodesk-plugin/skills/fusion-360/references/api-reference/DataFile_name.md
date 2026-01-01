# DataFile.name Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Gets and sets the displayed name of this item.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object. |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. string propertyValue = dataFile_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = dataFile_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |