# DataFolder.id Property

Parent Object: [DataFolder](DataFolder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolder.h>

## Description

Returns the unique ID for this folder. This is the same id used in the APS Data Management API.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolder\_var" is a variable referencing a DataFolder object. |

"dataFolder\_var" is a variable referencing a DataFolder object. ```` ``` #include <Core/Dashboard/DataFolder.h>  // Get the value of the property. string propertyValue = dataFolder_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |