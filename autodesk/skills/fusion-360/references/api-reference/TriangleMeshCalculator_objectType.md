# TriangleMeshCalculator.objectType Property

Parent Object: [TriangleMeshCalculator](TriangleMeshCalculator.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object.  ```` ``` # Get the value of the property. propertyValue = triangleMeshCalculator_var.objectType ``` ```` |

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. ```` ``` #include <Fusion/MeshData/TriangleMeshCalculator.h>  // Get the value of the property. string propertyValue = triangleMeshCalculator_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |