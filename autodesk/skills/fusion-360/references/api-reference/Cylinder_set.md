# Cylinder.set Method

Parent Object: [Cylinder](Cylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cylinder.h>

## Description

Sets the data that defines the cylinder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinder\_var" is a variable referencing a [Cylinder](Cylinder.htm) object.```` ``` returnValue = cylinder_var.set(origin, axis, radius) ``` ```` |

"cylinder\_var" is a variable referencing a [Cylinder](Cylinder.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point (center) of the base of the cylinder. |
| axis | [Vector3D](Vector3D.htm) | The center axis (along the length) of the cylinder that defines its normal direction. |
| radius | double | The radius of the cylinder. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |