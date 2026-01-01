# BoundingBox2D.expand Method

Parent Object: [BoundingBox2D](BoundingBox2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox2D.h>

## Description

Expand this bounding box to contain the specified point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object.```` ``` returnValue = boundingBox2D_var.expand(point) ``` ```` |

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point2D](Point2D.htm) | The point to expand the box to. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |