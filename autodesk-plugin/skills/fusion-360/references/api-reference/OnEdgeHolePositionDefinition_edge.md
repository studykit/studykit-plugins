# OnEdgeHolePositionDefinition.edge Property

Parent Object: [OnEdgeHolePositionDefinition](OnEdgeHolePositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OnEdgeHolePositionDefinition.h>

## Description

Returns the edge the hole is positioned on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"onEdgeHolePositionDefinition\_var" is a variable referencing an OnEdgeHolePositionDefinition object. |

"onEdgeHolePositionDefinition\_var" is a variable referencing an OnEdgeHolePositionDefinition object. ```` ``` #include <Fusion/Features/OnEdgeHolePositionDefinition.h>  // Get the value of the property. Ptr<BRepEdge> propertyValue = onEdgeHolePositionDefinition_var->edge(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepEdge](BRepEdge.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |