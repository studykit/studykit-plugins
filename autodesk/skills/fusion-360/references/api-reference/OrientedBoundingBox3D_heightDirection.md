# OrientedBoundingBox3D.heightDirection Property

Parent Object: [OrientedBoundingBox3D](OrientedBoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

Gets the direction of the height of the oriented bounding box. A unit vector is always returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. |

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. ```` ``` #include <Core/Geometry/OrientedBoundingBox3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = orientedBoundingBox3D_var->heightDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

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