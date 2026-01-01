# JointGeometry.createBySphereFace Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object based on a sphere BRepFace object.

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
| face | [BRepFace](BRepFace.htm) | The sphere BRepFace object. |
| azimuthAngle | [JointQuadrantAngleTypes](JointQuadrantAngleTypes.htm) | Specifies the azimuth angle relative to the v parameterization of the input face. The zero, or start angle, is where the v parameter of the sphere is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType. |
| polarAngle | [JointKeyPointTypes](JointKeyPointTypes.htm) | Specifies the polar angle relative to the u parameterization of the input face. The zero, or start angle, is where the u parameter of the sphere is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartKeyPoint for the north pole, MiddleKeyPoint for points on the equator, or EndKeyPoint for the south pole. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |