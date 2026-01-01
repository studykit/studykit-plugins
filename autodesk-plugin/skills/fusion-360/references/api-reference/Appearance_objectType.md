# Appearance.objectType Property

Parent Object: [Appearance](Appearance.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearance.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearance\_var" is a variable referencing an Appearance object.  ```` ``` # Get the value of the property. propertyValue = appearance_var.objectType ``` ```` |

"appearance\_var" is a variable referencing an Appearance object. ```` ``` #include <Core/Materials/Appearance.h>  // Get the value of the property. string propertyValue = appearance_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |