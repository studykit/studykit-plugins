# GeometricConstraints.addTwoSidesOffset Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates two offset constraints, which results in creating two new sets of curves that are an offset of the input curves on each side of the original set of curves. The returned offset constraint objects provide access to the created curves and the parameters controlling the offsets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addTwoSidesOffset(input, linkOffsets) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetConstraint](OffsetConstraint.htm)[] | Returns an array containing the two OffsetConstraint objects or errors if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [OffsetConstraintInput](OffsetConstraintInput.htm) | The OffsetConstraintInput object that defines the offset to create. The same definition applies to both offsets that are created. |
| linkOffsets | boolean | Defines if the parameter driving the offset of the second side should reference the parameter of the first side. This sets up the parameters so if the first side is edited, the second side will automatically update using the same value. A value of true will create the linked parameter. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |