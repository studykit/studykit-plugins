# UnitsManager.objectType Property

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a UnitsManager object.  ```` ``` # Get the value of the property. propertyValue = unitsManager_var.objectType ``` ```` |

"unitsManager\_var" is a variable referencing a UnitsManager object. ```` ``` #include <Core/Application/UnitsManager.h>  // Get the value of the property. string propertyValue = unitsManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |