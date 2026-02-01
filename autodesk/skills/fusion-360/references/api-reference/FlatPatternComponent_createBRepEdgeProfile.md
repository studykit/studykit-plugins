# FlatPatternComponent.createBRepEdgeProfile Method

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Creates a profile based on the outside open edges of a BRepFace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.  ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Uses no optional arguments. returnValue = flatPatternComponent_var->createBRepEdgeProfile(edges);  // Uses optional arguments. returnValue = flatPatternComponent_var->createBRepEdgeProfile(edges, chainEdges); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Profile](Profile.htm) | Returns the new Profile object or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edges | [Base](Base.htm) | A single BRepEdge object or an ObjectCollection containing multiple BRepEdge objects, or a BRepLoop object. If a single edge is input, the chainEdges argument is checked to determine if connected edges (they do not need to be tangent) should be automatically found. If multiple edges are provided the chainEdges argument is always treated as false so you must provide all of the edges in the object collection that you want included in the profile. and the edges must all connect together in a single path. if a BRepLoop object is provided, all of the edges in the loop are included in the profile and the chainEdges argument is ignored. |
| chainEdges | boolean | If true, this finds any edges that connect to the single input edge and automatically includes them in the profile. If false, only the edges provided will be used to define the profile. This argument is ignored and treated as false if multiple edges or a BRepLoop is input.   This is an optional argument whose default value is True. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |