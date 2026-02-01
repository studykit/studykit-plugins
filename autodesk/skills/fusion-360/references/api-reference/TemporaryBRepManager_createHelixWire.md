# TemporaryBRepManager.createHelixWire Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Creates a B-Rep body that contains a wire with a single edge that represents a helical curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createHelixWire(axisPoint, axisVector, startPoint, pitch, turns, taperAngle) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns a temporary BRepBody object that contains a wire body that is the shape of the specified helix. Return null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| axisPoint | [Point3D](Point3D.htm) | A Point3D object that defines a point along the axis of the helix. |
| axisVector | [Vector3D](Vector3D.htm) | A Vector3D object that defines the direction of the axis of the helix. |
| startPoint | [Point3D](Point3D.htm) | A Point3D that defines the start point of the helix. This is a point on the helix and defines the starting point of the helix. The distance of this point to the axis defines the starting radius of the helix. |
| pitch | double | The pitch of the helix, or the distance between each of the turns, in centimeters. |
| turns | double | The number of turns of the helix. |
| taperAngle | double | The taper angle of the helix in radians. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |