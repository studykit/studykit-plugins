# BoundingBox3D.contains Method

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

Determines if the specified point is within the bound box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object.```` ``` returnValue = boundingBox3D_var.contains(point) ``` ```` |

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the point is within the bounding box. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point you want to check to see if it's in the bounding box. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |