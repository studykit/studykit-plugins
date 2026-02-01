# JointGeometry.createByProfile Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object based on a planar BRepFace object. A JointGeometry object can be used to create a joint or joint origin.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointGeometry](JointGeometry.htm) | Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| profile | [Profile](Profile.htm) | The Profile object. |
| sketchCurve | [SketchCurve](SketchCurve.htm) | A sketch curve that is part of the input profile. This argument can be null in the case where the keyPointType is CenterKeypoint indicating the center of the profile is to be used. When a curve is used, the keyPointType specifies the position along the curve for the keypoint. |
| keyPointType | [JointKeyPointTypes](JointKeyPointTypes.htm) | Specifies the position along the curve where the joint keypoint will be located. For open curves (lines, arcs, elliptical arcs, and open splines) this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint. For closed analytic (circles and ellipses), it must be CenterKeyPoint. When no curve is specified, it must be CenterKeyPoint indicating the center of area of the profile is to be used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [RevoluteJointMotion API Sample](RevoluteJointMotionSample_Sample.htm) | Demonstrates creating a joint with revolute joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |