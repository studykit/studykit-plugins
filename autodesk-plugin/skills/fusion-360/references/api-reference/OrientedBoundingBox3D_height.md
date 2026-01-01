# OrientedBoundingBox3D.height Property

Parent Object: [OrientedBoundingBox3D](OrientedBoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

Gets and sets the height of the oriented bounding box in centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. |

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. ```` ``` #include <Core/Geometry/OrientedBoundingBox3D.h>  // Get the value of the property. double propertyValue = orientedBoundingBox3D_var->height();  // Set the value of the property, where value_var is a double. bool returnValue = orientedBoundingBox3D_var->height(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

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