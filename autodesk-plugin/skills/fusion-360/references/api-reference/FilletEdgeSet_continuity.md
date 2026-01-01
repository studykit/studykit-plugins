# FilletEdgeSet.continuity Property

Parent Object: [FilletEdgeSet](FilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSet.h>

## Description

Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. |

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. ```` ``` #include <Fusion/Features/FilletEdgeSet.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = filletEdgeSet_var->continuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = filletEdgeSet_var->continuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |