# OrientedBoundingBox3D.setOrientation Method

Parent Object: [OrientedBoundingBox3D](OrientedBoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

Sets the orientation of the oriented bounding box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"orientedBoundingBox3D\_var" is a variable referencing an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm) object.```` ``` returnValue = orientedBoundingBox3D_var.setOrientation(lengthDirection, widthDirection) ``` ```` |

"orientedBoundingBox3D\_var" is a variable referencing an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lengthDirection | [Vector3D](Vector3D.htm) | A Vector3D object that defines the direction of the length of the oriented bounding box. The magnitude of the vector is ignored and just the direction is used. |
| widthDirection | [Vector3D](Vector3D.htm) | A Vector3D object that defines the direction of the width of the oriented bounding box. The magnitude of the vector is ignored and just the direction is used. The width direction must be perpendicular to the length direction. |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |