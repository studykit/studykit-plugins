# TangentRelationshipInput.objectType Property

Parent Object: [TangentRelationshipInput](TangentRelationshipInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationshipInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationshipInput\_var" is a variable referencing a TangentRelationshipInput object.  ```` ``` # Get the value of the property. propertyValue = tangentRelationshipInput_var.objectType ``` ```` |

"tangentRelationshipInput\_var" is a variable referencing a TangentRelationshipInput object. ```` ``` #include <Fusion/Components/TangentRelationshipInput.h>  // Get the value of the property. string propertyValue = tangentRelationshipInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |