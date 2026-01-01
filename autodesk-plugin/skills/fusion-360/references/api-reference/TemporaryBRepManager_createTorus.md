# TemporaryBRepManager.createTorus Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Creates a temporary toroidal BRepBody object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createTorus(center, axis, majorRadius, minorRadius) ``` ```` |

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
| center | [Point3D](Point3D.htm) | The center point of the torus. |
| axis | [Vector3D](Vector3D.htm) | The axis of the torus. |
| majorRadius | double | The radius, in centimeters, of the major radius of the torus. If the torus was created by sweeping a circle around another circle this would be the radius of the path circle. |
| minorRadius | double | The radius, in centimeters, of the minor radius of the torus. If the torus was created by sweeping a circle around another circle this would be the radius of the profile circle. |

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