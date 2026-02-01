# BoundingBox3D.combine Method

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

Combines this bounding box with the input bounding box. If the input bounding box extends outside this bounding box then this bounding box will be extended to encompass both of the original bounding boxes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object.```` ``` returnValue = boundingBox3D_var.combine(boundingBox) ``` ```` |

"boundingBox3D\_var" is a variable referencing a [BoundingBox3D](BoundingBox3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the combine was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| boundingBox | [BoundingBox3D](BoundingBox3D.htm) | The other bounding box. It is not edited but is used to extend the boundaries of the bounding box the method is being called on. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |