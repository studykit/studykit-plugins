# ConstantRadiusFilletEdgeSetInput.continuity Property

Parent Object: [ConstantRadiusFilletEdgeSetInput](ConstantRadiusFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ConstantRadiusFilletEdgeSetInput.h>

## Description

Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType. The default is TangentSurfaceContinuityType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constantRadiusFilletEdgeSetInput\_var" is a variable referencing a ConstantRadiusFilletEdgeSetInput object. |

"constantRadiusFilletEdgeSetInput\_var" is a variable referencing a ConstantRadiusFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/ConstantRadiusFilletEdgeSetInput.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = constantRadiusFilletEdgeSetInput_var->continuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = constantRadiusFilletEdgeSetInput_var->continuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature API Sample](FilletFeatureSample_Sample.htm) | Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |