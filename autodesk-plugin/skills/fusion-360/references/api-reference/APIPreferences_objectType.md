# APIPreferences.objectType Property

Parent Object: [APIPreferences](APIPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"aPIPreferences\_var" is a variable referencing an APIPreferences object.  ```` ``` # Get the value of the property. propertyValue = aPIPreferences_var.objectType ``` ```` |

"aPIPreferences\_var" is a variable referencing an APIPreferences object. ```` ``` #include <Core/Application/APIPreferences.h>  // Get the value of the property. string propertyValue = aPIPreferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |