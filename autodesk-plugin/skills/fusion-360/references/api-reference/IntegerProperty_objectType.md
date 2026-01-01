# IntegerProperty.objectType Property

Parent Object: [IntegerProperty](IntegerProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/IntegerProperty.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerProperty\_var" is a variable referencing an IntegerProperty object.  ```` ``` # Get the value of the property. propertyValue = integerProperty_var.objectType ``` ```` |

"integerProperty\_var" is a variable referencing an IntegerProperty object. ```` ``` #include <Core/Application/IntegerProperty.h>  // Get the value of the property. string propertyValue = integerProperty_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |