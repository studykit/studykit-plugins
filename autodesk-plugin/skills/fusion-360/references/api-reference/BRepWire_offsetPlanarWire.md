# BRepWire.offsetPlanarWire Method

Parent Object: [BRepWire](BRepWire.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWire.h>

## Description

Method that computes the offset for a planar wire. A BRepBody containing the resulting BRepWire object(s) is returned. It's possible that the offset result of a single wire can result in multiple wires.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWire\_var" is a variable referencing a [BRepWire](BRepWire.htm) object.```` ``` returnValue = bRepWire_var.offsetPlanarWire(planeNormal, distance, cornerType) ``` ```` |

"bRepWire\_var" is a variable referencing a [BRepWire](BRepWire.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns a new temporary BRepBody that contains one or more wires that represent the offset. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planeNormal | [Vector3D](Vector3D.htm) | Input Vector3D object that defines the positive direction of the plane the plane the wire lies on. This vector must be normal to the plane and is used to determine the side to offset the curves to. A positive offset distance is in the direction of the cross product (wire\_tangent x wire\_plane\_normal). A negative offset is in the opposite direction. |
| distance | double | The offset distance in centimeters. See the description for the Normal argument to see how a positive or negative value for the distance specifies the direction of the offset. |
| cornerType | [OffsetCornerTypes](OffsetCornerTypes.htm) | Specifies how the corners are connected when offsetting the curves results in gaps in the corners. See the documentation of the enum for a detailed description of each option. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BrepWire Sample](BrepWireSample_Sample.htm) | BrepWires and BrepWire related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |