# ConstructionPlane.transform Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Returns the current position and orientation of the construction plane as a matrix. For a parametric construction plane, this property is read-only. For a construction plane in a direct modeling model or in a base feature, this is read-write and can be used to reposition the constructions plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = constructionPlane_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = constructionPlane_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |