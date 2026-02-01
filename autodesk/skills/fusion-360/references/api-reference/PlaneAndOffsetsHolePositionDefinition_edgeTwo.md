# PlaneAndOffsetsHolePositionDefinition.edgeTwo Property

Parent Object: [PlaneAndOffsetsHolePositionDefinition](PlaneAndOffsetsHolePositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PlaneAndOffsetsHolePositionDefinition.h>

## Description

The second of two edges the hole position is measured from. OffsetTwo provides access to the model parameter controlling the offset distance. This property can return null in the case where only one edge is used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planeAndOffsetsHolePositionDefinition\_var" is a variable referencing a PlaneAndOffsetsHolePositionDefinition object. |

"planeAndOffsetsHolePositionDefinition\_var" is a variable referencing a PlaneAndOffsetsHolePositionDefinition object. ```` ``` #include <Fusion/Features/PlaneAndOffsetsHolePositionDefinition.h>  // Get the value of the property. Ptr<BRepEdge> propertyValue = planeAndOffsetsHolePositionDefinition_var->edgeTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepEdge](BRepEdge.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |