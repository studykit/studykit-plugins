# BoundingBox2D.contains Method

Parent Object: [BoundingBox2D](BoundingBox2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox2D.h>

## Description

Determines if the specified point lies within the bounding box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object.```` ``` returnValue = boundingBox2D_var.contains(point) ``` ```` |

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the point lies within the bounding box. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point2D](Point2D.htm) | The point to test containment with. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |