# BoundingBox3D.expand Method

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

Expands the size of bounding box to include the specified point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object.```` ``` returnValue = boundingBox3D_var.expand(point) ``` ```` |

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the expansion was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to include within the bounding box. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |