# Ellipse3D.set Method

Parent Object: [Ellipse3D](Ellipse3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Sets all of the data defining the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse3D\_var" is a variable referencing an [Ellipse3D](Ellipse3D.htm) object.```` ``` returnValue = ellipse3D_var.set(center, normal, majorAxis, majorRadius, minorRadius) ``` ```` |

"ellipse3D\_var" is a variable referencing an [Ellipse3D](Ellipse3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The center point of the ellipse. |
| normal | [Vector3D](Vector3D.htm) | The normal vector of the ellipse. The plane through the center point and perpendicular to the normal vector defines the plane of the ellipse. |
| majorAxis | [Vector3D](Vector3D.htm) | The major axis of the ellipse. |
| majorRadius | double | The major radius of the of the ellipse. |
| minorRadius | double | The minor radius of the of the ellipse. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |