# EllipticalCylinder.set Method

Parent Object: [EllipticalCylinder](EllipticalCylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Sets the data defining the elliptical cylinder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCylinder\_var" is a variable referencing an [EllipticalCylinder](EllipticalCylinder.htm) object.```` ``` returnValue = ellipticalCylinder_var.set(origin, axis, majorAxis, majorRadius, minorRadius) ``` ```` |

"ellipticalCylinder\_var" is a variable referencing an [EllipticalCylinder](EllipticalCylinder.htm) object. |

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
| majorAxis | [Vector3D](Vector3D.htm) | The direction of the major axis of the ellipse that defines the cylinder. |
| majorRadius | double | The major radius of the ellipse that defines the cylinder. |
| minorRadius | double | The minor radius of the ellipse that defines the cylinder. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |