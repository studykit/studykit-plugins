# MeasureManager.measureMinimumDistance Method

Parent Object: [MeasureManager](MeasureManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MeasureManager.h>

## Description

Measures the minimum distance between the two input geometries.

## Syntax

* [Python](#Python)
* [C++](#C++)

"measureManager\_var" is a variable referencing a [MeasureManager](MeasureManager.htm) object.```` ``` returnValue = measureManager_var.measureMinimumDistance(geometryOne, geometryTwo) ``` ```` |

"measureManager\_var" is a variable referencing a [MeasureManager](MeasureManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeasureResults](MeasureResults.htm) | A MeasureResults object that contains the distance and the two points on the geometry that the distance that was measured between them in centimeters. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| geometryOne | [Base](Base.htm) | The first geometry to measure from. This can be an Occurrence, BRepBody, BRepFace, BRepEdge, BRepVertex, ConstructionPlane, ConstructionAxis, ConstructionPoint, and any sketch entity. The only temporary geometry supported is the Plane object. |
| geometryTwo | [Base](Base.htm) | The first geometry to measure from. This can be an Occurrence, BRepBody, BRepFace, BRepEdge, BRepVertex, ConstructionPlane, ConstructionAxis, ConstructionPoint, and any sketch entity. The only temporary geometry supported is the Plane object. |

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