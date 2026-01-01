# TemporaryBRepManager.createCylinderOrCone Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Creates a temporary solid cylinder or cone BRepBody object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createCylinderOrCone(pointOne, pointOneRadius, pointTwo, pointTwoRadius) ``` ```` |

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
| pointOneRadius | double | The radius of the cylinder or cone at the point one end, in centimeters. |
| pointTwo | [Point3D](Point3D.htm) | A point at the opposite end of the cylinder or cone. |
| pointTwoRadius | double | The radius of the cylinder or cone at the point two end, in centimeters. For a cylinder the pointTwoRadius should be equal to the pointOneRadius. |

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