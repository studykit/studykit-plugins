# ChamferEdgeSets.objectType Property

Parent Object: [ChamferEdgeSets](ChamferEdgeSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSets.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferEdgeSets\_var" is a variable referencing a ChamferEdgeSets object.  ```` ``` # Get the value of the property. propertyValue = chamferEdgeSets_var.objectType ``` ```` |

"chamferEdgeSets\_var" is a variable referencing a ChamferEdgeSets object. ```` ``` #include <Fusion/Features/ChamferEdgeSets.h>  // Get the value of the property. string propertyValue = chamferEdgeSets_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |