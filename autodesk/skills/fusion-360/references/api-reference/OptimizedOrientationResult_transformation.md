# OptimizedOrientationResult.transformation Property

Parent Object: [OptimizedOrientationResult](OptimizedOrientationResult.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/OptimizedOrientationResult.h>

## Description

The transformation matrix to be applied onto the occurrence's existing transformation at the time of the calculation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"optimizedOrientationResult\_var" is a variable referencing an OptimizedOrientationResult object. |

"optimizedOrientationResult\_var" is a variable referencing an OptimizedOrientationResult object. ```` ``` #include <Cam/GeneratedData/OptimizedOrientationResult.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = optimizedOrientationResult_var->transformation(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |