# Plane.setUVDirections Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Sets the U and V directions of the plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a [Plane](Plane.htm) object.```` ``` returnValue = plane_var.setUVDirections(uDirection, vDirection) ``` ```` |

"plane\_var" is a variable referencing a [Plane](Plane.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| uDirection | [Vector3D](Vector3D.htm) | The U direction for the plane. |
| vDirection | [Vector3D](Vector3D.htm) | The V direction for the plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |