# GeometricConstraints.addOffset Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

To access the full capabilities supported by offset, you should use the createOffsetInput and addOffset2 methods.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addOffset(curves, offset, basePoint) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.  ```` ``` #include <Fusion/Sketch/GeometricConstraints.h>  returnValue = geometricConstraints_var->addOffset(curves, offset, basePoint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetConstraint](OffsetConstraint.htm) | The created OffsetConstraint. You can use properties on the constraint to get information about the offset. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curves | SketchCurve[] | A set of end connected curves. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves. |
| offset | [ValueInput](ValueInput.htm) | The value that defines the offset. This is a ValueInput object so it can be a float value to define the offset in centimeters or it can be a string defining an expression that will be used by the dimension that controls the offset. |
| basePoint | [Point3D](Point3D.htm) | The location on one of the curves where the offset dimension will be created. |

## Version

Introduced in version September 2022
Retired in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |