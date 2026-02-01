# JointGeometry.createByTwoEdgeIntersection Method

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Creates a new transient JointGeometry object that is positioned at the intersection of the two input linear BRepEdge objects.

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
| edgeOne | [BRepEdge](BRepEdge.htm) | The first linear BRepEdge object. |
| edgeTwo | [BRepEdge](BRepEdge.htm) | The second linear BRepEdge object. This edge must exist either on the same body as edgeOne or on a body in the same component as edgeOne. edgeOne and edgeTwo must also both lie on the same plane and must intersect, they cannot be parallel. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |