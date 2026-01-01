# BoundingBox2D.combine Method

Parent Object: [BoundingBox2D](BoundingBox2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox2D.h>

## Description

Combines this bounding box with the input bounding box. If the input bounding box extends outside this bounding box then this bounding box will be extended to encompass both of the original bounding boxes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object.```` ``` returnValue = boundingBox2D_var.combine(boundingBox) ``` ```` |

"boundingBox2D\_var" is a variable referencing a [BoundingBox2D](BoundingBox2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the combine was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| boundingBox | [BoundingBox2D](BoundingBox2D.htm) | The other bounding box. It is not edited but is used to extend the boundaries of the bounding box the method is being called on. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |