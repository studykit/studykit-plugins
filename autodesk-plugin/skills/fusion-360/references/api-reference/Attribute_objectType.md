# Attribute.objectType Property

Parent Object: [Attribute](Attribute.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attribute.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attribute\_var" is a variable referencing an Attribute object.  ```` ``` # Get the value of the property. propertyValue = attribute_var.objectType ``` ```` |

"attribute\_var" is a variable referencing an Attribute object. ```` ``` #include <Core/Application/Attribute.h>  // Get the value of the property. string propertyValue = attribute_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |