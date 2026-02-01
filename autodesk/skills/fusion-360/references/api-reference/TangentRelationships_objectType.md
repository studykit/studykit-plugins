# TangentRelationships.objectType Property

Parent Object: [TangentRelationships](TangentRelationships.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationships.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationships\_var" is a variable referencing a TangentRelationships object.  ```` ``` # Get the value of the property. propertyValue = tangentRelationships_var.objectType ``` ```` |

"tangentRelationships\_var" is a variable referencing a TangentRelationships object. ```` ``` #include <Fusion/Components/TangentRelationships.h>  // Get the value of the property. string propertyValue = tangentRelationships_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |