# TemporaryBRepManager.createEllipticalCylinderOrCone Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Creates a temporary elliptical solid cylinder or cone BrepBody object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createEllipticalCylinderOrCone(pointOne, pointOneMajorRadius, pointOneMinorRadius, pointTwo, pointTwoMajorRadius, majorAxisDirection) ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the newly created temporary BRepBody object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOne | [Point3D](Point3D.htm) | A point at one end of the cylinder or cone. |
| pointOneMajorRadius | double | The major radius of the cylinder or cone at the point one end, in centimeters. |
| pointOneMinorRadius | double | The minor radius of the cylinder or cone at the point one end, in centimeters. |
| pointTwo | [Point3D](Point3D.htm) | A point at the opposite end of the cone. |
| pointTwoMajorRadius | double | The major radius of the cylinder or cone at the point two end, in centimeters. The minor radius is automatically determined using the point one ratio of the minor and major radii. |
| majorAxisDirection | [Vector3D](Vector3D.htm) | A Vector3D object that defines the direction of the major axis. |

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