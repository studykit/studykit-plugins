# Property.objectType Property

Parent Object: [Property](Property.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Property.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"property\_var" is a variable referencing a Property object.  ```` ``` # Get the value of the property. propertyValue = property_var.objectType ``` ```` |

"property\_var" is a variable referencing a Property object. ```` ``` #include <Core/Application/Property.h>  // Get the value of the property. string propertyValue = property_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |