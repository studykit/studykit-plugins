# JointGeometry.createBySplineFace Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object based on a spline BRepFace object.

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
| face | [BRepFace](BRepFace.htm) | The spline BRepFace object. |
| paramU | [JointKeyPointTypes](JointKeyPointTypes.htm) | Specifies the u parameter of the input spline face where the joint keypoint will be located. The possible values can be StartKeyPoint, MiddleKeyPoint or EndKeyPoint. |
| paramV | [JointKeyPointTypes](JointKeyPointTypes.htm) | Specifies the v parameter of the input spline face where the joint keypoint will be located. The possible values can be StartKeyPoint, MiddleKeyPoint or EndKeyPoint. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |