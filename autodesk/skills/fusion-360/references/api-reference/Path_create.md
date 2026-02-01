# Path.create Method

Parent Object: [Path](Path.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

Creates a new Path that can be used as input to various features. For example, it is used to create an open set of curves to create surfaces using extrude, revolve, and sweep. It is also used to create the path for a sweep and sections and profiles and rails for lofts. And it is used to define the boundary of a patch feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. ```` ```  returnValue = adsk.fusion.Path.create(curves, chainOptions) ``` ```` |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Path](Path.htm) | Returns the new Path object or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curves | [Base](Base.htm) | A SketchCurve, BRepEdge, or an ObjectCollection containing multiple sketch entities and/or BRepEdges. If a single sketch curve or BRepEdge is input the chainCurves argument is used to determine if connected curves or edges (they do not need to be tangent) should be automatically found. Searching for connected curves is only performed within the same sketch or open edges on the same body. If multiple curves are provided the chainCurves argument is treated as false so only the specified input curves are used. The input curves need to geometrically connect for a path to be created. |
| chainOptions | [ChainedCurveOptions](ChainedCurveOptions.htm) | If a single SketchCurve or BRepEdge is input, this argument is used to specify the rules in how chained entities should be found. If an ObjectCollection is input, this argument is ignored. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [pathPatternFeatures.add](pathPatternFeatures_add_Sample.htm) | Demonstrates the pathPatternFeatures.add method using a selected body and sketch curve as the path. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |