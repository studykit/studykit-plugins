# JointGeometry.createByTangentFaceEdge Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object based on a BRepFace object as well as a BRepEdge object which is on the BRepFace.

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
| face | [BRepFace](BRepFace.htm) | The cylindrical, conical, spherical, toroidal or spline BRepFace object. |
| edge | [BRepEdge](BRepEdge.htm) | A BRepEdge object that is one of the edges on the selected face. |
| edgePointType | [JointTangentFaceEdgePointTypes](JointTangentFaceEdgePointTypes.htm) | Specifies the position along the edge where the joint keypoint will be located. The possible values depend on whether the edge is closed or not. For closed edge, the possible values can be StartJointTangentFaceEdgePointType, QuarterJointTangentFaceEdgePointType, MiddleJointTangentFaceEdgePointType or ThirdQuarterJointTangentFaceEdgePointType. For open edge, the possible values can be StartJointTangentFaceEdgePointType, MiddleJointTangentFaceEdgePointType, or EndJointTangentFaceEdgePointType. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |