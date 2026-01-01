# Path.addCurves Method

Parent Object: [Path](Path.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

Adds additional curves to the existing path. This can be useful when creating a complex path for a sweep and you want to include sets of curves from multiple sketches and edges from multiple bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"path\_var" is a variable referencing a [Path](Path.htm) object.```` ``` returnValue = path_var.addCurves(curves, chainOptions) ``` ```` |

"path\_var" is a variable referencing a [Path](Path.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the process was successful or not. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curves | [Base](Base.htm) | A SketchCurve, BRepEdge, or an ObjectCollection containing multiple sketch entities and/or BRepEdges. If a single sketch curve or BRepEdge is input the chainCurves argument is used to determine if connected curves or edges (they do not need to be tangent) should be automatically found. Searching for connected curves is only performed within the same sketch or open edges on the same body. If multiple curves are provided the chainCurves argument is treated as false so only the specified input curves are used. The input curves need to geometrically connect for a path to be created. |
| chainOptions | [ChainedCurveOptions](ChainedCurveOptions.htm) | If a single SketchCurve or BRepEdge is input, this argument is used to specify the rules in how chained entities should be found. If an ObjectCollection is input, this argument is ignored. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |