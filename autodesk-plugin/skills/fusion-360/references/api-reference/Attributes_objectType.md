# Attributes.objectType Property

Parent Object: [Attributes](Attributes.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attributes.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attributes\_var" is a variable referencing an Attributes object.  ```` ``` # Get the value of the property. propertyValue = attributes_var.objectType ``` ```` |

"attributes\_var" is a variable referencing an Attributes object. ```` ``` #include <Core/Application/Attributes.h>  // Get the value of the property. string propertyValue = attributes_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |