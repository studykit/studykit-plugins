# BoundingBox3D.intersects Method

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

Determines if the two bounding boxes intersect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object.```` ``` returnValue = boundingBox3D_var.intersects(boundingBox) ``` ```` |

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the two boxes intersect. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| boundingBox | [BoundingBox3D](BoundingBox3D.htm) | The other bounding box to check for intersection with. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |