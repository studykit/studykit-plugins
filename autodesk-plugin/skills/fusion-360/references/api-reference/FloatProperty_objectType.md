# FloatProperty.objectType Property

Parent Object: [FloatProperty](FloatProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FloatProperty.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatProperty\_var" is a variable referencing a FloatProperty object.  ```` ``` # Get the value of the property. propertyValue = floatProperty_var.objectType ``` ```` |

"floatProperty\_var" is a variable referencing a FloatProperty object. ```` ``` #include <Core/Application/FloatProperty.h>  // Get the value of the property. string propertyValue = floatProperty_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |