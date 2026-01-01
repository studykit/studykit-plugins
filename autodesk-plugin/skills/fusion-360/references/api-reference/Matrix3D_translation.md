# Matrix3D.translation Property

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Gets and sets the translation component of the matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a Matrix3D object. |

"matrix3D\_var" is a variable referencing a Matrix3D object. ```` ``` #include <Core/Geometry/Matrix3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = matrix3D_var->translation();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = matrix3D_var->translation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [moveFeatures.add](moveFeatures_add_Sample.htm) | Demonstrates the moveFeatures.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |