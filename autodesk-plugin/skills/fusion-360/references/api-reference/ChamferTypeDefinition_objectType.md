# ChamferTypeDefinition.objectType Property

Parent Object: [ChamferTypeDefinition](ChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferTypeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferTypeDefinition\_var" is a variable referencing a ChamferTypeDefinition object.  ```` ``` # Get the value of the property. propertyValue = chamferTypeDefinition_var.objectType ``` ```` |

"chamferTypeDefinition\_var" is a variable referencing a ChamferTypeDefinition object. ```` ``` #include <Fusion/Features/ChamferTypeDefinition.h>  // Get the value of the property. string propertyValue = chamferTypeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |