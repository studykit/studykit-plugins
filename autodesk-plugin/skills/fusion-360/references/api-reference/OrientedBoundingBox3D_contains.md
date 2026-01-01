# OrientedBoundingBox3D.contains Method

Parent Object: [OrientedBoundingBox3D](OrientedBoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

Determines if the specified point lies within the oriented bounding box.

## Syntax

* [Python](#Python)
* [C++](#C++)

"orientedBoundingBox3D\_var" is a variable referencing an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm) object.```` ``` returnValue = orientedBoundingBox3D_var.contains(point) ``` ```` |

"orientedBoundingBox3D\_var" is a variable referencing an [OrientedBoundingBox3D](OrientedBoundingBox3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the point lies within the bounding box. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to test containment with. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Measure Sample](MeasureSample_Sample.htm) | Measure related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |