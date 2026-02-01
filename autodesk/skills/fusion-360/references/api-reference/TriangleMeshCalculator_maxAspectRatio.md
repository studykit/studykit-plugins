# TriangleMeshCalculator.maxAspectRatio Property

Parent Object: [TriangleMeshCalculator](TriangleMeshCalculator.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

Specifies the maximum length to height ratio that a triangle can have. This helps to avoid long skinny triangles. A value of 0 (the default) indicates that no maximum aspect ratio is specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. |

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. ```` ``` #include <Fusion/MeshData/TriangleMeshCalculator.h>  // Get the value of the property. double propertyValue = triangleMeshCalculator_var->maxAspectRatio();  // Set the value of the property, where value_var is a double. bool returnValue = triangleMeshCalculator_var->maxAspectRatio(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |