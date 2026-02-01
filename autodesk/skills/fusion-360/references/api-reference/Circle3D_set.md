# Circle3D.set Method

Parent Object: [Circle3D](Circle3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle3D.h>

## Description

Sets all of the data defining the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle3D\_var" is a variable referencing a [Circle3D](Circle3D.htm) object.```` ``` returnValue = circle3D_var.set(center, normal, radius) ``` ```` |

"circle3D\_var" is a variable referencing a [Circle3D](Circle3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The center point of the circle. |
| normal | [Vector3D](Vector3D.htm) | The normal vector of the circle. The plane through the center point and perpendicular to the normal vector defines the plane of the circle. |
| radius | double | The radius of the circle. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |