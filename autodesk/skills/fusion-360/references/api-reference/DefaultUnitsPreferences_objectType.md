# DefaultUnitsPreferences.objectType Property

Parent Object: [DefaultUnitsPreferences](DefaultUnitsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DefaultUnitsPreferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"defaultUnitsPreferences\_var" is a variable referencing a DefaultUnitsPreferences object.  ```` ``` # Get the value of the property. propertyValue = defaultUnitsPreferences_var.objectType ``` ```` |

"defaultUnitsPreferences\_var" is a variable referencing a DefaultUnitsPreferences object. ```` ``` #include <Core/Application/DefaultUnitsPreferences.h>  // Get the value of the property. string propertyValue = defaultUnitsPreferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |