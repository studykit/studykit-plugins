# JointGeometry.createByTorusFace Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object based on a torus BRepFace object.

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
| face | [BRepFace](BRepFace.htm) | The torus BRepFace object. |
| azimuthAngle | [JointQuadrantAngleTypes](JointQuadrantAngleTypes.htm) | Specifies the azimuth angle relative to the v parameterization of the input face. The zero, or start angle, is where the v parameter of the sphere is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType. |
| sectionAngle | [JointQuadrantAngleTypes](JointQuadrantAngleTypes.htm) | Specifies the angle relative to the start point of the section circle at give azimuth angle. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |