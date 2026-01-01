# BRepLoop.edges Property

Parent Object: [BRepLoop](BRepLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoop.h>

## Description

Returns the BRepEdges used by this loop

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoop\_var" is a variable referencing a BRepLoop object. |

"bRepLoop\_var" is a variable referencing a BRepLoop object. ```` ``` #include <Fusion/BRep/BRepLoop.h>  // Get the value of the property. Ptr<BRepEdges> propertyValue = bRepLoop_var->edges(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepEdges](BRepEdges.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |