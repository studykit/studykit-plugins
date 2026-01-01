# TriangleMeshCalculator.maxSideLength Property

Parent Object: [TriangleMeshCalculator](TriangleMeshCalculator.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

Specifies the maximum side of any triangle in the mesh. A value of 0 (the default) indicates that no maximum length is specified. The value is specified in centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. |

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. ```` ``` #include <Fusion/MeshData/TriangleMeshCalculator.h>  // Get the value of the property. double propertyValue = triangleMeshCalculator_var->maxSideLength();  // Set the value of the property, where value_var is a double. bool returnValue = triangleMeshCalculator_var->maxSideLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |