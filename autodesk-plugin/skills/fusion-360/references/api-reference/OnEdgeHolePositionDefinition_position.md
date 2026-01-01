# OnEdgeHolePositionDefinition.position Property

Parent Object: [OnEdgeHolePositionDefinition](OnEdgeHolePositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OnEdgeHolePositionDefinition.h>

## Description

Returns the position of the hole on the edge. The hole can be at the start, midpoint, or end of the edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"onEdgeHolePositionDefinition\_var" is a variable referencing an OnEdgeHolePositionDefinition object. |

"onEdgeHolePositionDefinition\_var" is a variable referencing an OnEdgeHolePositionDefinition object. ```` ``` #include <Fusion/Features/OnEdgeHolePositionDefinition.h>  // Get the value of the property. HoleEdgePositions propertyValue = onEdgeHolePositionDefinition_var->position(); ``` ```` |

## Property Value

This is a read only property whose value is a [HoleEdgePositions](HoleEdgePositions.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |