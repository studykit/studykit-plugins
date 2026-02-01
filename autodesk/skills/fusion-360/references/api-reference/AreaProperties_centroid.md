# AreaProperties.centroid Property

Parent Object: [AreaProperties](AreaProperties.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AreaProperties.h>

## Description

Gets the centroid where the units are centimeters. The Location is relative to the sketch origin for a profile or relative to the world coordinate system for a planar face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"areaProperties\_var" is a variable referencing an AreaProperties object. |

"areaProperties\_var" is a variable referencing an AreaProperties object. ```` ``` #include <Fusion/Fusion/AreaProperties.h>  // Get the value of the property. Ptr<Point3D> propertyValue = areaProperties_var->centroid(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point3D](Point3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample for AreaProperties](AreaPropertiesSample_Sample.htm) | Demonstrates how to use AreaProperties |

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |