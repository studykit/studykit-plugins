# DataFolders.objectType Property

Parent Object: [DataFolders](DataFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolders\_var" is a variable referencing a DataFolders object.  ```` ``` # Get the value of the property. propertyValue = dataFolders_var.objectType ``` ```` |

"dataFolders\_var" is a variable referencing a DataFolders object. ```` ``` #include <Core/Dashboard/DataFolders.h>  // Get the value of the property. string propertyValue = dataFolders_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |