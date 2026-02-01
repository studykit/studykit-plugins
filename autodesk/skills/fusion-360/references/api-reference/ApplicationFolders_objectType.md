# ApplicationFolders.objectType Property

Parent Object: [ApplicationFolders](ApplicationFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationFolders.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationFolders\_var" is a variable referencing an ApplicationFolders object.  ```` ``` # Get the value of the property. propertyValue = applicationFolders_var.objectType ``` ```` |

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. ```` ``` #include <Core/Application/ApplicationFolders.h>  // Get the value of the property. string propertyValue = applicationFolders_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |