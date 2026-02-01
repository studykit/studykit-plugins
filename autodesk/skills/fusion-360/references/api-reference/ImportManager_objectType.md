# ImportManager.objectType Property

Parent Object: [ImportManager](ImportManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importManager\_var" is a variable referencing an ImportManager object.  ```` ``` # Get the value of the property. propertyValue = importManager_var.objectType ``` ```` |

"importManager\_var" is a variable referencing an ImportManager object. ```` ``` #include <Core/Application/ImportManager.h>  // Get the value of the property. string propertyValue = importManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |