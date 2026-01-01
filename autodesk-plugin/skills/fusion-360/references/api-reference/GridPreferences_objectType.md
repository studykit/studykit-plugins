# GridPreferences.objectType Property

Parent Object: [GridPreferences](GridPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GridPreferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"gridPreferences\_var" is a variable referencing a GridPreferences object.  ```` ``` # Get the value of the property. propertyValue = gridPreferences_var.objectType ``` ```` |

"gridPreferences\_var" is a variable referencing a GridPreferences object. ```` ``` #include <Core/Application/GridPreferences.h>  // Get the value of the property. string propertyValue = gridPreferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |