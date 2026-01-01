# MeasureManager.measureAngle Method

Parent Object: [MeasureManager](MeasureManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureManager.h>

## Description

Measures the angle between the input geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"measureManager\_var" is a variable referencing a [MeasureManager](MeasureManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"measureManager\_var" is a variable referencing a [MeasureManager](MeasureManager.htm) object.  ```` ``` #include <Core/Application/MeasureManager.h>  // Uses no optional arguments. returnValue = measureManager_var->measureAngle(geometryOne, geometryTwo);  // Uses optional arguments. returnValue = measureManager_var->measureAngle(geometryOne, geometryTwo, geometryThree); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeasureResults](MeasureResults.htm) | A MeasureResults object that contains the angle and the two points on the geometry that the angle that was measured between them in radians. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometryOne | [Base](Base.htm) | The first geometry to measure the angle to. This can be any 3D point geometry (Construction Point, Vertex, SketchPoint, or Point3D), any 3D linear geometry (Construction Axis, linear BRepEdge, SketchLine, Line3D, or InfiniteLine3D), or any planar geometry (Construction Plane, planar BRepFace, or Plane). |
| geometryTwo | [Base](Base.htm) | The second geometry to measure the angle to. This can be any 3D point geometry (Construction Point, Vertex, SketchPoint, or Point3D), any 3D linear geometry (Construction Axis, linear BRepEdge, SketchLine, Line3D, or InfiniteLine3D), or any planar geometry (Construction Plane, planar BRepFace, or Plane). |
| geometryThree | [Base](Base.htm) | The optional third geometry to measure the angle to. This is only used when the first two geometries are points and this defines the third point. When three points define a triangle, the apex of the triangle is defined by the second point. A point can be defined by a Construction Point, Vertex, SketchPoint, or Point3D object.   This is an optional argument whose default value is null. |

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