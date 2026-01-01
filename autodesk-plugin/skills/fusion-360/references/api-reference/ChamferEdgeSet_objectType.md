# ChamferEdgeSet.objectType Property

Parent Object: [ChamferEdgeSet](ChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSet.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferEdgeSet\_var" is a variable referencing a ChamferEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = chamferEdgeSet_var.objectType ``` ```` |

"chamferEdgeSet\_var" is a variable referencing a ChamferEdgeSet object. ```` ``` #include <Fusion/Features/ChamferEdgeSet.h>  // Get the value of the property. string propertyValue = chamferEdgeSet_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |