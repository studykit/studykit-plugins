# BoundingBox2D.intersects Method

Parent Object: [BoundingBox2D](BoundingBox2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox2D.h>

## Description

Test if this bounding box intersects with the specified bounding box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object.```` ``` returnValue = boundingBox2D_var.intersects(boundingBox) ``` ```` |

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the bounding boxes intersect. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| boundingBox | [BoundingBox2D](BoundingBox2D.htm) | The bounding box to test intersection with. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |