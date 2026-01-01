# TriangleMeshCalculator.surfaceTolerance Property

Parent Object: [TriangleMeshCalculator](TriangleMeshCalculator.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

Specifies the maximum distance that the mesh can deviate from the smooth surface. The value is in centimeters. Smaller values can result in a much greater number of facets being returned and will require more processing time to calculate.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. |

"triangleMeshCalculator\_var" is a variable referencing a TriangleMeshCalculator object. ```` ``` #include <Fusion/MeshData/TriangleMeshCalculator.h>  // Get the value of the property. double propertyValue = triangleMeshCalculator_var->surfaceTolerance();  // Set the value of the property, where value_var is a double. bool returnValue = triangleMeshCalculator_var->surfaceTolerance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |