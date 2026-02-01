# JointGeometry.createByCylinderOrConeFace Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object based on a cylinder or cone BRepFace object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointGeometry](JointGeometry.htm) | Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| face | [BRepFace](BRepFace.htm) | The cylindrical or conical BRepFace object. |
| angle | [JointQuadrantAngleTypes](JointQuadrantAngleTypes.htm) | Specifies the angle relative to the parameterization of the input face. The zero, or start angle, is where the v parameter of the cylinder is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType. |
| height | [JointKeyPointTypes](JointKeyPointTypes.htm) | Specifies the vertical position relative to the bottom of the cylinder at the given angle. The possible values can be StartKeyPoint, MiddleKeyPoint or EndKeyPoint. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |