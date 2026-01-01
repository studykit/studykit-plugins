# TemporaryBRepManager.createSphere Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Creates a temporary spherical BRepBody object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.```` ``` returnValue = temporaryBRepManager_var.createSphere(center, radius) ``` ```` |

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
| center | [Point3D](Point3D.htm) | The center point of the sphere. |
| radius | double | The radius of the sphere in centimeters. |

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